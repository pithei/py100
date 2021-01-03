"""
1. Read the "show_vlan.txt" file into your program. 
Loop through the lines in this file and extract all of 
the VLAN_ID, VLAN_NAME combinations. 
From these VLAN_ID and VLAN_NAME construct a new list where each 
element in the list is a tuple consisting of (VLAN_ID, VLAN_NAME). 
Print this data structure to the screen. Your output should look as follows: 

[('1', 'default'),
 ('400', 'blue400'),
 ('401', 'blue401'),
 ('402', 'blue402'),
 ('403', 'blue403')]
"""
from pprint import pprint
with open("show_vlan.txt") as f:
    data = f.readlines()

data = data[2:]
line_fields = []
for line in data:
    fields = line.split()
    line_fields.append(fields)

vlan_list = []
for line in line_fields:
    #print(type(line[0]))
    if(line[0].isdigit()):
        vlan_id = line[0]
        vlan_name = line[1]
        vlan_list.append((vlan_id, vlan_name))
    #print(line)

pprint(vlan_list)

"""
Solution, https://github.com/ktbyers/pynet/blob/master/learning_python/lesson3/exercise1.py

from __future__ import unicode_literals, print_function
from pprint import pprint

vlan_list = []
with open("show_vlan.txt") as f:
    show_vlan = f.read()

for line in show_vlan.splitlines():
    # Skip certain lines
    if "VLAN" in line or "-----" in line or line.startswith("  "):
        continue
    fields = line.split()
    vlan_id = fields[0]
    vlan_name = fields[1]
    vlan_list.append((vlan_id, vlan_name))

print()
pprint(vlan_list)
print()
"""