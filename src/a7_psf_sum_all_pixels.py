#!python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Aug 09, 2016
# Last update : 
""" This program will get the sum of all the pixels in a fitsfile.

:Runtime:
  1 minute 30 sec 
  
"""



# Imports
from astropy.io import fits
import numpy as np
import time



def psf_sum_of_all_pixels(indir):
    '''This program will print out sum of all the pixels in a given fitsfile.'''


    for i in range(21):
        
        infile = indir + '/psf{}.fits'.format(i)
        data   = fits.getdata(infile)
        shape  = data.shape
    
        rows = data.shape[0]
        total = 0.0
        for i in range(rows):
            total += sum(data[i])
        print('{} {} {}'.format(infile,' sum_of_all_pixels = ',total))



if __name__ == '__main__':

    # beginning time
    begin_time,begin_ctime = time.time(), time.ctime()

    # run main program
    psf_sum_of_all_pixels('phosim_output_unzipped')
    psf_sum_of_all_pixels('phosim_normalized_psf')

    # print the time taken
    end_time,end_ctime  = time.time(), time.ctime()
    seconds             = end_time - begin_time
    m, s                = divmod(seconds, 60)
    h, m                = divmod(m, 60)
    d, h                = divmod(h, 24)
    print('\nBegin time: ', begin_ctime,'\nEnd   time: ', end_ctime,'\n' )
    print("Time taken: {0:.0f} days, {1:.0f} hours, \
          {2:.0f} minutes, {3:f} seconds.".format(d, h, m, s))
