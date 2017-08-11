#!python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 25, 2016
""" This program will unzip zipped psfs created by PHOSIM.
 
:Inputs:
  phosim_output_zipped/narrowband*_out/zipped_psf

:Outputs: 
  phosim_output_unzipped/psf*.fits

:Runtime: 
  12 seconds
  

"""


# Imports
import gzip
import glob
import os
import time
import shutil

def unzip_psf():
    '''Unzip the input psfs.'''

    print('{} {} {}'.format('\nRunning a5_unzip_all_psf','', ''))

    # Clobber outdir
    outdir = 'phosim_output_unzipped'
    if os.path.exists(outdir):
        shutil.rmtree(outdir)

    os.makedirs(outdir)

    # Loop through psfs
    for i in range(21):

        # Input/output info
        indir = 'phosim_output_zipped' + r'/' + 'narrowband{:d}_out'.format(i)
        infile = indir + r'/' + r'lsst_e_99999999_f2_R22_S11_E000.fits.gz'
        outfile = outdir + r'/' + 'psf{:d}.fits'.format(i)
        print('{} {:d} {}'.format('\ncount  : ', i, ''))
        print('{} {} {}'.format('infile : ',infile, ''))
        print('{} {} {}'.format('outfile: ',outfile, ''))

        # Read zipdata
        with gzip.open(infile, 'rb') as inzip:
            zipdata = inzip.read()

        # Write zipdata to files
        with open(outfile, 'wb') as f:
            f.write(zipdata)

    # Also, unzip broadband
    # Input/output info
    indir = 'phosim_output_zipped' + r'/' + 'broadband_out'
    infile = indir + r'/' + r'lsst_e_99999999_f2_R22_S11_E000.fits.gz'
    outfile = outdir + r'/' + 'broadband.fits'
    print('{} {} {}'.format('infile : ',infile, ''))
    print('{} {} {}'.format('outfile: ',outfile, ''))

    # Read zipdata
    with gzip.open(infile, 'rb') as inzip:
        zipdata = inzip.read()

    # Write zipdata to files
    with open(outfile, 'wb') as f:
        f.write(zipdata)


    print('{} {} {}'.format('\nEnd of a5_unzip_all_psf','', ''))


if __name__ == '__main__':

        # beginning time
    program_begin_time = time.time()
    begin_ctime        = time.ctime()

    # run main
    unzip_psf()



    # print the time taken
    program_end_time = time.time()
    end_ctime        = time.ctime()
    seconds          = program_end_time - program_begin_time
    m, s             = divmod(seconds, 60)
    h, m             = divmod(m, 60)
    d, h             = divmod(h, 24)
    print('\nBegin time: ', begin_ctime)
    print('End   time: ', end_ctime,'\n')
    print("Time taken: {0:.0f} days, {1:.0f} hours, \
          {2:.0f} minutes, {3:f} seconds.".format(d, h, m, s))
