"""
5. [Optional/bonus] 

*** Note, to actually test this in your environment, change the test IP addresses to something in your environment that you can ping successfully. ***

Construct a list of 254 IP addresses. The base IP address should be equal to '10.10.100.0' or '10.10.100.'.

You should use the 'range' builtin to accomplish this.

Your list should have all of the IP addresses from 10.10.100.1 to 10.10.100.254.

Use Python's 'enumerate' to print out all of the IP addresses and their corresponding list index. The output should look similar to the following:  

0 ---> 10.10.100.1
1 ---> 10.10.100.2
2 ---> 10.10.100.3
3 ---> 10.10.100.4
4 ---> 10.10.100.5
...

Use a list slice to create a new list that goes from 10.10.100.3 to 10.10.100.6.

Using a loop and os.system("ping -c 3 10.10.100.3") try pinging all of the IP addresses in this short list. 
For Windows the command will probably be os.system("ping -n 3 10.10.100.3").

Put a variable at the top to define whether you are using Windows or Linux/MacOs. This should be similar to the following: 

WINDOWS = False

base_cmd_linux = 'ping -c 2 '
base_cmd_windows = 'ping -n 2 '
# Ternary operator
base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux
"""
import sys
import os

base_cmd_linux = 'ping -c 2'
base_cmd_windows = 'ping -n 2'

platform = sys.platform

base_cmd = base_cmd_windows if 'win' in platform else base_cmd_linux

#print(base_cmd)

subnet_ips = []
for i in range(255):
    generated_ip = "192.168.88." + str(i)
    subnet_ips.append(generated_ip)

print("-" * 100)

for ip in enumerate(subnet_ips):
    #print(ip)
    pass

print("-" * 100)

sliced_ips = subnet_ips[3:7]
print(sliced_ips)
print("-" * 100)

for ip in sliced_ips:
    print(ip)

print("-" * 100)
print("pinging sliced ip range:")
print("-" * 100)

for ip in sliced_ips:
    os_command = base_cmd + " " + ip
    print(os_command)
    os.system(os_command)

"""
Solution, https://github.com/ktbyers/pynet/blob/master/learning_python/lesson3/exercise5.py

from __future__ import unicode_literals, print_function
import os

# Toggle this to use Windows
WINDOWS = False

base_ip = "10.10.100."
base_cmd_linux = "ping -c 2"
base_cmd_windows = "ping -n 2"
# Ternary operator
base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux

ip_list = []
for last_octet in range(1, 255):
    new_ip = base_ip + str(last_octet)
    ip_list.append(new_ip)

for i, ip_addr in enumerate(ip_list):
    print("{} ---> {}".format(i, ip_addr))

# Only use IP addresses 8.8.4.3 to 8.8.4.6
ip_list = ip_list[2:6]

print()
print("-" * 80)
for ip_addr in ip_list:
    print("IP Addr: ", ip_addr)
    return_code = os.system("{} {}".format(base_cmd, ip_addr))
    print("-" * 80)
print("-" * 80)
print()
© 2021 GitHub, Inc.
"""