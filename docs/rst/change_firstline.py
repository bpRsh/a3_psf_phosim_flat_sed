#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Jul 24, 2017 Mon
# Last update : 
#
import subprocess
import glob
import os

def replace_first_line():
    ''' This function replaces a string in first line of all *.rst files.'''
    for infile in glob.glob("*.rst"):
        lines = open(infile, 'r').readlines()
        lines[0] = lines[0].replace("module", "")
        out = open(infile, 'w')
        out.writelines(lines)
        out.close()
             
        
if __name__ == '__main__':
    replace_first_line()


