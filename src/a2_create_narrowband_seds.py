#!python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date      : Jun 22, 2016
# Last update: Jul 18, 2017 Tue

"""This program creates 21 narrowbands and one broadband seds.

:Inputs:
    original_seds/exp9_pf_12gyr_interpolated.cat

:Outputs: 
    narrowband_seds/broadband.sed
    
    narrowband_seds/narrowband*.sed
    
:Runtime: 
    15 sec

:Info:

  1. This program takes in ONE input_sed_file and creates TWENTY_ONE output_sed files.

  2. The input sed file has two columns: wavelength (nm) and flux (ergs/cm^2/s/nm)
      wavelength varies from 300 nm to 1200 nm.

  3. We can plot wavelength vs flux and see the sed, which looks like Capital PI.

  4. To create output_seds from this input_sed_file, we first decrease the
     flux at 500 nm wavelength by a factor of 100 so that when phosim software
     uses this flux to normalize all the values, it will have lesser impact.
     
     i.e. sed_flat.txt    : 500.000  3.97290e-12
     
     narrowband*.sed : 500.000  3.9728999999999995e-14
     
     broadband.sed   : 500.000  3.9728999999999995e-14
     
  5.  Now, for one narrowband we look at the LSST_RED_BAND_FILTER_FILE 
      there we see that the values of wavelength where transmission is 
      NOT <= 5% are 531-696 nm.

  6. So, we will take the wavelength range only between this range and set all
     the other wavelength fluxes to zero EXCEPT for 500 nm case.


:sed_info:

    sed file: original_seds/exp9_pf.cat
    
    column0 : wavelength (1000-12000 Angstron)
    
    column5 : flux for 6 Gyr old star.
    
    column11 : flux for 12 Gyr old star.
    
    
:filter_info:

    source_red_band_filter_lsst : phosim/data/lsst/filter_2.txt
    
    We take wavelength range such that transmission <= 5%,
    and we get 531 nm - 696 nm.
    
    We can plot sed_file and see the flat peak and negligible bottom fluxes.


"""

# Imports
import numpy as np
import os
import shutil
import time

# Global Variables
infile = r'original_seds/exp9_pf_6gyr_interpolated.cat'
lookup = '5000.0'
outfolder = 'narrowband_seds'

def replace_outdir(outdir):
    """Replace a folder."""   
    if os.path.exists(outdir):
        print('Replacing folder: %s\n'%outdir)
        shutil.rmtree(outdir)
        os.makedirs(outdir)
    else:
        print('Making new folder: %s\n'%outdir)
        os.makedirs(outdir)


def replace_line(infile, line_num, text):
    ''' This function replaces a given line number.
    
        :Usage: replace_line(infile, line_num, text)
    '''

    lines = open(infile, 'r').readlines()
    lines[line_num] = text
    lines[line_num] = lines[line_num].lstrip()
    out = open(infile, 'w')
    out.writelines(lines)
    out.close()


def get_data(infile):
    """Get data."""
    data = ''
    with open(infile, 'r') as f:
        data = f.readlines()
    #print('data[0] = \n', data[0])
    return data

def get_ncom_lines(data):
    """Get number of comment lines. """
    data = get_data(infile)
    ncom_lines = 0
    for line in data:
        if line.strip().startswith('#'):
            ncom_lines += 1
        else:
            break
    #print('{} {} {}'.format('No of comment_lines = ', ncom_lines, '\n\n'))
    return ncom_lines


def get_normalizing_line(infile, lookup,data):
    """Get normalizing line of 500 nm for phosim.
    
    :Example: 
      for exp9_pf_6gyr_interpolated.cat
      
      before: 5000.0 5.297875e-05

      after: 5000.0 5.297875e-07
    
    """
    data = get_data(infile)
    normalize_line = ''
    normalize_line_num = 0
    ncom_lines = get_ncom_lines(data)
    with open(infile) as f:
        for num, line in enumerate(f, 1):
            if lookup in line:
                normalize_line = line
                normalize_line_num = num - 1
                #print ('normalize line = ', line)
                #print ('normalize line num = ', num)

    print('{} {} {}'.format('normalize_line            : ', normalize_line, ''))
    print('{} {} {}'.format('normalize_line_num        : ', normalize_line_num, ''))
    print('{} {} {}'.format(r'data[normalize_line_num]  :', data[normalize_line_num], ''))

    ## decrease the flux of normalize line by a factor of 100
    wave = normalize_line.split()[0]
    flux = normalize_line.split()[1]
    print('{} {} {}'.format('wave = ', wave, ''))
    print('{} {} {}'.format('flux = ', flux, ''))

    fluxn = float(flux) / 100.0
    
    normalize_line = normalize_line.replace(str(flux), str(fluxn))
    
    print("\n")
    print(data[ncom_lines-1])
    print(data[normalize_line_num])
    print(normalize_line)


    return (normalize_line, normalize_line_num)
    
    


def get_breakpoints():
    """Get breakpoints.

From red band filter of lsst : phosim/data/lsst/filter_2.txt

We take wavelength range such that transmission <= 5%, and we get 531 nm - 696 nm

  0     1     2     3     4     5     6     7     8     9     10    11    12    13    14    15    16    17    18    19    20     21
  
  5310, 5388, 5467, 5545, 5624, 5703, 5781, 5860, 5938, 6017, 6096, 6174, 6253, 6331, 6410, 6489, 6567, 6646, 6724, 6803, 6882, 6960



"""
    lambda_start = 5310.0
    lambda_end = 6960.0

    # step between sed0 and sed1
    step = (lambda_end - lambda_start) / 21.0  # 7.9 nm


    # sed file has decimal precision 1, so round off step to one precision
    step = float(str(round(step, 1)))
    #print('{} {} {}'.format('\nlambda_start = ', lambda_start, 'nm'))
    #print('{} {} {}'.format('lambda_end = ', lambda_end, 'nm'))
    #print('{} {} {}'.format('lambda range = ', lambda_end - lambda_start, 'nm'))
    #print('{} {} {}'.format('step = ', step, ' nm\n'))

    breakpoints = np.arange(lambda_start, lambda_end, step)
    breakpoints = np.append(breakpoints, lambda_end)
    breakpoints = [int(i) for i in breakpoints]

    print(' ','     '.join(map(str, range(22))))
    print('{} {}{}'.format('breakpoints = \n', breakpoints, '\n\n'))
    #print('{} {}{}'.format('\nlen breakpoints = ', len(breakpoints), ''))
    
    return breakpoints


def get_lin_nums():
    """Get index of breakpoints."""
    lin_nums = []
    breakpoints = get_breakpoints()
    with open(infile, 'r') as fi:
        data = fi.readlines()
        idx, tmpidx = 0, 0
        for line in data:
            idx += 1
            for value in list(breakpoints):
                if (str(value) + '.0') in line:
                    tmpidx = idx
                    lin_nums.append(tmpidx)
    print('{} {} {}'.format('\nlin_nums = \n', lin_nums, ''))
    print('{} {} {}'.format('\nlen lin_nums = \n', len(lin_nums), '\n'))
    
    return lin_nums


def check_data():
    """Debug data breakpoints and lin_nums."""
    
    data = get_data(infile)
    breakpoints = get_breakpoints()
    lin_nums = get_lin_nums()
    
    print('{} {}{}'.format('data[0]   = \n', data[0], ''))
    print('{} {}{}'.format('len data  = ', len(data), ''))
    print('{} {}{}'.format('last data = ', data[(len(data) - 1)], ''))


    print('{} {}{}'.format('breakpoints[0] = ', breakpoints[0], ''))
    print('{} {}{}'.format('lin_nums[0]     = ', lin_nums[0], '\n'))

    print('{} {}{}'.format('breakpoints[1] = ', breakpoints[1], ''))
    print('{} {}{}'.format('lin_nums[1]     = ', lin_nums[1], '\n'))

    print('{} {}{}'.format('breakpoints[19] = ', breakpoints[19], ''))
    print('{} {}{}'.format('lin_nums[19]     = ', lin_nums[19], '\n'))

    print('{} {}{}'.format('breakpoints[20] = ', breakpoints[20], ''))
    print('{} {}{}'.format('lin_nums[20]     = ', lin_nums[20], '\n'))

    print('{} {}{}'.format('breakpoints[21] = ', breakpoints[21], ''))
    print('{} {}{}'.format('lin_nums[21]     = ', lin_nums[21], '\n'))



def write_narrowband_seds(outfolder):
    """Write 20 narrowbands and one broadband seds.

  0     1     2     3     4     5     6     7     8     9     10    11    12    13    14    15    16    17    18    19    20     21

    
[5310, 5388, 5467, 5545, 5624, 5703, 5781, 5860, 5938, 6017, 6096, 6174, 6253, 6331, 6410, 6489, 6567, 6646, 6724, 6803, 6882, 6960]

[4311, 4389, 4468, 4546, 4625, 4704, 4782, 4861, 4939, 5018, 5097, 5175, 5254, 5332, 5411, 5490, 5568, 5647, 5725, 5804, 5883, 5961] 

For exp9_pf_12gyr_interpolated.cat file:

narrowband0.sed
5310.0 5.8413982e-05
5387.0 5.64633062327e-05

narrowband1.sed
5388.0 5.64258902362e-05
5466.0 5.65162048804e-05

narrowband19.sed
6803.0 5.78295882118e-05
6881.0 5.8806992713e-05


narrowband20.sed
6882.0 5.88396263152e-05
6960.0 5.86330294926e-05

    
    """
    lin_nums = get_lin_nums()
    data = get_data(infile)
    ncom_lines = get_ncom_lines(data)
    normalize_line, normalize_line_num = get_normalizing_line(infile, lookup,data)
    replace_outdir(outfolder)
    
    print('{} {} {}'.format('\nwriting 21 output files ...', '', '\n'))
    nfiles = 21
    i = 0

    for i in range(nfiles):
        outfile = outfolder + r'/' + 'narrowband{:d}.sed'.format(i)
        with open(outfile, 'a') as f:

            # print
            print('{} {} {}'.format('writing to the file ', outfile, '...'))

            # add equal chunk_size data to all files
            lower = lin_nums[i] - 1
            upper = lin_nums[i + 1] - 1

            # write comment lines
            f.write(''.join(data[:ncom_lines]))

            for line in data:
                if not line.startswith('#'):
                    row = line.split()
                    tmp = str(row[0]) +'        ' +'0.0\n'
                    f.write(''.join(tmp))

                # print('{} {}{}'.format('\ni = ', i,'' ))
            j = 0
            for j in range(lin_nums[i], lin_nums[i + 1], 1):
                # print('{} {}{}'.format('j= ', j,'' ))
                replace_line(outfile, j - 1, data[j - 1])
                # print('{} {}{}'.format('data[j] = ', data[j],'' ))

        # add extra lines from index21 to index22 to last file
        # -1 is for 695.0
        if i == 20:
            for j in range(lin_nums[20] - 1, lin_nums[21], 1):
                replace_line(outfile, j, data[j])
        # rewrite normalized line at 500 nm from input sed to all output files
        replace_line(outfile, normalize_line_num, normalize_line)


def write_broadband_sed(outfolder):
    """Write broadband sed."""
    data = get_data(infile)
    ncom_lines = get_ncom_lines(data)
    lin_nums = get_lin_nums()
    normalize_line, normalize_line_num = get_normalizing_line(infile, lookup,data)
    
    
    outfile = outfolder + r'/' + 'broadband.sed'
    print('{} {} {}'.format('writing to the file ', outfile, '...'))
    with open(outfile, 'a') as f:

        # write comments
        f.write(''.join(data[:ncom_lines]))

        # change column two to zeros
        for line in data:
            if not line.startswith('#'):
                row = line.split()
                tmp = str(row[0]) + '        ' + '0.0\n'
                f.write(''.join(tmp))

        # replace line between lambda_start and lambda_end
        for j in range(lin_nums[0], lin_nums[21], 1):
            replace_line(outfile, j - 1, data[j - 1])

        # add one more line
        replace_line(outfile, j, data[j])


    # rewrite normalized line at 500 nm from input sed to all output files
    replace_line(outfile, normalize_line_num, normalize_line)

    # output info
    print('{} {} {}'.format('\ninput sed            : ', infile, ''))
    print('{} {} {}'.format('output folder        : ', outfolder, ''))
    print('{} {} {}'.format('output broadband sed :', outfile, ''))

def main(): 
    data = get_data(infile)
    ncom_lines = get_ncom_lines(data)
    normalize_line, normalize_line_num = get_normalizing_line(infile, lookup,data)
    breakpoints = get_breakpoints()
    lin_nums = get_lin_nums()
    #check_data()
    write_narrowband_seds(outfolder)
    write_broadband_sed(outfolder)
    
    
##==============================================================================
## Main program
##==============================================================================
if __name__ == '__main__':
    # Run main program
    main()



