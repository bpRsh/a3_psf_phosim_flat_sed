#!python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 25, 2016
# Last update : Jul 19, 2017 Wed

"""This script will create instance catalogs for the phosim software.

:Depends:

  1. ~/phosim/phosim 
  2. narrowband_seds/*.sed

:Outputs: 

  instance_catalogs/narrowband*.icat
  
  instance_catalogs/broadband.icat

:Runtime:

  1 second

"""

# Imports
import shutil
import os
import sys

# Global Variables
# data is defined in the function.
outfolder = 'instance_catalogs'

def replace_outfolder(outfolder):
    if os.path.exists(outfolder):
        print('Replacing folder: ', outfolder)
        shutil.rmtree(outfolder)
    os.makedirs(outfolder)

def create_catalogs():

    r'''Create catalogs.
    
:Inputs:
 
  argument: a number for SIM_SEED

:Outputs:
 
  instance_catalogs/narrowband*.icat

.. note::

  1. This program creates instance catalogs with different SIM_SEED variables.
  2. sed path in instance catalogs is relative to phosim/data/SEDS/ directory
  
     phosim = /Users/poudel/phosim/phosim.py
     
     SEDs   = /Users/poudel/phosim/data/SEDs/mySEDs
     
     ../../../ is Home.
     


    '''

    data = """
Unrefracted_RA_deg 0
Unrefracted_Dec_deg 0
Unrefracted_Azimuth 0
Unrefracted_Altitude 89
Slalib_date 1994/7/19/0.298822999997
Opsim_rotskypos 0
Opsim_rottelpos 0
Opsim_moondec -90
Opsim_moonra 180
Opsim_expmjd 49552.3
Opsim_moonalt -90
Opsim_sunalt -90
Opsim_filter 2
Opsim_dist2moon 180.0
Opsim_moonphase 10.0
Opsim_obshistid 99999999
Opsim_rawseeing 0.65
SIM_SEED  1000
SIM_MINSOURCE 1
SIM_TELCONFIG 0
SIM_CAMCONFIG 1
SIM_VISTIME 300
SIM_NSNAP 1
"""


    # function begin
    print("Beginning: create instance catalogs\n")


    # clobber outfolder
    outfolder = 'instance_catalogs'
    replace_outfolder(outfolder)


    for i in range(21):
        outfile = outfolder + '/' + 'narrowband' + '{:d}.icat'.format(i)
        print('{} {} {}'.format('creating: ',outfile, ''))
        with open(outfile,'w') as fout:
            print('{} {} {}'.format('creating: ',outfile, ''))
            fout.write(data.lstrip())
            sed  = '../../../Research/psf_creation_phosim/scripts/narrowband_seds/' + 'narrowband' + '{:d}.sed'.format(i)
            line = 'object 0 0.0 0.0 24 ' + sed + \
                   ' 0 0 0 0 0 0 star none none' + '\n'

            fout.write(line)


    # for broadband.icat
    outfile = outfolder + '/' + 'broadband.icat'
    print('{} {} {}'.format('creating: ',outfile, ''))
    with open(outfile,'w') as fout:
        print('{} {} {}'.format('creating: ',outfile, ''))
        fout.write(data.lstrip())
        sed  = '../../../Research/psf_creation_phosim/scripts/narrowband_seds/' + 'broadband.sed'
        line = 'object 0 0.0 0.0 24 ' + sed + \
               ' 0 0 0 0 0 0 star none none' + '\n'

        fout.write(line)


    # end function
    print("Ending: create instance catalogs\n")

if __name__ == '__main__':
    create_catalogs()
    pass


