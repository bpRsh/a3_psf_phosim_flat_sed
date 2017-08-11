#!python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Sep 07, 2016
# Last update : Jul 17, 2017 Mon
""" This script creates the background file for the phosim software.

:Depends:
    ~/phosim/phosim
    
:Inputs:
    None
    
:Outputs:
    backgrounds/background1.bkg
    
    
"""


# Imports
import shutil
import os
import sys

# Global Variables
# data is defined in the function.
outfolder = 'backgrounds'


def replace_outfolder(outfolder):
    if os.path.exists(outfolder):
        print('Replacing folder: ', outfolder)
        shutil.rmtree(outfolder)
    os.makedirs(outfolder)

def create_background():

    '''This program creates background file for the phosim.'''


    data = """
zenith_v 1000.0
raydensity 0.0
pixelsize 1.5
saturation 0
blooming 0
chargesharing 0
"""


    # function begin
    print("Beginning: create background file\n")


    # replace outfolder
    outfolder = 'backgrounds'
    replace_outfolder(outfolder)



    outfile = outfolder + '/' + 'background1.bkg'
    print('{} {} {}'.format('creating: ',outfile, ''))
    with open(outfile,'w') as fout:
        fout.write(data.lstrip())

    # end function
    print("Ending: create background\n")

if __name__ == '__main__':
    create_background()


