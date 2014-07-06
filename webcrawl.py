# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 12:11:04 2014

@author: Paul
"""
from bs4 import BeautifulSoup
from urllib2 import urlopen
import urllib
import re



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

soup = make_soup('http://waterrights.utah.gov/cgi-bin/docview.exe?Folder=welllog'+str(500))
lstsoup = sp.findAll("a")

print soup.find('a', href=re.compile('^http://waterrights.utah.gov/docSys/v907/.*'))['href']


