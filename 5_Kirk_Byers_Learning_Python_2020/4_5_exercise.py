"""
5. Read the 'show_ipv6_intf.txt' file.

From this file, use Python regular expressions to extract the two IPv6 addresses.

The two relevant IPv6 addresses you need to extract are: 

    2001:11:2233::a1/24
    2001:cc11:22bb:0:2ec2:60ff:fe4f:feb2/64

Try to use re.DOTALL flag as part of your search. 
Your search pattern should not include any of the literal characters in the IPv6 address.

From this, create a list of IPv6 addresses that includes only the above two addresses.

Print this list to the screen.
"""

import re
from pprint import pprint
with open("show_ipv6_intf.txt") as f:
    data = f.read()

#print(data)
match = re.search(r"IPv6 address:(?P<addr>.*) .* IPv6 subnet", data, flags=re.DOTALL)
if match:
    data_list = match.groupdict()

addresses = data_list["addr"].split()
#print(addresses)

for key in addresses:
    if "/" in key:
        print(key)

"""
Solution, https://github.com/ktbyers/pynet/blob/master/learning_python/lesson4/exercise5.py
from __future__ import unicode_literals, print_function
import re

with open("show_ipv6_intf.txt") as f:
    output = f.read()

# Use re.DOTALL to have .* span newlines
match = re.search(r"IPv6 address:\s+(.*)\s+IPv6 subnet:", output, flags=re.DOTALL)
# Extract the matched pattern and strip any white space
ipv6_addresses = match.group(1).strip()
ipv6_list = ipv6_addresses.splitlines()
# Strip out [VALID] from the IPv6 address string
for i, address in enumerate(ipv6_list[:]):
    address = re.sub(r"\[VALID\]", "", address)
    ipv6_list[i] = address.strip()

print()
print("-" * 80)
print(ipv6_list)
print("-" * 80)
print()

"""