import subprocess
import os
import yaml
import time
import pandas as pd
import multiprocessing
import functools
from pythonmp_10X_settings import ymlsettings

yml = ymlsettings('settings.yml')

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

#Process BCL -> FASTQ
if yml.makefastq:
    # Check for log directories
    if not os.path.exists(yml.logdir):
        os.mkdir(yml.logdir)

    fcores = str(min(yml.fcores, len(yml.mysampids)))
    mkfcmd = [yml.cranger, 'mkfastq',
              '--id='         + yml.projid,
              '--qc',
              '--run='        + yml.datadir,
              '--output-dir=' + yml.outdir,
              '--samplesheet='+ yml.sampsheet,
              '--localcores=' + str(yml.fcores)]

    fout = os.path.join(yml.logdir, "mkfastq" + ".out")
    ferr = os.path.join(yml.logdir, "mkfastq" + ".err")

    if yml.showcmd:
        print(mkfcmd)
    
    with open(fout, 'w') as stdout, open(ferr, 'w') as stderr:
        p = subprocess.Popen(mkfcmd, stdout = stdout, stderr = stderr).wait()

if yml.getcounts:
    # cellranger apparently does not have an argument to specify
    # the output directory so we only check for the existence of
    # directory for the log files
    if not os.path.exists(yml.logdir):
        os.mkdir(yml.logdir)

    cntcmd = [yml.cranger, 'count',
              '--transcriptome='+yml.refdir,
              '--fastqs='       + yml.outdir,
              '--expect-cells=' +str(yml.ncells),
              '--localcores='   +str(yml.ccores)]

    my10Xsample = functools.partial(_my10Xsample, cmdlist=cntcmd,
                                    logdir=yml.logdir, showcmd = yml.showcmd)
    
    
    pools=multiprocessing.Pool(processes = yml.cjobs)
    out = pools.map(my10Xsample, yml.mysampids)
    pools.close()
