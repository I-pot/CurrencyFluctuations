import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import re
from urllib.request import urlopen

def printAvgDayInHours(city):
    """Print the average length of a day in a given city
    
    :param city: Name of the city to be printed
    :return: None. Prints Length of day in hours
    """

    f=open(city+".dat","r")
    lines=f.readlines()
    lengthInSeconds = []
    for x in lines:
        if not x.startswith('#'):
            lengthInSeconds.append(float(x.split(':')[0])*60*60+float(x.split(':')[1])*60+float(x.split(':')[2]))
    print("Average length of day in "+city+" is = ",np.average(lengthInSeconds)/(60*60)," h")

def getAvgDayInHours(city):
    """Return the average length of a day in a given city
    
    :param city: Name of the city to be printed
    :return: Length in hours
    """

    f=open(city+".dat","r")
    lines=f.readlines()
    lengthInSeconds = []
    for x in lines:
        if not x.startswith('#'):
            lengthInSeconds.append(float(x.split(':')[0])*60*60+float(x.split(':')[1])*60+float(x.split(':')[2]))
    return np.average(lengthInSeconds)/(60*60)

def getAvgDayInSeconds(city):
    """Return the average length of a day in a given city
    
    :param city: Name of the city to be printed
    :return: Length in seonds
    """
    
    f=open(city+".dat","r")
    lines=f.readlines()
    lengthInSeconds = []
    for x in lines:
        if not x.startswith('#'):
            lengthInSeconds.append(float(x.split(':')[0])*60*60+float(x.split(':')[1])*60+float(x.split(':')[2]))
    return np.average(lengthInSeconds)

def writeMathcesForMost(websiteBegin,Fnimi):
    """Return the average length of a day in a given city
    
    :param websiteBegin: The beginning of the website (timeanddate) from which we scrape info
    :param Fnimi: Name of the file which we will save to
    :return: Length in seonds
    """

    lengths = []
    for i in range(1,13):
        url = websiteBegin+str(i)+"&year=2023"

        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")

        pattern = "<td class=\"c tr sep-l\".*?>.*?</td.*?>"
        match_results = re.findall(pattern, html, re.IGNORECASE)
        for i in match_results:
            i = re.sub("<.*?>", "", i)
            lengths.append(i)
    
    print("I scraped the website and discovered a length of",len(lengths))
    fd = open(Fnimi, "w")
    fd.write("#The file contains the length of day in the format hh:mm:ss \n")
    for i in lengths:
        fd.write(i+"\n")
    fd.close()    

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
    fd.close()

#Read Stockholm data
if(True):
    printAvgDayInHours("Stockholm")

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
    fd.close()

#Read Kuopio data
if(False):
    printAvgDayInHours("Kuopio")

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
if(False):
    printAvgDayInHours("London")

#Ugly solution for Alert data acquisition
if(False):
    lengths = []
    for i in range(1,13):
        url = "https://www.timeanddate.com/sun/canada/alert?month="+str(i)+"&year=2023"
        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
    
        if(i<=3):
            pattern = "<td class=\"c tr sep-l\".*?>?:?</td.*?>"
            patt_res = re.findall(pattern, html, re.IGNORECASE)
            for k in patt_res:
               k = re.sub("<.*?>", "", k)
               if(k == ""):
                   lengths.append("00:00:00")
               elif(len(k.split(':'))==2):
                   lengths.append("00:"+k)
               else:
                   lengths.append(k)

        if(i==4):
            pattern = "<td class=\"c tr sep-l\".*?>?:?</td.*?>"
            patt_res = re.findall(pattern, html, re.IGNORECASE)
            ind = 1
            for k in patt_res:
                k = re.sub("<.*?>", "", k)
                if(k == "" and ind == 5):
                    lengths.append("23:43:00")
                elif(k == ""):
                     lengths.append("24:00:00")
                elif(len(k.split(':'))==2):
                    lengths.append("00:"+k)
                else:
                    lengths.append(k)
                ind += 1

        if(4<i<=8):
            patt = "Up all day"
            patt_res = re.findall(patt, html, re.IGNORECASE)
            for k in patt_res:
                lengths.append("24:00:00")

        if(i==9):
            pattern = "<td class=\"c tr sep-l\".*?>?:?</td.*?>"
            patt_res = re.findall(pattern, html, re.IGNORECASE)
            ind = 1
            for k in patt_res:
                k = re.sub("<.*?>", "", k)
                if(k == "" and ind == 5):
                    lengths.append("23:29:00")
                elif(k == ""):
                     lengths.append("24:00:00")
                elif(len(k.split(':'))==2):
                    lengths.append("00:"+k)
                else:
                    lengths.append(k)
                ind += 1

        if(9 < i):
            pattern = "<td class=\"c tr sep-l\".*?>?:?</td.*?>"
            patt_res = re.findall(pattern, html, re.IGNORECASE)
            for k in patt_res:
               k = re.sub("<.*?>", "", k)
               if(k == ""):
                   lengths.append("00:00:00")
               elif(len(k.split(':'))==2):
                   lengths.append("00:"+k)
               else:
                   lengths.append(k)
    
    print("I scraped the website and discovered a length of",len(lengths))
    fd = open("Alert.dat", "w")
    fd.write("#The file contains the length of day in the format hh:mm:ss \n")
    for i in lengths:
        fd.write(i+"\n")
    fd.close()

#Read Alert data
if(False):
    printAvgDayInHours("Alert")

#Get matches for all months of Madrid
if(False):
    writeMathcesForMost("https://www.timeanddate.com/sun/spain/madrid?month=","Madrid.dat")

#Read Madrid data
if(False):
    printAvgDayInHours("Madrid")

#Get matches for all months of Cairo
if(False):
    writeMathcesForMost("https://www.timeanddate.com/sun/egypt/cairo?month=","Cairo.dat")

#Read Madrid data
if(False):
    printAvgDayInHours("Cairo")

#Get matches for all months of Santo-Domingo
if(False):
    writeMathcesForMost("https://www.timeanddate.com/sun/dominican-republic/santo-domingo?month=","SantoDomingo.dat")

#Read SantoDomingo data
if(True):
    printAvgDayInHours("SantoDomingo")

#Get matches for all months of Macapa
if(False):
    writeMathcesForMost("https://www.timeanddate.com/sun/brazil/macapa?month=","Macapa.dat")

#Read Macapa data
if(True):
    printAvgDayInHours("Macapa")

#Get matches for all months of Kampala
if(False):
    writeMathcesForMost("https://www.timeanddate.com/sun/uganda/kampala?month=","Kampala.dat")

#Read Kampala data
if(True):
    printAvgDayInHours("Kampala")

#Get matches for all months of Guayaquil
if(False):
    writeMathcesForMost("https://www.timeanddate.com/sun/ecuador/guayaquil?month=","Guayaquil.dat")

#Read Guayaquil data
if(True):
    printAvgDayInHours("Guayaquil")

#Get matches for all months of Lima
if(False):
    writeMathcesForMost("https://www.timeanddate.com/sun/peru/lima?month=","Lima.dat")

#Read Lima data
if(True):
    printAvgDayInHours("Lima")

#Get matches for all months of Sydney
if(False):
    writeMathcesForMost("https://www.timeanddate.com/sun/australia/sydney?month=","Sydney.dat")

#Read Sydney data
if(True):
    printAvgDayInHours("Sydney")

#Get matches for all months of Ushuaia
if(False):
    writeMathcesForMost("https://www.timeanddate.com/sun/argentina/ushuaia?month=","Ushuaia.dat")

#Read Ushuaia data
if(True):
    printAvgDayInHours("Ushuaia")


#Lets plot the average length of day as a function of latitude, Coordinates from Google (N,E)
CitiesAndCoord = [["Stockholm",59.323915, 18.070143],["Kuopio",62.885520, 27.680612],["London",51.503348, -0.124266],["Alert",82.499210, -62.337774],["Madrid",40.402029, -3.699910],["Cairo",30.047894, 31.228080],["SantoDomingo",18.470545, -69.933857],["Macapa",0.028988, -51.057047],["Kampala",0.336717, 32.584338],["Guayaquil",-2.201898, -79.897028],["Lima",-12.070371, -77.023878],["Sydney",-33.870735, 151.157158],["Ushuaia",-54.819720, -68.322720]]


mpl.rcParams['xtick.major.size'] = 6
mpl.rcParams['xtick.major.width'] = 2
mpl.rcParams['xtick.minor.size'] = 4
mpl.rcParams['xtick.minor.width'] = 1

mpl.rcParams['ytick.major.size'] = 6
mpl.rcParams['ytick.major.width'] = 2
mpl.rcParams['ytick.minor.size'] = 4
mpl.rcParams['ytick.minor.width'] = 1

font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 16}

mpl.rc('font', **font)

fig, ax1 = plt.subplots(1, 1, figsize=(13.2, 7.05) )#figsize=(10, 4), sharey = 'row'
plt.subplots_adjust(left=0.09, bottom=0.12, right=0.99, top=0.99, wspace = 0.188, hspace = 0.218)

fs = 30
akselit = [ax1]
for aks in akselit:
  aks.tick_params(which='minor',length=4)
  aks.xaxis.set_tick_params(which='both', labelbottom=True)
  aks.set_xlabel('N [deg]',fontsize=fs)
  aks.set_ylabel('Avg. Length of Day [h]',fontsize=fs)
  for axis in ['top','bottom','left','right']:
    aks.spines[axis].set_linewidth(2)

for city in CitiesAndCoord:
  ax1.plot(city[1], getAvgDayInHours(city[0]), marker='x',  linestyle='None', mew=3, ms='12', label=str(city[0]))

plt.legend()


fig2, ax2 = plt.subplots(1, 1, figsize=(13.2, 7.05) )#figsize=(10, 4), sharey = 'row'
plt.subplots_adjust(left=0.09, bottom=0.12, right=0.99, top=0.99, wspace = 0.188, hspace = 0.218)

fs = 30
akselit = [ax2]
for aks in akselit:
  aks.tick_params(which='minor',length=4)
  aks.xaxis.set_tick_params(which='both', labelbottom=True)
  aks.set_xlabel('E [deg]',fontsize=fs)
  aks.set_ylabel('Avg. Length of Day [h]',fontsize=fs)
  for axis in ['top','bottom','left','right']:
    aks.spines[axis].set_linewidth(2)

for city in CitiesAndCoord:
  ax2.plot(city[2], getAvgDayInHours(city[0]), marker='x',  linestyle='None', mew=3, ms='12', label=str(city[0]))

plt.legend()
plt.show()  
