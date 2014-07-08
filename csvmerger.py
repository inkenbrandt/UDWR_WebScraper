# -*- coding: utf-8 -*-
"""
Created on Mon Jul 07 12:26:24 2014

@author: paulinkenbrandt
"""
from glob import glob

with open('ramDataFile.csv', 'a') as singleFile:
    for csvFile in glob('pump*.csv'):
        for line in open(csvFile, 'r'):
            singleFile.write(line)