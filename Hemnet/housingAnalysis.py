import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import re
from urllib.request import Request, urlopen


def getHemnetSlutpris(nettisivu,Fnimi):
    """Return the matches
    
    :param url: The name of the website where we scrape data
    :param Fnimi: Name of the file which we will save to
    :return: Nothing
    """

    soldPrice = []
    
    req = Request(url=nettisivu, headers={'User-Agent': 'Mozilla/5.0'} )
    webpage = urlopen(req).read()
    
    html = webpage.decode("utf-8")
#<div class="sold-property-listing__subheading">Slutpris 3 050 000 kr </div>
#          <div class="sold-property-listing__price-change">+11 %          </div>
    pattern = "<div class=\"sold-property-listing__subheading\".*?>\n .*\n .*</div.*>"
    match_results = re.findall(pattern, html, re.IGNORECASE)
    for i in match_results:
        i = re.sub("<.*?>\n", "", i)
        i = re.sub(".*Slutpris ", "", i)
        i = re.sub("</div>", "", i)
        i = re.sub("\n", "", i)
        soldPrice.append(i)

    #print("I scraped the website and discovered a length of",len(soldPrice))
    fd = open(Fnimi, "w")
    fd.write("#The file contains the sold price in SEK of apartments on Kungsholmen \n")
    for i in soldPrice:
        fd.write(i+"\n")
    fd.close()    

def getHemnetPriceChange(nettisivu,Fnimi):
    """Return the matches
    
    :param url: The name of the website where we scrape data
    :param Fnimi: Name of the file which we will save to
    :return: Nothing
    """

    priceChange = []
    
    req = Request(url=nettisivu, headers={'User-Agent': 'Mozilla/5.0'} )
    webpage = urlopen(req).read()
    
    html = webpage.decode("utf-8")
#<div class="sold-property-listing__subheading">Slutpris 3 050 000 kr </div>
#          <div class="sold-property-listing__price-change">+11 %          </div>
    pattern = "<div class=\"sold-property-listing__price-change\".*?>\n .*\n .*</div.*>"
    match_results = re.findall(pattern, html, re.IGNORECASE)
    for i in match_results:
        i = re.sub("<.*?>\n", "", i)
        #i = re.sub(".*Slutpris ", "", i)
        i = re.sub("</div>", "", i)
        i = re.sub("\n", "", i)
        priceChange.append(i)

    print("I scraped the website and discovered a length of",len(priceChange))
    fd = open(Fnimi, "w")
    fd.write("#The file contains the sold price in SEK of apartments on Kungsholmen \n")
    for i in priceChange:
        fd.write(i+"\n")
    fd.close()    

def getHemnetSlutpris_Change(nettisivu,Fnimi):
    """Return the matches
    
    :param url: The name of the website where we scrape data
    :param Fnimi: Name of the file which we will save to
    :return: Nothing
    """

    #Where do we want to write
    fd = open(Fnimi, "w")
    fd.write("#The file contains the sold price (sp), percentage difference to asking price (%ac) and price per square meter (psm) in SEK of apartments on Kungsholmen \n")
    fd.write("# sp %ac  psm \n")
    
    #The website is protected.
    req = Request(url=nettisivu, headers={'User-Agent': 'Mozilla/5.0'} )
    webpage = urlopen(req).read()
    
    html = webpage.decode("utf-8")
    #The data which we want is in <div> units
    #<div class="sold-property-listing__subheading">Slutpris 3 050 000 kr </div>
    #<div class="sold-property-listing__price-change">+11 %          </div>
    
    #Tried the following
    #pattern = "<div class=\"sold-property-listing__subheading\".*?> .* <div class=\"sold-property-listing__price-change\".*?>"
    #pattern = '(sold-property-listing__subheading)(.+)((?:\n.+)+)(sold-property-listing__price-change)'
    
    #this seems to work the best
    pattern = 'sold-property-listing__price(.+)((?:\n.+)+)'
    #result = re.findall('(startText)(.+)((?:\n.+)+)(endText)',input)
    match_results = re.findall(pattern, html, re.M)
    indeksi = 0
    for i in match_results:
        jono = str(i[1])
        jono = re.sub("</div>", "", jono)
        jono = re.sub("<div.*>", "", jono)
        jono = re.sub("\n+", "", jono)
        jono = re.sub("\s+", "", jono)
        print(jono)
        if(indeksi%2 == 0):
            tulosS = re.findall("Slutpris.*",jono)
            fd.write(tulosS[0][8:-2:]+" ")
            #prices.append(tulosS[0][8:-2:]+" ") #Always start with Slutpris and end with kr
        if(indeksi%2 == 1):
            tulosS = re.findall(".*%",jono)
            increase = re.findall(".*%",jono)
            sqrmeter = re.findall("%.*",jono)
            if(len(tulosS) == 0):
                #prices.append("NaN"+" "+jono[:-5:]+"\n")
                temp = "NaN"+" "+jono[:-5:]+"\n"
                fd.write(temp)
            else:
                temp2 = increase[0][:-1:]+" "+sqrmeter[0][1:-5:]+"\n"
                fd.write(temp2)            
            
        indeksi += 1


#Get mathces from Hemnet website
if(False):
    url = 'https://www.hemnet.se/salda/bostader?location_ids%5B%5D=925968'
    
    #getHemnetSlutpris(url,"KungsholmenSold.dat")
    #getHemnetPriceChange(url,"KungsholmenChange.dat")
    getHemnetSlutpris_Change(url,"Kungsholmen.dat")
    
#Analyse the acquired data
if(True):
    data = np.genfromtxt("Kungsholmen.dat")
    avgChange = np.nanmean(data[::,1])
    #for i in data[::,1]:
    print(avgChange)
    
    #These two do not agree with each other. Need to match those that I have

