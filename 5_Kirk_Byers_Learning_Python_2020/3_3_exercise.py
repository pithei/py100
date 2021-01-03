"""

3.  Read the 'show_lldp_neighbors_detail.txt' file. 
Loop over the lines of this file. Keep reading the lines until you have encountered the remote "System Name" and remote "Port id". 
Save these two items into variables and print them to the screen. 
You should extract only the system name and port id from the lines (i.e. your variables should only have 'twb-sf-hpsw1' and '15'). 
Break out of your loop once you have retrieved these two items.

"""

with open("show_lldp_neighbors_detail.txt") as f:
    data = f.read()

sys_name_present, port_id_present = (False, False)
for line in data.splitlines():
    if "System Name" in line:
        sys_name_present = True
        field = line.split()
        sys_name = field[2]
    if "Port id" in line:
        port_id_present = True
        field = line.split()
        port_id = field[2]
    if sys_name_present and port_id_present:
        print("Sys NAme: {} \nPort ID: {}".format(sys_name, port_id))
        break

"""
Solution, https://github.com/ktbyers/pynet/blob/master/learning_python/lesson3/exercise3.py

#!/usr/bin/env python

from __future__ import unicode_literals, print_function


with open("show_lldp_neighbors_detail.txt") as f:
    show_lldp = f.read()

system_name, port_id = (None, None)
for line in show_lldp.splitlines():
    if "System Name: " in line:
        _, system_name = line.split("System Name: ")
    elif "Port id: " in line:
        _, port_id = line.split("Port id: ")

    if port_id and system_name:
        break

print()
print("System Name: {}".format(system_name))
print("Port ID: {}".format(port_id))
print()
"""