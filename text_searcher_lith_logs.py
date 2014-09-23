# -*- coding: utf-8 -*-
"""
Created on Wed Sep 03 08:16:48 2014

@author: paulinkenbrandt
"""

import pandas as pd
import os
import re
import glob

filepath = 'C:\\PROJECTS\\WR_DATA\\*.txt'
lithpath = 'C:\\PROJECTS\\WR_DATA\\lith\\'


for f in glob.glob(filepath): 
    win = []
    win.append(int(os.path.split(f)[1][3:8]))   
    text = open(f).read()    
# Lith Logs ---------------------------------------------------------------------------------
    lithlog = []    
    lithlog.append(text[text.find('LITHOLOGY:'):text.find('\r\n\r\n ',text.find('LITHOLOGY:'))])

    rev = []
    win1 = []

    #print texty[0:3]
    for i in range(len(lithlog)):
        if len(lithlog[i]) > 10:    
            rev.append(str(re.sub('\r\n       +', ' ',lithlog[i])))
            win1.append(str(win[i]))
        else:
            pass  

    for i in range(len(rev)):
        rev[i] = re.sub('\r\n','\n',rev[i])
        rev[i] = re.sub(',',';',rev[i])
        rev[i] = re.sub('  +',',',rev[i])
        rev[i] = re.sub('\n,','\n',rev[i])
        
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
        g.append(lithpath + 'lith' + str(win1[i]).zfill(5) + '.csv')    
        b = open(g[i], 'w')
        b.write(rev[i])  
        
# Well Tests ------------------------------------------------------------------------------

    welltest = []    
    welltest.append(text[text.find('WELL TESTS:'):text.find('\r\n\r\n ',text.find('WELL TESTS:'))])
    
    print welltest

    rev = []
    win1 = []

    #print texty[0:3]
    for i in range(len(welltest)):
        if len(welltest[i]) > 10:    
            rev.append(str(re.sub('\r\n       +', ' ',welltest[i])))
            win1.append(str(win[i]))
        else:
            pass  

    for i in range(len(rev)):
        rev[i] = re.sub('\r\n','\n',rev[i])
        rev[i] = re.sub(',',';',rev[i])
        rev[i] = re.sub('  +',',',rev[i])
        rev[i] = re.sub('\n,','\n',rev[i])
        
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
        g.append(lithpath + 'lith' + str(win1[i]).zfill(5) + '.csv')    
        b = open(g[i], 'w')
        b.write(rev[i])



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
