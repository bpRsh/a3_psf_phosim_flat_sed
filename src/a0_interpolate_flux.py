#!python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Jun 09, 2017 Fri
# Last update : 
"""This program does interpolatio to 1 Angstrom width to the input sed file.

:Inputs:
    1. original_seds/ssp_pf.cat
    2. original_seds/exp9_pf.cat

:Outputs:
    1. original_seds/ssp_pf_6gyr_interpolated.cat
    2. original_seds/ssp_pf_12gyr_interpolated.cat
    3. original_seds/exp9_pf_6gyr_interpolated.cat
    4. original_seds/exp9_pf_12gyr_interpolated.cat

 """



# Imports
import numpy as np
import scipy as sp
import scipy.interpolate
import time

def interpolate_flux(infile, lambda1,lambda2):
    """ Interpolate the sed file in step of 1 Angstrom. 
    
    
    .. note::
    
       output file name is created using input name.  
       
       e.g. ssp_pf.cat will be ssp_pf_6gyr_interpolated.cat
       
    """
    wave, flux6, flux12 = np.loadtxt(infile, skiprows=15, unpack=True,
                                   dtype='float', usecols=(0, 6, 12))
    #print('{} {} {}'.format('wave[0] = ', wave[0], ''))
    #print('{} {} {}'.format('flux[0] = ', flux[0], '\n'))

    # wavelength range to interpolate
    nums = int(lambda2 - lambda1) + 1
    waverange = np.linspace(lambda1, lambda2, num=nums, endpoint=True)
    #print('{} {} {}'.format('waverange :\n', waverange, ''))


    # interpolation
    #print('{} {} {}'.format('\nInterpolating flux from the file : ', infile, ' \n...'))
    iflux6  = sp.interpolate.interp1d(wave, flux6, kind='cubic')(waverange)
    iflux12 = sp.interpolate.interp1d(wave, flux12, kind='cubic')(waverange)


    # write to a file
    outfile6  = infile[:-4] + '_6gyr_interpolated.cat'
    outfile12 = infile[:-4] + '_12gyr_interpolated.cat'
    np.savetxt(outfile6, list(map(list, zip(*[waverange, iflux6]))),
               fmt=['%-13.1f','%.13e'], delimiter='\t', newline='\n')
    np.savetxt(outfile12, list(map(list, zip(*[waverange, iflux12]))),
               fmt=['%-13.1f','%.13e'], delimiter='\t', newline='\n')


    # output info
    print('\nInterpolating from %d to %d from file: %s' % (lambda1,lambda2,infile) )
    print('Writing interpolated file to:', outfile6, '\n')
    #print('{} {} {}'.format('\ninterpolation range :',  waverange, '\n'))
    #print('{} {} {}'.format('input file            : ', infile, ''))
    #print('{} {} {}'.format('output file           :',  outfile, ''))
    
def main():
    lambda1 = 1000
    lambda2 = 12000
    # read data from the file
    infileb  = 'original_seds/ssp_pf.cat'
    infiled  = 'original_seds/exp9_pf.cat'
    interpolate_flux(infileb, lambda1,lambda2)
    interpolate_flux(infiled, lambda1,lambda2)
    
    
##==============================================================================
## Main program
##==============================================================================
if __name__ == '__main__':

    # beginning time
    begin_time,begin_ctime = time.time(), time.ctime()

    # run main program
    main()

    # print the time taken
    end_time,end_ctime  = time.time(), time.ctime()
    seconds             = end_time - begin_time
    m, s                = divmod(seconds, 60)
    h, m                = divmod(m, 60)
    d, h                = divmod(h, 24)
    print("\n")
    print('Begin time: ', begin_ctime,'\nEnd   time: ', end_ctime,'\n' )
    print("Time taken: {0:.0f} days, {1:.0f} hours, \
          {2:.0f} minutes, {3:f} seconds.".format(d, h, m, s))

