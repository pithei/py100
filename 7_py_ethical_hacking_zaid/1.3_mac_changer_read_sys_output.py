'''
2021.01.17

getmac /v /FO csv

\w\w:\w\w:\w\w:\w\w:\w\w:\w\w:
Algorithm:
    execute and read ifconfig
    read the mac address from output
    check if mac in ifconfig is what the user requested
    print appropriate message


data from iproute output
if_data = "root@vmdev:/home/user# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:83:a1:c2 brd ff:ff:ff:ff:ff:ff
    inet 192.168.88.10/24 brd 192.168.88.255 scope global dynamic noprefixroute enp0s3
       valid_lft 433sec preferred_lft 433sec
    inet6 fe80::6295:6731:d9ef:8967/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
3: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default
    link/ether 02:42:c7:60:7c:7f brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
root@vmdev:/home/user#"
""
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

argument_list = get_arguments()


nic_details = """root@vmdev:/home/user# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:83:a1:c2 brd ff:ff:ff:ff:ff:ff
    inet 192.168.88.10/24 brd 192.168.88.255 scope global dynamic noprefixroute enp0s3
       valid_lft 433sec preferred_lft 433sec
    inet6 fe80::6295:6731:d9ef:8967/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
3: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default
    link/ether 02:42:c7:60:7c:7f brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
root@vmdev:/home/user#"""

# save ouptu from system command to a variable
mac_details = subprocess.check_output(["getmac", "-v"])
mac_details = mac_details.decode("UTF-8")

# search for mac addresses in interface details ( data taken from linux vm )

mac_addresses = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", nic_details)
print(repr(nic_details))
if mac_addresses:
    #print("Some Data found")
    print(mac_addresses.group(0))
else:
    print("No macs found in input")

