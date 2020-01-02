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

for key, value in yml.items():
    print (key, value)

# Parse out YAML settings file
makefastq = yml['makefastq']
getcounts = yml['getcounts']
showcmd   = yml['showcmd']

cranger  = yml['cranger']
bcl2fastq= yml['bcl2fastq']

projid   = yml['projid']
datadir  = yml['datadir']
refdir   = yml['refdir']
outdir   = yml['outdir']
logdir   = yml['logdir']


cjobs  = yml['cjobs']
ccores = yml['ccores']
fcores = yml['fcores']
ncells = yml['ncells']

sampleids = yml['sampleids']
sampsheet = yml['sampsheet']
sampskip  = yml['sampskip']
sampidcol = yml['sampidcol']
sampdelim = yml['sampdelim']


# # Add bcl2fastq to UNIX PATH and print version
# os.environ['PATH'] = os.environ.get('PATH') + ":" + bcl2fastq
# print("Check bclfastq version")
# subprocess.Popen(['bcl2fastq', '--version'])

# print("Check cellranger version")
# subprocess.Popen([cranger, 'mkfastq', '--version'])



# if sampleids is None:
#     # Read in sample ids from sample sheet
#     sampdf = pd.read_csv(sampsheet, sep = ",", skiprows = sampskip)
#     mysampids = list(sampdf[sampidcol])
# else:
#     mysampids = sampleids

# print("These are the " + str(len(mysampids)) + " sample ids to be processed")
# print(mysampids)
