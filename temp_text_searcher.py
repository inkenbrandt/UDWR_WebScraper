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
scrnpath = 'C:\\PROJECTS\\WR_DATA\\temp\\'


revlist = []

for f in glob.glob(filepath): 
    win = []
    win.append(int(os.path.split(f)[1][3:8]))   
    text = open(f).read()    
    
    
# Well Tests ------------------------------------------------------------------------------

    temp = []    
    temp.append(text[text.find('DRILLER:'):text.find('\r',text.find('DRILLER:'))])
    

    rev = []
    win1 = []

    #print texty[0:3]
    for i in range(len(temp)):
        if len(temp[i]) > 5:    
            rev.append(str(temp[i]))
            win1.append(str(win[i]))
        else:
            pass  

    for i in range(len(rev)):
        rev[i] = re.sub('  +',',',rev[i])
        rev[i] = re.sub(':',',',rev[i])
        rev[i] = win1[i]+','+rev[i]
        rev[i] = rev[i].split(',')
     

    if len(rev) > 0:
        revlist = rev + revlist        

df = pd.DataFrame(revlist)

print df
df.to_clipboard()

#    for i in range(len(rev)):
#        g.append(scrnpath + 'scrn' + str(win1[i]).zfill(5) + '.csv')    
#        b = open(g[i], 'w')
#        b.write(rev[i])
#
#    
#
#
#fout=open(scrnpath+"out.csv","a")
## first file:
#
#testcombpath = scrnpath+"*.csv"
#for line in open(scrnpath + "scrn00003.csv"):
#    fout.write(line)
## now the rest:    
#for scrnfile in glob.glob(testcombpath):
#    f = open(scrnfile)
#    lines = f.readlines()[3:]    
#    fout.write("\n")    
#    for g in lines:
#        fout.write(g)    
#    f.close() # not really needed
#fout.close()
