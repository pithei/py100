"""
2. Create a list of five IP addresses.

Use the .append() method to add an IP address onto the end of the list. 
Use the .extend() method to add two more IP addresses to the end of the list.

Use list concatenation to add two more IP addresses to the end of the list.

Print out the entire list of ip addresses. 
Print out the first IP address in the list. 
Print out the last IP address in the list.

Using the .pop() method to remove the first IP address in the list and the last IP address in the list.

Update the new first IP address in the list to be '2.2.2.2'. 
Print out the new first IP address in the list.

"""

ipam = ['1.1.1.1', '2.2.2.2', '3.3.3.3', '4.4.4.4', '5.5.5.5']
ipam.append('6.6.6.6')
#print(ipam)

ipam.extend(['7.7.7.7', '8.8.8.8'])
print(ipam)
print(ipam[0])
print(ipam[-1])

ipam.pop(0)
ipam.pop(1)

ipam[0] = '22.22.22.22'
print(ipam)
print(ipam[0])


"""
Solution, https://github.com/ktbyers/pynet/blob/master/learning_python/lesson2/exercise2.py


from __future__ import print_function, unicode_literals

my_ipaddress = ["192.168.1.1", "10.1.1.1", "172.16.31.254", "8.8.8.8", "8.8.4.4"]
my_ipaddress.append("10.10.10.10")
my_ipaddress.extend(["1.1.1.1", "1.1.1.2"])
my_ipaddress = my_ipaddress + ["172.16.1.1", "172.16.1.2"]
print(my_ipaddress)

print(my_ipaddress[0])
print(my_ipaddress[-1])

first_ip = my_ipaddress.pop(0)
last_ip = my_ipaddress.pop()

my_ipaddress[0] = "2.2.2.2"
print(my_ipaddress[0])

"""