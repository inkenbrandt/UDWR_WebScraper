# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 12:11:04 2014

@author: Paul
"""
from bs4 import BeautifulSoup
from urllib2 import urlopen
import urllib
import re
import pandas as pd
import lxml
from lxml import etree
from lxml import *
# use this image scraper from the location that 
#you want to save scraped images to

def make_soup(url):
    # opens webpage for use in BeautifulSoup    
    html = urlopen(url).read()
    return BeautifulSoup(html, "lxml")

def get_images(url):
    soup = make_soup(url)
    #this makes a list of bs4 element tags
    images = [img for img in soup.findAll('img')]
    print (str(len(images)) + "images found.")
    print 'Downloading images to current working directory.'
    #compile our unicode list of image links
    image_links = [each.get('src') for each in images]
    for each in image_links:
        filename=each.split('/')[-1]
        urllib.urlretrieve(each, filename)
    return image_links

#a standard call looks like this
#get_images('http://cpgeosystems.com/nam.html')
#sp=[]
#for i in range(498,502):
#    sp.append(make_soup('http://waterrights.utah.gov/cgi-bin/docview.exe?Folder=welllog'+str(i)))

# Water Rights win number to begin search
winbegin = 9001
space = 1000

while winbegin < space + 1:

    winend = winbegin + space
    soup = []
    winrev = []
    
    # opens waterrights webpage by win
    for i in range(winbegin,winend):
        try:
            soup.append(make_soup('http://waterrights.utah.gov/cgi-bin/docview.exe?Folder=welllog'+str(i)))
            winrev.append(str(i))
        except TypeError:        
            pass
    
    souplist = []
    winrev2 = []
    
    # finds printed well log in opened water rights webpage and adds them to the list souplist 
    for i in range(len(soup)):
        try:
            souplist.append(soup[i].find('a', href=re.compile('^http://waterrights.utah.gov/docSys/v907/.*'))['href'])
            winrev2.append(winrev[i])
        except TypeError:
            pass
    
    soupsite = []    
    souptext = []
    winreva  = []    
    
    
    for i in range(len(souplist)):
        try:
            soupsite.append(make_soup(souplist[i]))
            winreva.append(winrev2[i])
        except Warning:
            pass

    winrevb = []    
    
    for i in range(len(souplist)):
        try:
            souptext.append(soupsite[i].get_text())
            winrevb.append(winreva[i])
        except HTMLParser.HTMLParseError:
            pass
    texty = []
    
    for t in souptext:
        texty.append(t[t.find('LITHOLOGY:'):t.find('\r\n\r\n ',t.find('LITHOLOGY:'))])
    
    rev = []
    rv=[]
    winrev3 = []
    
    #print texty[0:3]
    for i in range(len(texty)):
        if len(texty[i]) > 10:    
            rev.append(str(re.sub('\r\n       +', ' ',texty[i])))
            winrev3.append(winrevb[i])
        else:
            pass  
    
    for i in range(len(rev)):
        rev[i] = re.sub('\r\n','\n',rev[i])
        rev[i] = re.sub(',',';',rev[i])
        rev[i] = re.sub('  +',',',rev[i])
        rev[i] = re.sub('\n,','\n',rev[i])
       
    for i in range(len(rev)):    
        rv.append(rev[i].split('\n'))
        for j in range(len(rv[i])):    
            if rv[i][j].count(',')==2:
                rv[i][j] = winrev3[i] + ',' + rv[i][j] + ', , ' 
            elif rv[i][j].count(',')==3: 
                rv[i][j]= winrev3[i] + ',' + rv[i][j] +  ', '
            elif rv[i][j].count(',')==1: 
                rv[i][j]= winrev3[i] + ',' + rv[i][j] +  ', , , '
            elif rv[i][j].count(',')==4: 
                rv[i][j]= winrev3[i] + ',' + rv[i][j]    
            elif rv[i][j].count(',')==0:
                rv[i][j]= winrev3[i] + ',' + rv[i][j] +  ', , , , '
        rev[i] = '\n'.join(rv[i])
    
    path = 'C:\\PROJECTS\\WR_DATA\\'
    
    g=[]
    
    for i in range(len(rev)):
        g.append(path + 'w' + str(winrev3[i]).zfill(5) + '.csv')    
        b = open(g[i], 'w')
        b.write(rev[i])
    
   
    df = []
    
    for i in range(len(g)):
        try:
            df.append(pd.io.parsers.read_table(g[i], index_col=None, sep=',', names=['win','from','to','lith','color','other'], skiprows=3, error_bad_lines=False))
        except pd.parser.CParserError:
            pass

        
    
    frame = df[0].append(df)
        
    frame.to_csv(path+'output'+str(winbegin)+'.csv')

    winbegin = winend