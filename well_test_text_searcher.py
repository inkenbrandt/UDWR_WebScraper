# -*- coding: utf-8 -*-
"""
Created on Wed Sep 03 12:46:50 2014

@author: paulinkenbrandt
"""

import pandas as pd
import os
import re
import glob

filepath = 'C:\\PROJECTS\\WR_DATA\\*.txt'
testpath = 'C:\\PROJECTS\\WR_DATA\\welltest\\'



for f in glob.glob(filepath): 
    win = []
    win.append(int(os.path.split(f)[1][3:8]))   
    text = open(f).read()    
    
    
# Well Tests ------------------------------------------------------------------------------

    welltest = []    
    welltest.append(text[text.find('WELL TESTS:'):text.find('\r\n\r\n\r\n ',text.find('WELL TESTS:'))])
    

    rev = []
    win1 = []

    #print texty[0:3]
    for i in range(len(welltest)):
        if len(welltest[i]) > 10:    
            rev.append(str(re.sub('\r\n       +', '\n',welltest[i])))
            win1.append(str(win[i]))
        else:
            pass  

    for i in range(len(rev)):
        rev[i] = re.sub('\r\n','\n',rev[i])
        rev[i] = re.sub(',',';',rev[i])
        rev[i] = re.sub('  +',',',rev[i])
        rev[i] = re.sub('\n,','\n',rev[i])
        rev[i] = re.sub('\n\n','\n',rev[i])
        
    rv=[]
   
    for i in range(len(rev)):    
        rv.append(rev[i].split('\n'))
        for j in range(len(rv[i])):    
            if rv[i][j].count(',')==2:
                rv[i][j] = win1[i] + ',' + rv[i][j] + ', , ' 
            elif rv[i][j].count(',')==3: 
                rv[i][j]= win1[i] + ',' + rv[i][j] +  ', '
            elif rv[i][j].count(',')==1: 
                rv[i][j]= win1[i] + ',' + rv[i][j] +  ', , , '
            elif rv[i][j].count(',')==4: 
                rv[i][j]= win1[i] + ',' + rv[i][j]    
            elif rv[i][j].count(',')==0:
                rv[i][j]= win1[i] + ',' + rv[i][j] +  ', , , , '
        rev[i] = '\n'.join(rv[i])

    g=[]
    
    for i in range(len(rev)):
        g.append(testpath + 'test' + str(win1[i]).zfill(5) + '.csv')    
        b = open(g[i], 'w')
        b.write(rev[i])



fout=open(testpath+"out.csv","a")
# first file:

testcombpath = testpath+"*.csv"
for line in open(testpath + "test00001.csv"):
    fout.write(line)
# now the rest:    
for testfile in glob.glob(testcombpath):
    f = open(testfile)
    lines = f.readlines()[3:]    
    fout.write("\n")    
    for g in lines:
        fout.write(g)    
    f.close() # not really needed
fout.close()
