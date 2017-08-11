#!python
# -*- coding: utf-8 -*-
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Jul 18, 2016
# Last update :

# Inputs      : phosim_output_zipped/narrowbands_sum.fits
#               phosim_output_zipped/broadband_out/lsst_e_99999999_f2_R22_S11_E000.fits.gz
# Outputs     : phosim_output_zipped/difference.fits

# Info:
# 1. This program takes in two input fits file :
#       phosim_output_zipped/narrowbands_sum.fits, and, 
#       phosim_output_zipped/broadband_out/lsst_e_99999999_f2_R22_S11_E000.fits.gz, then
#       creates the difference of two as :
#       phosim_output_zipped/difference.fits
#
# Estimated time: 2 sec               


# Imports
from astropy.io import fits
import numpy as np
import subprocess
import time

def create_difference_fits():
    """ Create difference fits file from two fitsfiles. """

    # start time
    start_time = time.time()
    
    # get data shape from first input file
    infile1 = 'phosim_output_zipped/narrowbands_sum.fits'
    data1   = fits.getdata(infile1)
    shape1   = data1.shape
    print('{} {} {}'.format('Reading file: ', infile1, ''))
    print('{} {} {}'.format(r'shape[0] = ',shape1[0], ''))
    print('{} {} {}'.format(r'shape[1] = ',shape1[1], '\n'))
    
    # get data shape from first second file
    infile2 = 'phosim_output_zipped/broadband_out/' + r'lsst_e_99999999_f2_R22_S11_E000.fits.gz'
    data2   = fits.getdata(infile2)
    shape2  = data2.shape
    print('{} {} {}'.format('Reading file: ', infile2, ''))
    print('{} {} {}'.format(r'shape[0] = ',shape2[0], ''))
    print('{} {} {}'.format(r'shape[1] = ',shape2[1], '\n'))
    
    
    
    # output data
    outfile = r'phosim_output_zipped/difference.fits'
    dout = data1 - data2
    hdu  = fits.PrimaryHDU()
    hdu.data = dout
    hdu.writeto(outfile, clobber=True)
    
    #output info
    print('{} {} {}'.format('infile1     : ',infile1, ''))
    print('{} {} {}'.format('infile2     : ',infile2, ''))
    print('{} {} {}'.format('output file : ',outfile, ''))

if __name__ == '__main__':
    create_difference_fits()
