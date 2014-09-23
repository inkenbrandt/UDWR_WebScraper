# -*- coding: utf-8 -*-
"""
Created on Wed Sep 03 06:32:38 2014

@author: paulinkenbrandt
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 12:11:04 2014

@author: Paul
"""
from bs4 import BeautifulSoup
from urllib2 import urlopen
import re
import HTMLParser

# use this image scraper from the location that 
#you want to save scraped images to

def make_soup(url):
    # opens webpage for use in BeautifulSoup    
    html = urlopen(url).read()
    return BeautifulSoup(html, "lxml")


# Water Rights win number to begin search
winbegin = 0
space = 100
path = 'C:\\PROJECTS\\WR_DATA\\'

winend = winbegin + space
  
while winbegin < 60000:
         
    soup = []
    win = []
       
    # opens waterrights webpage by win   
    for i in range(winbegin,winend):
        try:
            soup.append(make_soup('http://waterrights.utah.gov/cgi-bin/docview.exe?Folder=welllog'+str(i)))
            win.append(str(i))
        except TypeError:        
            pass
    
        souplist = []
        win1 = []
        
    # finds printed well log in opened water rights webpage and adds them to the list souplist 
    for j in range(len(soup)):
        try:
            souplist.append(soup[j].find('a', href=re.compile('^http://waterrights.utah.gov/docSys/v907/.*'))['href'])
            win1.append(win[j])
        except TypeError:
            pass
    
    soupsite = []    
    souptext = []
    win  = []    
    
    for j in range(len(souplist)):
        try:
            soupsite.append(make_soup(souplist[j]))
            win.append(win1[j])
        except Warning:
            pass
    
    win1 = []    
    
    for j in range(len(souplist)):
        try:
            souptext.append(soupsite[j].get_text())
            win1.append(win[j])
        except HTMLParser.HTMLParseError:
            pass
    
    g=[]
    
    for j in range(len(souptext)):
        g.append(path + 'log' + str(win1[j]).zfill(5) + '.txt')    
        b = open(g[j], 'w')
        b.write(souptext[j])

    winbegin = winend
    winend = winbegin + space