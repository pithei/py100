"""
3.  Read in the 'show_version.txt' file. 
From this file, use regular expressions to extract the 
OS version, 
serial number, 
and configuration register values.

Your output should look as follows: 

OS Version: 15.4(2)T1      
Serial Number: FTX0000038X    
Config Register: 0x2102 
"""

import re

with open("show_version.txt") as f:
    data = f.read()

temp_version = re.search(r"Version.+,", data).group(0)
version = temp_version.split()[1].split(",")[0]

temp_serial = re.search(r"\*0.+", data).group(0)
serial = temp_serial.split()[2]

temp_register = re.search(r"Configuration register.+", data).group(0)
register = temp_register.split()[3]

print("OS Version: ", version)
print("Serial Number: ", serial)
print("Config Register: ", register)


'''
Solution, https://github.com/ktbyers/pynet/blob/master/learning_python/lesson4/exercise3.py

from __future__ import unicode_literals, print_function
import re

with open("show_version.txt") as f:
    show_ver = f.read()

match = re.search(r"^Cisco IOS Software,.* Version (.*),", show_ver, flags=re.M)
if match:
    os_version = match.group(1)

match = re.search(r"^Processor board ID (.*)\s*$", show_ver, flags=re.M)
if match:
    serial_number = match.group(1)

match = re.search(r"^Configuration register is (.*)\s*$", show_ver, flags=re.M)
if match:
    config_register = match.group(1)

print()
print("{:>20}: {:15}".format("OS Version", os_version))
print("{:>20}: {:15}".format("Serial Number", serial_number))
print("{:>20}: {:15}".format("Config Register", config_register))
print()
'''