# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 12:11:04 2014

@author: Paul
"""
from bs4 import BeautifulSoup
from urllib2 import urlopen
import urllib
import re
from itertools import takewhile, chain
import pandas as pd


# use this image scraper from the location that 
#you want to save scraped images to

def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html)

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

win = range(1,50)
winbegin = 1 
winend = 50
soup = []

for i in range(winbegin,winend):
    try:
        soup.append(make_soup('http://waterrights.utah.gov/cgi-bin/docview.exe?Folder=welllog'+str(i)))
    except TypeError:        
        pass

souplist = []

for i in range(len(soup)):
    try:
        souplist.append(soup[i].find('a', href=re.compile('^http://waterrights.utah.gov/docSys/v907/.*'))['href'])
    except TypeError:
        pass
soupsite = []
litho = []

for site in souplist:
    soupsite.append(make_soup(site))
    
souptext = []
for i in range(len(soupsite)):
    souptext.append(soupsite[i].get_text())

texty = []

for t in souptext:
    texty.append(t[t.find('LITHOLOGY:'):t.find('\r\n\r\n ',t.find('LITHOLOGY:'))])
print texty[0:1]
rev = []
rv=[]
df =[]
#print texty[0:3]
for text in texty:
    rev.append(str(re.sub('\r\n       +', ' ',text)))
for i in range(len(rev)):    
    rev[i] = re.sub('\r\n','\n',rev[i])
    rev[i] = re.sub('  +','\t',rev[i])
    rev[i] = re.sub('\n\t','\n',rev[i])
    
for i in range(len(rev)):    
    rv.append(rev[i].split('\n'))
    for j in range(len(rv[i])):    
        if rv[i][j].count('\t')==3:
            rv[i][j] = rv[i][j]+'\t \t '
        elif rv[i][j].count('\t')==4: 
            rv[i][j]=rv[i][j] +  '\t '
    rev[i] = '\n'.join(rv[i])
print rev[1]
g=[]
for i in range(len(rev)):
    g.append('w'+ str(i))    
    b = open(g[i], 'w')
    b.write(rev[i])


for i in range(len(rev)):
    df.append(pd.read_table(g[i], sep='\t', skiprows=3))

print df[0]