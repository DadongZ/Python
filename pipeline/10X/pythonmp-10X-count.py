import subprocess
import os
import yaml
import time
import pandas as pd
import multiprocessing
import functools


with open("settings.yml", 'r') as stream:
    try:
        yml = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

# Parse out YAML settings file
makefastq = yml['makefastq']
getcounts = yml['getcounts']
showcmd   = yml['showcmd']

cranger  = yml['cranger']
bcl2fastq= yml['bcl2fastq']

projid   = yml['projid']
datadir  = yml['datadir']
refdir   = yml['refdir']
logdir   = yml['logdir']
fastqdir = os.path.join(projid, 'outs/fastq_path/')

cjobs  = yml['cjobs']
ccores = yml['ccores']
fcores = yml['fcores']
ncells = yml['ncells']

sampleids = yml['sampleids']
sampsheet = yml['sampsheet']
sampskip  = yml['sampskip']
sampidcol = yml['sampidcol']
sampdelim = yml['sampdelim']


# Add bcl2fastq to UNIX PATH and print version
os.environ['PATH'] = os.environ.get('PATH') + ":" + bcl2fastq
print("Check bclfastq version")
subprocess.Popen(['bcl2fastq', '--version'])


# Read in samples from settings or sample sheet
if sampleids is None:
    # Read in sample ids from sample sheet
    sampdf = pd.read_csv(sampsheet, sep = ",", skiprows = sampskip)
    mysampids = list(sampdf[sampidcol])
else:
    mysampids = sampleids

# Function to process cellranger count for each sample
def _my10Xsample(sampid, cmdlist, logdir, showcmd):
    sampcmd = cmdlist+['--id', sampid, '--sample', sampid]
    fout = os.path.join(logdir, sampid+".out")
    ferr = os.path.join(logdir, sampid+".err")
    if showcmd:
        print(sampcmd)
    with open(fout, 'w') as stdout, open(ferr, 'w') as stderr:
        p = subprocess.Popen(sampcmd, stdout = stdout, stderr = stderr)
        p.wait()





# Process BCL -> FASTQ
if makefastq:
    # Check for log directories
    if not os.path.exists(logdir):
        os.mkdir(logdir)

    fcores = str(min(fcores, len(mysampids)))
    mkfcmd = [cranger, 'mkfastq',
              '--id='         + projid,
              '--qc',
              '--run='        + datadir,
              '--output-dir=' + fastqdir,
              '--samplesheet='+ sampsheet,
              '--localcores=' + fcores]

    fout = os.path.join(logdir, "mkfastq" + ".out")
    ferr = os.path.join(logdir, "mkfastq" + ".err")

    if showcmd:
        print(mkfcmd)
    
    with open(fout, 'w') as stdout, open(ferr, 'w') as stderr:
        p = subprocess.Popen(mkfcmd, stdout = stdout, stderr = stderr).wait()

if getcounts:
    # cellranger apparently does not have an argument to specify
    # the output directory so we only check for the existence of
    # directory for the log files
    if not os.path.exists(logdir):
        os.mkdir(logdir)

    cntcmd = [cranger, 'count',
              '--transcriptome='+refdir,
              '--fastqs='       + fastqdir,
              '--expect-cells=' +str(ncells),
              '--localcores='   +str(ccores)]

    my10Xsample = functools.partial(_my10Xsample, cmdlist=cntcmd,
                                    logdir=logdir, showcmd = showcmd)
    
    
    pools=multiprocessing.Pool(processes = cjobs)
    out = pools.map(my10Xsample, mysampids)
    pools.close()
