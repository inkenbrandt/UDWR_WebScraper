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
wldatapath = 'C:\\PROJECTS\\WR_DATA\\wldata\\'
revlist = []

for f in glob.glob(filepath): 
    win = []
    win.append(int(os.path.split(f)[1][3:8]))   
    text = open(f).read()    
# Lith Logs ---------------------------------------------------------------------------------
    wldata = []    
    wldata.append(text[text.find('WATER LEVEL DATA:'):text.find('\r\n\r\n ',text.find('WATER LEVEL DATA:'))])

    rev = []
    win1 = []

    #print texty[0:3]
    for i in range(len(wldata)):
        if len(wldata[i]) > 10:    
            rev.append(str(re.sub('\r\n    +', '\n',wldata[i])))
            win1.append(str(win[i]))
        else:
            pass  

    for i in range(len(rev)):
        rev[i] = re.sub('\r\n','\n',rev[i])
        rev[i] = re.sub(' +',',',rev[i])
        rev[i] = re.sub('\n,','\n',rev[i])
        rev[i] = re.sub('\n',',',rev[i])
        
    rv=[]
   
    for i in range(len(rev)):    
        rev[i] = win1[i]+','+rev[i]        
        rev[i] = rev[i].split(',')

   
    if len(rev) > 0:
        revlist = rev + revlist        

df = pd.DataFrame(revlist)

print df
df.to_clipboard() 
        
