"""
1. Create a dictionary representing a network device. 
The dictionary should have key-value pairs representing the 'ip_addr', 'vendor', 'username', and 'password' fields.

Print out the 'ip_addr' key from the dictionary.

If the 'vendor' key is 'cisco', then set the 'platform' to 'ios'. 
If the 'vendor' key is 'juniper', then set the 'platform' to 'junos'.

Create a second dictionary named 'bgp_fields'. 
The 'bgp_fields' dictionary should have a keys for 'bgp_as', 'peer_as', and 'peer_ip'.

Using the .update() method add all of the 'bgp_fields' dictionary key-value pairs to the network device dictionary.

Using a for-loop, iterate over the dictionary and print out all of the dictionary keys.

Using a single for-loop, iterate over the dictionary and print out all of the dictionary keys and values.
"""

device ={
    "ip_addr" : "1.2.3.4",
    "vendor" : "cisco",
    "username" : "user",
    "password" : "password"
}

bgp_fields ={
    "bgp_as" : "65321",
    "peer_as" : "65421",
    "peer_ip" : "1.2.3.5"
}
print(device["ip_addr"])

if device["vendor"] == "cisco":
    device["platform"] = "ios"

if device["vendor"] == "juniper":
    device["platform"] = "junos"

print(device["platform"])

device.update(bgp_fields)
print(device)


for key, value in device.items():
    print(key)

for key, value in device.items():
    print(key, " ", value)

"""
Solution, https://github.com/ktbyers/pynet/blob/master/learning_python/lesson4/exercise1.py

from __future__ import unicode_literals, print_function

net_device = {
    "ip_addr": "10.10.10.10",
    "vendor": "cisco",
    "username": "admin",
    "password": "password",
}

print()
print(net_device["ip_addr"])
print()

if net_device["vendor"].lower() == "cisco":
    net_device["platform"] = "ios"
elif net_device["vendor"].lower() == "juniper":
    net_device["platform"] = "junos"

bgp_fields = {
    "bgp_as": 42,
    "peer_as": 100,
    "peer_ip": "172.16.31.100",
}

net_device.update(bgp_fields)

print("-" * 80)
for key in net_device:
    print("{:>15}".format(key))
print("-" * 80)
print()

print("-" * 80)
for key, value in net_device.items():
    print("{key:>15} ---> {value:>15}".format(key=key, value=value))
print("-" * 80)
print()
"""