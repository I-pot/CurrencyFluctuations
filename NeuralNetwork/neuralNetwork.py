#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Written by Topi Löytäinen
#Based on the article: https://towardsdatascience.com/how-to-build-your-own-neural-network-from-scratch-in-python-68998a08e4f6
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from pylab import *
import sys
import logisticFunctions as lf

from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,ScalarFormatter,FuncFormatter,
                               AutoMinorLocator,SymmetricalLogLocator) #AutoMinorLocator requires linear scale

#One layer neural network
class NeuralNetwork0:
    def __init__(self, x, y):
        self.input      = x
        self.weights1   = np.random.rand(self.input.shape[1],4)
        self.y          = y
        self.output     = np.zeros(y.shape)

    def feedforward(self): #Biases assumed zero here
        #print("sigmoidin input = ",np.dot(self.input, self.weights1))
        self.output = lf.sigmoid(np.dot(self.input, self.weights1))
        #return self.output #Maybe it is better not to return anything

    def backprop(self):#T stands for transpose
        d_weights1 = np.dot(self.input.T, (2*(self.y - self.output) * lf.sigmoid_derivative(self.output)))

        self.weights1 += d_weights1

    def train(self, x, y):
        self.feedforward()
        self.backprop()

#Two layer neural network
class NeuralNetwork:
    def __init__(self, x, y):
        self.input      = x
        self.weights1   = np.random.rand(self.input.shape[1],4)
        self.weights2   = np.random.rand(4,1)
        self.y          = y
        self.output     = np.zeros(y.shape)

    def feedforward(self): #Biases assumed zero here
        self.layer1 = lf.sigmoid(np.dot(self.input, self.weights1))
        self.output = lf.sigmoid(np.dot(self.layer1, self.weights2))
        #return self.output #Maybe it is better not to return anything

    def backprop(self):#T stands for transpose
        d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * lf.sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T, (np.dot(2*(self.y - self.output) * lf.sigmoid_derivative(self.output), self.weights2.T) * lf.sigmoid_derivative(self.layer1)))

        self.weights1 += d_weights1
        self.weights2 += d_weights2

    def train(self, x, y):
        self.feedforward()
        self.backprop()


class NeuralNetwork2:
    def __init__(self, x, y):
        self.input      = x
        self.weights1   = np.random.rand(self.input.shape[1],4)
        self.weights2   = np.random.rand(4,1)
        self.y          = y
        self.output     = np.zeros(y.shape)

    def feedforward(self): #Biases assumed zero here
        self.layer1 = np.tanh(np.dot(self.input, self.weights1))
        self.output = np.tanh(np.dot(self.layer1, self.weights2))
        #return self.output #Maybe it is better not to return anything

    def backprop(self):#T stands for transpose
        d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * lf.tanh_derivative(self.output)))
        d_weights1 = np.dot(self.input.T, (np.dot(2*(self.y - self.output) * lf.tanh_derivative(self.output), self.weights2.T) * lf.tanh_derivative(self.layer1)))

        self.weights1 += d_weights1
        self.weights2 += d_weights2

    def train(self, x, y):
        self.feedforward()
        self.backprop()




#==========================================
#Okay, testing complete. Use logistic function for currency fluctuations
#==========================================
if(False):
    Askeleet=[]
    Ennuste1=[]
    Havio1=[]
    #What we train with. Taken from sek.dat by hand
    x1=np.array(([10.7415,10.6788,10.6500,10.6280,10.5703],[10.6788,10.6500,10.6280,10.5703,10.5525],[10.6500,10.6280,10.5703,10.5525,10.5860],[10.6280,10.5703,10.5525,10.5860,10.6063]), dtype=float)
    #What we want
    y1=np.array(([10.7498],[10.7415],[10.6788],[10.6500]), dtype=float)

    #One layer network
    if(True):
        eka = NeuralNetwork0(x1,y1)
        #eka.feedforward()
        for i in range(3):
            print("========Askel = "+str(i)+" =============")
            print("Output ennen feedforward: ",eka.output)
            print("Kertoimet1 ennen feedforward: ",eka.weights1)
            eka.feedforward()
            print("Output jälkeen feedforward: ",eka.output)
            print("Kertoimet1 jälkeen feedforward: ",eka.weights1)
            eka.backprop()
            print("Output jälkeen backprop: ",eka.output)
            print("Kertoimet1 jälkeen backprop: ",eka.weights1)


    #Two layer network
    if(False):
        eka = NeuralNetwork(x1,x2)
        for i in range(3):
            print("========Askel = "+str(i)+" =============")
            print("Output ennen feedforward: ",eka.output)
            print("Kertoimet1 ennen feedforward: ",eka.weights1)
            print("Kertoimet2 ennen feedforward: ",eka.weights2)
            eka.feedforward()
            print("Output jälkeen feedforward: ",eka.output)
            print("Kertoimet1 jälkeen feedforward: ",eka.weights1)
            print("Kertoimet2 jälkeen feedforward: ",eka.weights2)
            eka.backprop()
            print("Output jälkeen backprop: ",eka.output)
            print("Kertoimet1 jälkeen backprop: ",eka.weights1)
            print("Kertoimet2 jälkeen backprop: ",eka.weights2)


    #Run training
    if(False):
        for i in range(100): # trains the eka 1,000 times
            Askeleet.append(i)
            for k in eka.output:#it is an array of arrays
                Ennuste1.append(k[0])
            Havio1.append(np.mean(np.square(y1 - eka.output)))
            eka.train(x1, y1)

    #Print coefficients
    if(False):
      fs = 16#Changes additional text and main legend
      font = {'family' : 'serif',
            'weight' : 'normal',
            'size'   : fs}#Changes axes label and extra legend

      #Plotting stuff#
      fig1 = plt.figure(1,figsize=(14.0, 8.0)) #figsize=(13.68, 9.74), figsize=(13.68, 12.74) works pretty nicely
      ax2 = fig1.add_subplot(111)
    
      #Adjusting axels
      akselit = [ax2]
      plt.title("")
      # change all spines
      for aks in akselit:
         aks.set_ylabel('Predicted $y_i$',fontsize=fs)
         aks.set_xlabel('Number of steps',fontsize=fs)
         #aks.tick_params(width=4)
         aks.xaxis.set_tick_params(which='both', labelbottom=True)
         aks.yaxis.set_tick_params(which='both', labelbottom=True)
         aks.xaxis.set_minor_locator(AutoMinorLocator())
         aks.yaxis.set_minor_locator(AutoMinorLocator())
         #aks.tick_params(which='minor',length=6 )
         for axis in ['top','bottom','left','right']:
            aks.spines[axis].set_linewidth(2)

      sask = 5
      plt.plot(Askeleet[::sask],Ennuste1[::4*sask],label='NN1 $y_0=0$',linewidth='2',marker='',markersize='8',fillstyle='none',linestyle='solid',color='red')
      plt.plot(Askeleet[::sask],Ennuste1[1::4*sask],label='NN1 $y_1=1$',linewidth='2',marker='',markersize='8',fillstyle='none',linestyle='dashed',color='green')
      plt.plot(Askeleet[::sask],Ennuste1[2::4*sask],label='NN1 $y_2=1$',linewidth='2',marker='',markersize='8',fillstyle='none',linestyle='dotted',color='green')
      plt.plot(Askeleet[::sask],Ennuste1[3::4*sask],label='NN1 $y_3=0$',linewidth='2',marker='',markersize='8',fillstyle='none',linestyle='dashdot',color='red')
        
      plt.legend(frameon=False,fontsize=fs)


    #Print Loss function
    if(False):
      fs = 16#Changes additional text and main legend
      font = {'family' : 'serif',
            'weight' : 'normal',
            'size'   : fs}#Changes axes label and extra legend

      #Plotting stuff#
      fig2 = plt.figure(2,figsize=(14.0, 8.0)) #figsize=(13.68, 9.74), figsize=(13.68, 12.74) works pretty nicely
      ax2 = fig2.add_subplot(111)
    
      #Adjusting axels
      akselit = [ax2]
      plt.title("")
      # change all spines
      for aks in akselit:
         aks.set_ylabel('Loss',fontsize=fs)
         aks.set_xlabel('Number of steps',fontsize=fs)
         #aks.tick_params(width=4)
         aks.xaxis.set_tick_params(which='both', labelbottom=True)
         aks.yaxis.set_tick_params(which='both', labelbottom=True)
         aks.xaxis.set_minor_locator(AutoMinorLocator())
         aks.yaxis.set_minor_locator(AutoMinorLocator())
         #aks.tick_params(which='minor',length=6 )
         for axis in ['top','bottom','left','right']:
            aks.spines[axis].set_linewidth(2)


      plt.plot(Askeleet[::5],Havio1[::5],label='NN1 $\\frac{1}{4}\\sum_{i=1}^4 (y_i-\\hat{y})^2$',linewidth='2',marker='',markersize='8',fillstyle='none',linestyle='solid',color='blue')
    
    
    
      plt.legend(frameon=False,fontsize=fs)
    
    plt.show()






#==========================================
#Initiating a testing Python class object
#==========================================

if(True):
    #What we train with
    #x=np.array(([0,0,1],[0,1,1],[1,0,1],[1,1,1]), dtype=float)
    #x=np.array(([0,0,1,0,0,0],[0,1,1,1,1,1],[1,0,1,0,1,0],[1,1,1,0,1,0]), dtype=float)
    x1=np.array(([0.5,0,1,0,0,0],[0,0.5,1,1,1,1],[1,0,0.5,0,1,0],[1,0.5,1,0,1,0]), dtype=float)
    x2=np.array(([0.5,0,1,0,0,0],[0,0.5,1,1,1,1],[1,0,0.5,0,1,0],[1,0.5,1,0,1,0]), dtype=float)
    #x=np.array(([0],[0],[1],[1]), dtype=float)
    #x=np.array(([1],[0],[0],[1]), dtype=float)
    #x=np.array(([0,0],[0,1],[1,1],[1,0]), dtype=float)
    #x=np.array(([1,1],[1,0],[0,0],[0,1]), dtype=float)

    #What we want
    y1=np.array(([0],[1],[1],[0]), dtype=float)
    y2=np.array(([0],[1],[1],[0]), dtype=float)
    Ennuste1 = []
    Havio1 = []
    Ennuste2 = []
    Havio2 = []

    Askeleet = []
    Iteraatiot=0
    if len(sys.argv) == 2:
        Iteraatiot = int(sys.argv[1])
    else:
        Iteraatiot = 1500

    eka = NeuralNetwork(x1,y1)
    toka = NeuralNetwork2(x2,y2)
    for i in range(Iteraatiot): # trains the NN 1,000 times
        Askeleet.append(i)
        #if i % 1000 ==0: 
        #    print ("for iteration # " + str(i) + "\n")
        #    print ("Input : \n" + str(x))
        #    print ("Actual Output: \n" + str(y))
        #    print ("Predicted Output: \n" + str(eka.output))
        #    print ("Loss: \n" + str(np.mean(np.square(y - eka.output)))) # mean sum squared loss
        #    print ("\n")

        for k in eka.output:#it is an array of arrays
            Ennuste1.append(k[0])
        Havio1.append(np.mean(np.square(y1 - eka.output)))
        eka.train(x1, y1)

        for m in toka.output:#it is an array of arrays
            Ennuste2.append(m[0])
        Havio2.append(np.mean(np.square(y2 - toka.output)))
        toka.train(x2, y2)


    #Print coefficients
    if(True):
      fs = 16#Changes additional text and main legend
      font = {'family' : 'serif',
            'weight' : 'normal',
            'size'   : fs}#Changes axes label and extra legend

      #Plotting stuff#
      fig1 = plt.figure(1,figsize=(14.0, 8.0)) #figsize=(13.68, 9.74), figsize=(13.68, 12.74) works pretty nicely
      ax2 = fig1.add_subplot(111)
    
      #Adjusting axels
      akselit = [ax2]
      plt.title("")
      # change all spines
      for aks in akselit:
         aks.set_ylabel('Predicted $y_i$',fontsize=fs)
         aks.set_xlabel('Number of steps',fontsize=fs)
         #aks.tick_params(width=4)
         aks.xaxis.set_tick_params(which='both', labelbottom=True)
         aks.yaxis.set_tick_params(which='both', labelbottom=True)
         aks.xaxis.set_minor_locator(AutoMinorLocator())
         aks.yaxis.set_minor_locator(AutoMinorLocator())
         #aks.tick_params(which='minor',length=6 )
         for axis in ['top','bottom','left','right']:
            aks.spines[axis].set_linewidth(2)

      sask = 5
      plt.plot(Askeleet[::sask],Ennuste1[::4*sask],label='NN1 $y_0=0$',linewidth='2',marker='',markersize='8',fillstyle='none',linestyle='solid',color='red')
      plt.plot(Askeleet[::sask],Ennuste1[1::4*sask],label='NN1 $y_1=1$',linewidth='2',marker='',markersize='8',fillstyle='none',linestyle='dashed',color='green')
      plt.plot(Askeleet[::sask],Ennuste1[2::4*sask],label='NN1 $y_2=1$',linewidth='2',marker='',markersize='8',fillstyle='none',linestyle='dotted',color='green')
      plt.plot(Askeleet[::sask],Ennuste1[3::4*sask],label='NN1 $y_3=0$',linewidth='2',marker='',markersize='8',fillstyle='none',linestyle='dashdot',color='red')
    
      #plt.plot(Askeleet[::sask],Ennuste2[::4*sask],label='NN2 $y_0=0$',linewidth='2',marker='',markersize='8',fillstyle='none',linestyle='solid',color='orange')
      #plt.plot(Askeleet[::sask],Ennuste2[1::4*sask],label='NN2 $y_1=1$',linewidth='2',marker='',markersize='8',fillstyle='none',linestyle='dashed',color='blue')
      #plt.plot(Askeleet[::sask],Ennuste2[2::4*sask],label='NN2 $y_2=1$',linewidth='2',marker='',markersize='8',fillstyle='none',linestyle='dotted',color='blue')
      #plt.plot(Askeleet[::sask],Ennuste2[3::4*sask],label='NN2 $y_3=0$',linewidth='2',marker='',markersize='8',fillstyle='none',linestyle='dashdot',color='orange')

    
    
      plt.legend(frameon=False,fontsize=fs)
    

    #Print Loss function
    if(True):
      fs = 16#Changes additional text and main legend
      font = {'family' : 'serif',
            'weight' : 'normal',
            'size'   : fs}#Changes axes label and extra legend

      #Plotting stuff#
      fig2 = plt.figure(2,figsize=(14.0, 8.0)) #figsize=(13.68, 9.74), figsize=(13.68, 12.74) works pretty nicely
      ax2 = fig2.add_subplot(111)
    
      #Adjusting axels
      akselit = [ax2]
      plt.title("")
      # change all spines
      for aks in akselit:
         aks.set_ylabel('Loss',fontsize=fs)
         aks.set_xlabel('Number of steps',fontsize=fs)
         #aks.tick_params(width=4)
         aks.xaxis.set_tick_params(which='both', labelbottom=True)
         aks.yaxis.set_tick_params(which='both', labelbottom=True)
         aks.xaxis.set_minor_locator(AutoMinorLocator())
         aks.yaxis.set_minor_locator(AutoMinorLocator())
         #aks.tick_params(which='minor',length=6 )
         for axis in ['top','bottom','left','right']:
            aks.spines[axis].set_linewidth(2)


      plt.plot(Askeleet[::5],Havio1[::5],label='NN1 $\\frac{1}{4}\\sum_{i=1}^4 (y_i-\\hat{y})^2$',linewidth='2',marker='',markersize='8',fillstyle='none',linestyle='solid',color='blue')
      plt.plot(Askeleet[::5],Havio2[::5],label='NN2 $\\frac{1}{4}\\sum_{i=1}^4 (y_i-\\hat{y})^2$',linewidth='2',marker='',markersize='8',fillstyle='none',linestyle='solid',color='red')
    
    
    
      plt.legend(frameon=False,fontsize=fs)
    
    plt.show()
