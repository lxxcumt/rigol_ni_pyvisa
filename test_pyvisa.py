#!/usr/bin/env python

############################################################################
# Date: 2017-11-14
############################################################################
# Author: Rawat S. 
#   (Dept. of Electrical & Computer Engineering, KMUTNB, Bangkok/Thailand)
#
############################################################################
# Short Description:
#   This Python script is used to test the USB connection to 
#   Rigol digital oscilloscopes (such as DS2072A) 
#   or function generators (DG1022).
#   It relies on the NI VISA interface / driver. 
#   (Make sure that the proper NI VISA driver has been installed correctly.)
#
############################################################################
# Usage:
#   Don't forget to install pyusb and pyvisa packages:
#   (When using Linux/Ubuntu, don't forget to use the sudo command).
# 
#   $ pip install pyusb -U
#   $ pip install pyvisa -U
#   $ pip install pyvisa-py -U
#
#   To run the script under Linux (e.g. Ubuntu)
#   (When using Linux/Ubuntu, don't forget to use the sudo command).
#
#   $ python2  ./test_pyvisa.py
#   $ python3  ./test_pyvisa.py
#
############################################################################

import visa
import time, sys

visa_driver = ''  #  use either 'visa64' or 'visa32' or '@py' or left empty. 
resources = visa.ResourceManager( visa_driver ) 
devices = resources.list_resources()

if len(devices) > 0:
    print ('Found #devices: %d' % len(devices) )
    for device in devices:
        print ('>>', device)
        
print (30*'-')

if len(devices) > 0:
    instr = resources.open_resource( devices[0] ) # select the first device found
    instr.write( '*IDN?' )
    ret_str = instr.read()
    fields = ret_str.split(',')
    dev_model = fields[2]
    print ( ', '.join(fields[0:3]) )
    #print (ret_str)
    print ( dev_model )
else:
    print ('No device found')

print ('\nDone....')

############################################################################
