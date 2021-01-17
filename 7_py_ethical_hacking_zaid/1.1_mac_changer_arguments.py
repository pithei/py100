'''
2021.01.17
parse and validate input arguments from user
optparse module will be used
'''

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Defined interface for mac addr change")
parser.add_option("-m", "--mac", dest="new_mac", help="New mac address")

data = parser.parse_args()

print(data[0].interface,)
print(data[0].new_mac)