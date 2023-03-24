import cv2
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

i = misc.ascent()

#Take a look at the image i
if(False):
    plt.grid(False)
    plt.gray()
    plt.axis('off')
    plt.imshow(i)
    plt.show()

i_transformed = np.copy(i)
size_x = i_transformed.shape[0]
size_y = i_transformed.shape[1]

# This filter detects edges nicely
# It creates a filter that only passes through sharp edges and straight lines. 
# Experiment with different values for fun effects.
#filter = [ [0, 1, 0], [1, -4, 1], [0, 1, 0]] 
# A couple more filters to try for fun!
filter = [ [-1, -2, -1], [0, 0, 0], [1, 2, 1]]
#filter = [ [-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
# If all the digits in the filter don't add up to 0 or 1, you 
# should probably do a weight to get it to do so
# so, for example, if your weights are 1,1,1 1,2,1 1,1,1
# They add up to 10, so you would set a weight of .1 if you want to normalize them
weight  = 1

#Testing 3x3 filters
if(False):

    def apply3x3Filter(i_orig,i_transformed, filter, weight, size_x, size_y):
        """Applies the defined filter

        :param i_orig: The original np.array
        :param i_transformed: the np.array that we want to be transformed
        :param filter: the 3x3 filter which we want to apply
        :param weight: If digits in filter not 1 or 0, add a weight
        :param size_x: Size of the x-axis
        :param size_y: Size of the y-axis
        """

        for x in range(1,size_x-1):
          for y in range(1,size_y-1):
              output_pixel = 0.0
              output_pixel = output_pixel + (i_orig[x - 1, y-1] * filter[0][0])
              output_pixel = output_pixel + (i_orig[x, y-1] * filter[0][1])
              output_pixel = output_pixel + (i_orig[x + 1, y-1] * filter[0][2])
              output_pixel = output_pixel + (i_orig[x-1, y] * filter[1][0])
              output_pixel = output_pixel + (i_orig[x, y] * filter[1][1])
              output_pixel = output_pixel + (i_orig[x+1, y] * filter[1][2])
              output_pixel = output_pixel + (i_orig[x-1, y+1] * filter[2][0])
              output_pixel = output_pixel + (i_orig[x, y+1] * filter[2][1])
              output_pixel = output_pixel + (i_orig[x+1, y+1] * filter[2][2])
              output_pixel = output_pixel * weight
              if(output_pixel<0):
                output_pixel=0
              if(output_pixel>255):
                output_pixel=255
              i_transformed[x, y] = output_pixel

    i_trans1 = np.copy(i)
    filter1 = [ [-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    apply3x3Filter(i,i_trans1,filter1,1,size_x,size_y)

    i_trans2 = np.copy(i)
    filter2 = [ [0, 1, 0], [1, -4, 1], [0, 1, 0]] 
    apply3x3Filter(i,i_trans2,filter2,1,size_x,size_y)

    i_trans3 = np.copy(i)
    filter3 = [ [-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    apply3x3Filter(i,i_trans3,filter3,1,size_x,size_y)

    i_trans4 = np.copy(i)
    #filter4 = [ [1, 1, 1], [1, 2, 1], [1, 1, 1]]#If notmalization not 0.1, then picture oversaturated
    filter4 = [ [100, 100, 100], [-100, -100, -100], [1, 0, 0]]
    apply3x3Filter(i,i_trans4,filter4,0.1,size_x,size_y)

    # Plot the image. Note the size of the axes -- they are 512 by 512
    fig, ((ax1, ax2),(ax3,ax4)) = plt.subplots(2, 2, figsize=(13.2, 7.05) )
    #plt.gray()
    plt.grid(False)
    ax1.imshow(i)#Original
    ax2.imshow(i_trans1)
    ax3.imshow(i_trans2)
    ax4.imshow(i_trans4)
    #plt.axis('off')
    plt.show()   

#Testing 5x5 filters
if(False):

    def apply5x5Filter(i_orig,i_transformed, filter, weight, size_x, size_y):
        """Applies the defined filter

        :param i_orig: The original np.array
        :param i_transformed: the np.array that we want to be transformed
        :param filter: the 5x5 filter which we want to apply
        :param weight: If digits in filter not 1 or 0, add a weight
        :param size_x: Size of the x-axis
        :param size_y: Size of the y-axis
        """
        offset = 2
        for x in range(offset,size_x-offset):
          for y in range(offset,size_y-offset):
              output_pixel = 0.0
              for k in range(-2,3):
                output_pixel = output_pixel + (i_orig[x + k, y-2] * filter[0][2+k])

              for k in range(-2,3):
                output_pixel = output_pixel + (i_orig[x + k, y-1] * filter[1][2+k])

              for k in range(-2,3):
                output_pixel = output_pixel + (i_orig[x + k, y] * filter[2][2+k])

              for k in range(-2,3):
                output_pixel = output_pixel + (i_orig[x + k, y+1] * filter[3][2+k])

              for k in range(-2,3):
                output_pixel = output_pixel + (i_orig[x + k, y+2] * filter[4][2+k])

              output_pixel = output_pixel * weight

              if(output_pixel<0):
                output_pixel=0
              if(output_pixel>255):
                output_pixel=255
              i_transformed[x, y] = output_pixel

    i_trans1 = np.copy(i)
    size_x = i_trans1.shape[0]
    size_y = i_trans1.shape[1]

    filter1 = [ [-1, -3, -4, -3, -1], [-1,-3, -4, -3, -1], [0, 0, 0, 0, 0], [1, 3, 4, 3, 1], [1, 3, 4, 3, 1]]
    apply5x5Filter(i,i_trans1,filter1,1,size_x,size_y)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.2, 7.05) )
    plt.gray()
    plt.grid(False)
    ax1.imshow(i)#Original
    ax2.imshow(i_trans1)
    #plt.axis('off')
    plt.show()  

#Testing 7x7 filters
if(True):

    def apply7x7Filter(i_orig,i_transformed, filter, weight, size_x, size_y):
        """Applies the defined filter

        :param i_orig: The original np.array
        :param i_transformed: the np.array that we want to be transformed
        :param filter: the 7x7 filter which we want to apply
        :param weight: If digits in filter not 1 or 0, add a weight
        :param size_x: Size of the x-axis
        :param size_y: Size of the y-axis
        """
        offset = 3
        for x in range(offset,size_x-offset):
          for y in range(offset,size_y-offset):
              output_pixel = 0.0
              for m in range(-offset,offset+1):
                for k in range(-offset,offset+1):
                    output_pixel = output_pixel + (i_orig[x + k, y+m] * filter[2+m][2+k])#note k and m

              output_pixel = output_pixel * weight

              if(output_pixel<0):
                output_pixel=0
              if(output_pixel>255):
                output_pixel=255
              i_transformed[x, y] = output_pixel

    i_trans1 = np.copy(i)
    size_x = i_trans1.shape[0]
    size_y = i_trans1.shape[1]

    filter1 = [ [-1, -3, -4, -4, -4, -3, -1],
                [-1, -3, -4, -4, -4, -3, -1],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [1, 3, 4, 4, 4, 3, 1],
                [1, 3, 4, 4, 4, 3, 1]]

    apply7x7Filter(i,i_trans1,filter1,1,size_x,size_y)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.2, 7.05) )
    plt.gray()
    plt.grid(False)
    ax1.imshow(i)#Original
    ax2.imshow(i_trans1)
    #plt.axis('off')
    plt.show()  



