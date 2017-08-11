#!python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 20, 2016
# Last update : Jul 19, 2017 Wed
"""
:Depends: 
 
  * instance_catalogs/narrowband*.icat
  * narrowband_seds/narrowband*.sed
  * backgrounds/background1.bkg

:Outputs: 

  * phosim_output_zipped/narrowband*/17_zipped_psf_fitsfiles
           
:Runtime:
    Time taken: 2 days, 7 hours,           21 minutes, 32.907248 seconds.
    Machine   : Macos Mavericks pisces 8 GB RAM
    Exptime   : SIM_VISTIME 300
    SED       : original_seds/exp9_pf_12gyr_interpolated.cat and its childeren.

           
.. note::

    1. The program a1_create_background.py will create backgrounds/background1.bkg

    2. The program a2_create_seds.py will create narrowband_seds/narrowband*.sed and
    narrowband_seds/broadband.sed.

    3. The program a3_create_instance_catalogs.py will create instance_catalogs/narrowband*.icat and
    instance_catalogs/broadband.icat.

    4. We can change seed, magnitude , sed etc while creating instance catalogs.

    5. For 21 input instance catalogs this program will create 21 unzipped psfs.

    6. We need only electron image and for that we will use a5_unzip_all_psf.py.
    
       
.. warning::

   To run phosim, we should use python2 not the ananconda python3.
   `export PATH="/Library/Frameworks/Python.framework/Versions/2.7/bin:${PATH}"`
   

"""

# Imports
import subprocess  
import os     
import shutil 
import re
import sys
import time

def replace_outdir(outdir):
    """Replace a folder."""    
    if os.path.exists(outdir):
        print('Replacing folder: %s\n'%outdir)
        shutil.rmtree(outdir)
        os.makedirs(outdir)
    else:
        print('Making new folder: %s\n'%outdir)
        os.makedirs(outdir)

def run_phosim():
    '''Run the phosim program.

    '''
    
    # clobber output folder 
    output = 'phosim_output_zipped'
    if os.path.exists(output):
        shutil.rmtree(output)
    os.makedirs(output)

    # catalogs
    for i in range(21):
        
        subprogram = 'narrowband{:d}'.format(i)
        print('{} {} {}'.format('\n\n Begin running Phosim for catalog :',subprogram, '\n\n'))
    
    
        # create output dir
        outputdir1 = output + '/narrowband{:d}_out'.format(i)
        os.makedirs(outputdir1)
    
        # commands to run relative to phosim installation folder
        instance_catalog  = '/Users/poudel/Research/psf_creation_phosim/scripts/' + \
                            'instance_catalogs/' + \
                            'narrowband{:d}.icat'.format(i)
                  
        background        = '/Users/poudel/Research/psf_creation_phosim/scripts/' +\
                            'backgrounds/background1.bkg'
        
        outputdir2        = '/Users/poudel/Research/psf_creation_phosim/scripts/' + outputdir1
        
        commands = 'cd ~/phosim;' + \
                   ' ./phosim '   + instance_catalog + \
                   ' -c '         + background + \
                   ' -o '         + outputdir2
              
    
        # run the program
        subprocess.call(commands,shell=True)
        
        print('{} {} {}'.format('\n\n End running Phosim for catalog :',subprogram, '\n\n'))
        
 



def run_phosim_broadband():
    """ Run phosim for broadband sed. """
    print('{} {} {}'.format('\n\n Begin running Phosim for catalog :','broadband', '\n\n'))

    # output dir
    outputdir1         = 'phosim_output_zipped/broadband_out'
    replace_outdir(outputdir1)
    
    # phosim command arguments relative to phosim installtion directory
    instance_catalog  = '/Users/poudel/Research/psf_creation_phosim/scripts/instance_catalogs/broadband.icat'          
    background        = '/Users/poudel/Research/psf_creation_phosim/scripts/backgrounds/background1.bkg'
    outputdir2        = '/Users/poudel/Research/psf_creation_phosim/scripts/phosim_output_zipped/broadband_out'
    
    commands = r'cd ~/phosim;' + \
           r' ./phosim ' + instance_catalog + \
           r' -c '       + background + \
           r' -o '       + outputdir2
           
    subprocess.call(commands,shell=True)
    print('{} {} {}'.format('\n\n End running Phosim for catalog :','broadband', '\n\n'))


if __name__ == '__main__':


    # beginning time
    program_begin_time = time.time()
    begin_ctime        = time.ctime()
    
    run_phosim()
    run_phosim_broadband()


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
    
