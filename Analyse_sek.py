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

dates = []
curVal = []
lask = 0
eka = ""
vika = ""
#Open the data file in read mode, other modes w=write and a=append
file_exists = exists('sek.dat')
if(not file_exists):
    fd = open("sek.dat", "w")
    fd.write("#The file contains the daily Eur to Sek exchange rate since 1999 not including weekends and some holidays \n")
    fd.write("#Date ExchangeRate \n")
    with open('sek.xml','r') as f:
        for line in f:
            if line[0:4] == "<Obs":
                if lask == 0:
                    eka = line
                dates.append(line[18:28])
                fd.write(line[18:28]+" ")
                if line[41:42] == '1': #Values always between 7 and 12 so take double digit starting with 1 separately
                    curVal.append(float(line[41:48]))
                    fd.write(line[41:48]+"\n")
                else:
                    curVal.append(float(line[41:47]))
                    fd.write(line[41:47]+"\n")
                lask += 1

            if line[0:9] == "</Series>":
                vika = prevLine
            prevLine = line
else:
    #fd = open("sek.dat", "r")
    #data1 = np.genfromtxt('sek.dat', comments='#')
    f=open("sek.dat","r")
    lines=f.readlines()
    for x in lines:
        if not x.startswith('#'):
            dates.append(x.split(' ')[0])
            #lengthOf = len(x.split(' ')[1])]
            curVal.append(x.split(' ')[1][:-1])
    f.close()

curVal = [float(i) for i in curVal]
#print(y)


#Do you wanna see some plots?
if(False):
    lask = len(curVal)
    fig, ((ax1, ax2),(ax3, ax4)) = plt.subplots(2, 2, figsize=(20,40))
    plt.subplots_adjust(left=0.05, bottom=0.08, right=0.995, top=0.965, wspace=0.177, hspace=0.225)
    ax1.set_title('Value of Eur in Sek')
    daysRange = np.arange(1,lask+1)
    #print(type(curVal[0]))
    ax1.plot(daysRange,curVal)
    ax1.set_xlabel("Days since 04.09.1999")
    ax1.set_ylabel("Exchange rate")


    N = lask+1 #Number of sample point
    T = 1 #sample spacing, one value per day
    curValF = fft(curVal) #fast Fourier transform
    #print(curValF[0:2])
    #// denotes floor division
    xf = fftfreq(N, T)[:N//2] #array of length N containing sample frequencies of which we take 0 to N//2 elements, 

    ax2.set_title('Fourier transform of value fluctuations')
    ax2.plot(xf, 2.0/N * np.abs(curValF[0:N//2])) 
    ax2.set_xlabel("Positive frequencies")
    ax2.set_ylabel("")
    #ax2.set_xlim([1e-300,1e-1])
    #ax2.set_xscale('log')
    #plt.grid()

    def lineaariFitti(x,a,b):
        """A function call returning a linear function

        :param x: variable (double or array)
        :param a: slope (double)
        :param b: offset (double)
        :return: a*x+b
        """
        return a*x+b

    def siniFitti(x, a, b, c, d):
        """A function call returning a sine function

        :param x: variable (double or array)
        :param a: amplitude (double)
        :param b: phase offset (double)
        :param c: slope for x^2 term
        :param d: constant offset
        :return: a*sin(x-b) + c*x^2
        """
        return a * np.sin(x-b) + c * x + d

    poptL, _ = curve_fit(lineaariFitti, daysRange, curVal)
    poptS, _ = curve_fit(siniFitti, daysRange, curVal)
    a, b = poptL
    #print("Generating a linear fit to data")
    #print('y = %.5f * x + %.5f' % (a, b))

    ax3.set_title("Linear fit to data")
    ax3.plot(daysRange,lineaariFitti(daysRange,a,b),color='red')


    a, b, c, d = poptS
    print(poptL)
    print(poptS)
    #print("Generating a linear fit to data")
    #print('y = %.5f * sin(x + %.5f) ' % (a, b, c))

    ax4.set_title("Sine fit to data")
    ax4.plot(daysRange,siniFitti(daysRange,a,b,c,d),color='green')
    ax4.set_yscale('log')


    plt.show()

    #Testing Fourier transform
    if(False):
        N = 600
        # sample spacing
        T = 1.0 / 800.0
        x = np.linspace(0.0, N*T, N, endpoint=False)
        A=10
        B=20
        y = A*np.sin(50.0 * 2.0*np.pi*x) + B*np.sin(80.0 * 2.0*np.pi*x)
        yf = fft(y)
        xf = fftfreq(N, T)[:N//2]
        import matplotlib.pyplot as plt
        plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
        plt.grid()
        plt.show()

#Print info about the data
if(False):
    mu = np.average(curVal)
    sigma = np.std(curVal)
    print("Average of the exchage rate = ",mu)
    print("Standard deviation of exchange rate = ", sigma)
    print("Variance of exchange rate = ", np.var(curVal))
    print("25th percentile = ",np.percentile(curVal,25))
    print("50th percentile = ",np.percentile(curVal,50))
    print("75th percentile = ",np.percentile(curVal,75))
    #Wanna see what kind of a Gaussian distribution one would acquire with the given avg and std
    def gaussian(x, mu, sig):
        """Returns a gaussian
        
        :param x: variable
        :param mu: mean of the distribution
        :param sig: standard deviation of the distribution
        """
        return np.exp(-(1.0/2.0)*((x - mu)/sig)**2.0)/(np.sqrt(2.0*np.pi)*sig)

    plt.figure(1)
    alaraja = mu-4
    ylaraja = mu+4
    numOfBins = 100
    x = np.linspace(alaraja,ylaraja,1000)
    weights = np.ones_like(curVal)/float(len(curVal))
    #plt.hist(curVal, weights=weights,bins=1000)

    plt.hist(curVal,bins=1000)
    p = norm.pdf(x, mu, sigma)
    plt.plot(x, p, linewidth=2, color="blue", label="Valmis")
    plt.plot(x, gaussian(x,mu,sigma), linewidth=2, color="red", label="Oma")
    plt.ylabel("Probability")
    plt.xlabel("Exchange rate")
    plt.legend()
    plt.show()

    #plt.figure(2)
    #hist, bins = np.histogram(curVal, bins=1000, density=True)
    #widths = np.diff(bins)
    #plt.bar(bins[:-1], hist, widths)
    #plt.show()

#Testing binning of gaussian numbers
if(False):
    gaussian_numbers = np.random.normal(size=10000)
    print(gaussian_numbers)
    plt.hist(gaussian_numbers, bins=100, density=True)
    plt.title("Gaussian Histogram")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()

#Print out some info about the data
if(False):
    print("Data file contains Eur to Sek Currency values disregarding weekends")
    print("Amount of lines = ",lask)
    input("Press Enter to continue...")
    print("eka = ",eka)
    input("Press Enter to continue...")
    print("vika = ",vika)
    input("Pess Enter to continue...")
    print("Retrieved dates = ",dates)
    input("Press Enter to continue...")
    print("Retrived currency values = ",curVal)
    input("Press Enter to continue...")


