import subprocess
import os
import yaml
import time
import pandas as pd
import multiprocessing
import functools


class ymlsettings():
    def __init__(self, settingfile):
        with open(settingfile, 'r') as stream:
            try:
                yml = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        self.makefastq = yml['makefastq']
        self.getcounts = yml['getcounts']
        self.showcmd   = yml['showcmd']
        self.cranger  = yml['cranger']
        self.bcl2fastq= yml['bcl2fastq']
        self.projid   = yml['projid']
        self.datadir  = yml['datadir']
        self.refdir   = yml['refdir']
        self.outdir   = yml['outdir']
        self.logdir   = yml['logdir']
        self.cjobs  = yml['cjobs']
        self.ccores = yml['ccores']
        self.fcores = yml['fcores']
        self.ncells = yml['ncells']
        self.sampleids = yml['sampleids']
        self.sampsheet = yml['sampsheet']
        self.sampskip  = yml['sampskip']
        self.sampidcol = yml['sampidcol']
        self.sampdelim = yml['sampdelim']
        
        print("These are the paths and versions of programs to be used: \n")
        if 'bcl2fastq' in os.environ.get('PATH'):
            subprocess.Popen(['bcl2fastq', '--version'])
        else:
            os.environ['PATH'] = os.environ.get('PATH') + ":" + self.bcl2fastq
            subprocess.Popen(['bcl2fastq', '--version'])
        subprocess.Popen([self.cranger, 'mkfastq', '--version'])
        
        if self.sampleids is None:
            # Read in sample ids from sample sheet
            sampdf = pd.read_csv(self.sampsheet, sep = ",", skiprows = self.sampskip)
            self.mysampids = list(sampdf[self.sampidcol])
        else:
            self.mysampids = sampleids

        print("These are the " + str(len(self.mysampids)) + " sample ids to be processed \n")
        print(self.mysampids)