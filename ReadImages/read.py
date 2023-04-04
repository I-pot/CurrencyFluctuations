import matplotlib.pyplot as plt

from PIL import Image
from scipy import *
from pylab import *

im = array(Image.open('fig3.png')) #format = [height,width,channel]
#print(shape(im))
#for joku in im:
#    print(joku)

hh = im.shape[0]
ww = im.shape[1]
#print("hh = ",hh)#465
#print("ww = ",ww)#666

plt.imshow(im)
plt.show()
#print(im[100,0,:])
Col = array([255,0,0])
bnd = 30
print("Col-bnd = ",Col-bnd)
print("Col+bnd = ",Col+bnd)
print("im[1,0,:0] = ",im[1,0,:])
ymax_lin = log10(0.5)
ymin_lin = log10(2e-4)
yax = linspace(ymax_lin,ymin_lin,hh)
xax = linspace(1,14,ww)
#for i in range(hh):
#    for j in range(ww):
#        whatisThis = 255*(any(im[i,j,:]>Col+bnd) or any(im[i,j,:]<Col-bnd)) 
#        im[i,j,:] = whatisThis
#        # print(whatisThis)
#mapim = abs(im[:,:,0]/255-1).astype(bool)
#print(mapim)
#yval = array([average(yax[mapim[:,t]]) for t in range(ww)])
#yval = 10**yval