'''
2021.01.17
windows getmac command, getmac /v /FO csv
regex pattern for mac match, \w\w:\w\w:\w\w:\w\w:\w\w:\w\w:
Algorithm:
    execute and read ifconfig
    read the mac address from output
    check if mac in ifconfig is what the user requested
    print appropriate message
'''

import subprocess
import optparse
import re

from pprint import pprint

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

def get_current_mac(interface):
    # search for mac addresses in interface details ( data taken from linux vm )
    # save ouptut from system command to a variable. PReferably, it should get mac from interface command, ip a show dev {interface}
    mac_details = subprocess.check_output(["getmac", "-v"])
    mac_details = mac_details.decode("UTF-8")
    mac_addresses = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", interface)
    #print(repr(nic_details))
    if mac_addresses:
        return mac_addresses.group(0)
    else:
        pass
        #print("No macs found in input")

argument_list = get_arguments()


interface = """root@vmdev:/home/user# ip a show dev enp0s3
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:83:a1:c2 brd ff:ff:ff:ff:ff:ff
    inet 192.168.88.10/24 brd 192.168.88.255 scope global dynamic noprefixroute enp0s3
       valid_lft 396sec preferred_lft 396sec
    inet6 fe80::6295:6731:d9ef:8967/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
root@vmdev:/home/user#
"""

current_mac = get_current_mac(interface)
print("Current mac", current_mac)