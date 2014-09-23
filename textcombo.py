# -*- coding: utf-8 -*-
"""
Created on Wed Sep 03 10:11:48 2014

@author: paulinkenbrandt
"""

import glob

lithpath = 'C:\\PROJECTS\\WR_DATA\\lith\\'

fout=open(lithpath+"out.csv","a")
# first file:

lithcombpath = lithpath+"*.csv"
for line in open(lithpath + "lith00001.csv"):
    fout.write(line)
# now the rest:    
for lithfile in glob.glob(lithcombpath):
    f = open(lithfile)
    lines = f.readlines()[3:]    
    fout.write("\n")    
    for g in lines:
        fout.write(g)    
    f.close() # not really needed
fout.close()