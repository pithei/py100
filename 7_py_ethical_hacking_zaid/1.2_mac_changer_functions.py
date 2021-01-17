'''
2021.01.17
parse and validate input arguments from user
optparse module will be used
'''

import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Defined interface for mac addr change")
    parser.add_option("-m", "--mac", dest="new_mac", help="New mac address")
    data = parser.parse_args()
    if not data[0].interface:
        # code to handle error
        parser.error("[-] Please specify interface name, use --help or -h for more information.")
    elif not data[0].new_mac:
        # code to handle error
        parser.error("[-] Please specify new mac, use --help or -h for more information.")
    return parser.parse_args()

def change_mac(interface, new_mac):
    print(interface)
    print(new_mac)
    #subprocess.call(["ifconfig", interface, "down"])
    #subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    #subprocess.call(["ifconfig", interface, "up"])

data = get_arguments()
change_mac(data[0].interface, data[0].new_mac)