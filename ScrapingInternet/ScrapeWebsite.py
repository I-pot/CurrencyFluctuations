from cProfile import label
from inspect import stack
from xml.etree.ElementTree import PI
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from scipy.fft import fft, fftfreq
from scipy.optimize import curve_fit
from scipy.stats import norm
from os.path import exists

from urllib.request import urlopen
import re

#Get mathces for a given website
if(False):
    url = "https://www.timeanddate.com/sun/sweden/stockholm"
    
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    #Get all matches for the current month
    if(True):
        pattern = "<td class=\"c tr sep-l\".*?>.*?</td.*?>"
        match_results = re.findall(pattern, html, re.IGNORECASE)
        lengths = []
        for i in match_results:
            i = re.sub("<.*?>", "", i)
            lengths.append(i)
            #print(i)
        print("I scraped the website and discovered a length of",len(lengths)," With inputs ",lengths)

#Get matches for all months of Stockholm
if(False):
    lengths = []
    for i in range(1,13):
        url = "https://www.timeanddate.com/sun/sweden/stockholm?month="+str(i)+"&year=2023"

        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")

        pattern = "<td class=\"c tr sep-l\".*?>.*?</td.*?>"
        match_results = re.findall(pattern, html, re.IGNORECASE)
        for i in match_results:
            i = re.sub("<.*?>", "", i)
            lengths.append(i)
            #print(i)
    
    print("I scraped the website and discovered a length of",len(lengths))
    fd = open("Stockholm.dat", "w")
    fd.write("#The file contains the length of day in the format hh:mm:ss \n")
    for i in lengths:
        fd.write(i+"\n")

#Read Stockholm data
if(True):
    f=open("Stockholm.dat","r")
    lines=f.readlines()
    lengthInSeconds = []
    for x in lines:
        if not x.startswith('#'):
            lengthInSeconds.append(float(x.split(':')[0])*60*60+float(x.split(':')[1])*60+float(x.split(':')[2]))
    print("Average length of day in Stockholm is = ",np.average(lengthInSeconds)/(60*60))

#Get matches for all months of Kuopio
if(False):
    lengths = []
    for i in range(1,13):
        #https://www.timeanddate.com/sun/finland/kuopio?month=1&year=2023
        url = "https://www.timeanddate.com/sun/finland/kuopio?month="+str(i)+"&year=2023"

        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")

        pattern = "<td class=\"c tr sep-l\".*?>.*?</td.*?>"
        match_results = re.findall(pattern, html, re.IGNORECASE)
        for i in match_results:
            i = re.sub("<.*?>", "", i)
            lengths.append(i)
            #print(i)
    
    print("I scraped the website and discovered a length of",len(lengths))
    fd = open("Kuopio.dat", "w")
    fd.write("#The file contains the length of day in the format hh:mm:ss \n")
    for i in lengths:
        fd.write(i+"\n")

#Read Kuopio data
if(True):
    f=open("Kuopio.dat","r")
    lines=f.readlines()
    lengthInSeconds = []
    for x in lines:
        if not x.startswith('#'):
            lengthInSeconds.append(float(x.split(':')[0])*60*60+float(x.split(':')[1])*60+float(x.split(':')[2]))
    print("Average length of day in Kuopio is = ",np.average(lengthInSeconds)/(60*60))

#Get matches for all months of London
if(False):
    lengths = []
    for i in range(1,13):
        url = "https://www.timeanddate.com/sun/uk/london?month="+str(i)+"&year=2023"

        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")

        pattern = "<td class=\"c tr sep-l\".*?>.*?</td.*?>"
        match_results = re.findall(pattern, html, re.IGNORECASE)
        for i in match_results:
            i = re.sub("<.*?>", "", i)
            lengths.append(i)
            #print(i)
    
    print("I scraped the website and discovered a length of",len(lengths))
    fd = open("London.dat", "w")
    fd.write("#The file contains the length of day in the format hh:mm:ss \n")
    for i in lengths:
        fd.write(i+"\n")
    fd.close()

#Read London data
if(True):
    f=open("London.dat","r")
    lines=f.readlines()
    lengthInSeconds = []
    for x in lines:
        if not x.startswith('#'):
            lengthInSeconds.append(float(x.split(':')[0])*60*60+float(x.split(':')[1])*60+float(x.split(':')[2]))
    print("Average length of day in London is = ",np.average(lengthInSeconds)/(60*60))

