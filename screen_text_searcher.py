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
scrnpath = 'C:\\PROJECTS\\WR_DATA\\screens\\'



for f in glob.glob(filepath): 
    win = []
    win.append(int(os.path.split(f)[1][3:8]))   
    text = open(f).read()    
    
    
# Well Tests ------------------------------------------------------------------------------

    welltest = []    
    welltest.append(text[text.find('SCREENS/PERFORATIONS:'):text.find('\r\n\r\n',text.find('SCREENS/PERFORATIONS:'))])
    

    rev = []
    win1 = []

    #print texty[0:3]
    for i in range(len(welltest)):
        if len(welltest[i]) > 10:    
            rev.append(str(re.sub('\r\n      +', '\n',welltest[i])))
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
                rv[i][j] = win1[i] + ',' + rv[i][j] + ', , , ' 
            elif rv[i][j].count(',')==3: 
                rv[i][j]= win1[i] + ',' + rv[i][j] +  ', , '
            elif rv[i][j].count(',')==1: 
                rv[i][j]= win1[i] + ',' + rv[i][j] +  ', , , , '
            elif rv[i][j].count(',')==4: 
                rv[i][j]= win1[i] + ',' + rv[i][j] +  ', '
            elif rv[i][j].count(',')==0:
                rv[i][j]= win1[i] + ',' + rv[i][j] +  ', , , , , '
            elif rv[i][j].count(',')==5: 
                rv[i][j]= win1[i] + ',' + rv[i][j]
        rev[i] = '\n'.join(rv[i])

    g=[]
    
    for i in range(len(rev)):
        g.append(scrnpath + 'scrn' + str(win1[i]).zfill(5) + '.csv')    
        b = open(g[i], 'w')
        b.write(rev[i])



fout=open(scrnpath+"out.csv","a")
# first file:

testcombpath = scrnpath+"*.csv"
for line in open(scrnpath + "scrn00003.csv"):
    fout.write(line)
# now the rest:    
for scrnfile in glob.glob(testcombpath):
    f = open(scrnfile)
    lines = f.readlines()[3:]    
    fout.write("\n")    
    for g in lines:
        fout.write(g)    
    f.close() # not really needed
fout.close()
