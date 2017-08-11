#!python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Jul 18, 2016
# Last update : Sep 13, 2016
""" This program sums up 21 narrowband psf and create narrownbands_sum.fits. 

:Inputs:

  1. phosim_output_zipped/narrowband*_out/lsst_e_99999999_f2_R22_S11_E000.fits.gz
  
:Outputs:
  phosim_output_zipped/narrowbands_sum.fits

:Runtime: 
  25 sec  

             
"""
 

# Imports
from astropy.io import fits
import numpy as np
import subprocess
import time



def sum_narrowbands():
    """ This program sums up the given fitsfiles and write new fitsfile. """

    # Get data shape from first input file
    infile1 = 'phosim_output_zipped/narrowband0_out/lsst_e_99999999_f2_R22_S11_E000.fits.gz'
    
    print('{} {} {}'.format('Reading data from: ',infile1, '\n'))
    data1   = fits.getdata(infile1)
    shape1   = data1.shape
    print('{} {} {}'.format(r'shape[0] = ',shape1[0], ''))
    print('{} {} {}'.format(r'shape[1] = ',shape1[1], '\n'))
    dout = np.zeros((shape1[0],shape1[1]))
    
    
    # Input filenames
    infiles = []
    nfiles = 20
    for i in range(nfiles):
        tmp = 'phosim_output_zipped/' + 'narrowband{:d}_out/'.format(i) + 'lsst_e_99999999_f2_R22_S11_E000.fits.gz'
        infiles.append(tmp)
        #print(tmp)
    
    for i in range(nfiles):
        infile   = infiles[i]
        data     = fits.getdata(infile)
        dout     = dout + data
        hdu      = fits.PrimaryHDU()
        hdu.data = dout    
        print('{} {} {}{}'.format('shape of ',infile, ' = ', data.shape))
    
        # Write output if shapes are same
        if (shape1 == data.shape):
            hdu.writeto('phosim_output_zipped/narrowbands_sum.fits', clobber=True)
        else:
            exit
    
    #Output info
    print('{} {} {}'.format('\noutput file: ', 'phosim_output_zipped/narrowbands_sum.fits  ', ''))


if __name__ == '__main__':
    sum_narrowbands()
