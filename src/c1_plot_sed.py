#!python
# -*- coding: utf-8 -*-
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Jun 24, 2016
# Last update : Aug 09, 2016

""" This program plots the given input sed file. 

:Inputs: 
  a sed file (zipped or non_zipped)
  
  e.g.  original_seds/sed_flat.txt
  
:Outputs: 
  input.png
   
  e.g. original_seds/sed_flat.png
  
"""
      
 

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_sed():
    """ Plot the sed file. """
    # input/output
    #infile = 'sed_flat.txt'
    infile = 'original_seds/exp9_pf.cat'
    outimage = infile[0:-4] + '_6gyr'+ '.png'
    
    # read in a file
    infile = infile
    colnames = ['c0', 'c1']
    print('{} {} {} {}'.format('\nreading file : ', infile, '','' ))
    df = pd.read_csv(infile,sep='\s+', header = None,skiprows = 0,
                     comment='#',names=colnames,usecols=(0,5))
    
    print(df.head())
    print("\n")
    
    
    ## plot wave vs trans
    plt.plot(df.c0,df.c1,linewidth=1,color='b')
    
    # title and axes labels
    plt.title(outimage)
    plt.xlabel('Wavelength (Angstrom) ', fontsize=14)
    plt.ylabel(r'Flux ', fontsize=14)
    
    
    
    # axes limit
    # uncomment for broadband.sed
    # comment for sed_flat.txt
    #plt.xlim(500,700)
    #plt.ylim(1e-12,7e-12)
    
    # grid
    plt.grid(True)
    plt.tight_layout()
    
    ## save figure
    outimage = outimage
    print('{} {}'.format('\noutput image = ',outimage ))
    plt.savefig(outimage)
    plt.show()

if __name__ == '__main__':
    plot_sed()
