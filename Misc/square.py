#==============================================
#Why is the uniform probability distribution from 0 to 4
#different from the probability distribution of square root of 0 to 16?
#Look below
#==============================================
import matplotlib.pyplot as plt
import numpy as np

a = np.random.beta(1,0.1)
b = np.random.rand(5)
c = np.random.uniform(0,4,1000)
print("Average of samples from [0,4] = ",np.average(c))
print("Average of square of samples = ",np.average(c*c))
d = np.random.uniform(0,16,1000)
print("=========================================================")
print("Average of samples from [0,16] = ",np.average(d))
print("Average of square root of samples = ",np.average(np.sqrt(d)))
print("2*sqrt(2) = ",2*np.sqrt(2))

if(True):
    bin_edges1 = np.linspace(0,4,5)
    counts1, bins1 = np.histogram(c, bins=bin_edges1,density=True)#density = False gives total number of hits
    counts1_1, bins1_1 = np.histogram(np.sqrt(d), bins=bin_edges1,density=True)#density = False gives total number of hits
    plt.figure(1)
    plt.hist(bins1[:-1], bins1, weights=counts1,alpha=0.5,label="[0,4]") 
    plt.hist(bins1_1[:-1], bins1_1, weights=counts1_1,alpha=0.5,label="sqrt([0,16])") 
    plt.legend()

    bin_edges2 = np.linspace(0,16,17)
    counts2, bins2 = np.histogram(c*c, bins=bin_edges2,density=True)
    counts3, bins3 = np.histogram(d, bins=bin_edges2,density=True)
    plt.figure(2)
    plt.hist(bins2[:-1], bins2, weights=counts2,alpha=0.5,label="[0,4]^2")
    plt.hist(bins3[:-1], bins3, weights=counts3,alpha=0.5,label="[0,16]")
    plt.legend()
    #print(bins2)
    #print(bins2[:-1])
    #print(counts2)
    #print(len(counts2))
    plt.show()
#
#bin_edges3 = np.linspace(0,16,17)
#counts4, bins4 = np.histogram(c*c, bins=bin_edges3)
#print(counts4)
#print(bins4)
#plt.figure(3)
#plt.hist(counts4)
#plt.show()
#Can also use plt.stairs to plot
#bin_edges = np.linspace(0,4,5)
#counts, bins = np.histogram(c, bins=bin_edges)
#plt.figure(1)
#plt.stairs(counts,bins)
