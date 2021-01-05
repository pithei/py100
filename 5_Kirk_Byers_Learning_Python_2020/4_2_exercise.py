"""
2. Create three separate lists of IP addresses. 
The first list should be the IP addresses of the Houston data center routers, 
and it should have over ten RFC1918 IP addresses in it (including some duplicate IP addresses).

The second list should be the IP addresses of the Atlanta data center routers, 
and it should have at least eight RFC1918 IP addresses (including some addresses that overlap with the Houston data center).

The third list should be the IP addresses of the Chicago data center routers, 
and it should have at least eight RFC1918 IP addresses. 
The Chicago IP addresses should have some overlap with both the IP addresses in Houston and Atlanta.

Convert each of these three lists to a set.

Using a set operation, find the IP addresses that are duplicated between Houston and Atlanta.

Using set operations, find the IP addresses that are duplicated in all three sites.

Using set operations, find the IP addresses that are entirely unique in Chicago.
"""

ip_huston = [
    "10.10.10.1",
    "10.10.10.1",
    "10.10.10.1",
    "10.20.10.1",
    "10.20.10.1",
    "10.30.10.1",
    "10.30.10.1",
    "10.10.10.1",
    "10.10.10.1",
    "10.10.30.1"
]

ip_atlanta = [
    "10.10.10.1",
    "10.10.30.1",
    "10.100.10.1",
    "10.100.20.1",
    "10.100.30.1",
    "10.100.40.1",
    "10.100.50.1",
    "10.100.60.1"
]

ip_chicago = [
    "10.10.10.1",
    "10.200.100.1",
    "10.200.30.1",
    "10.200.10.1",
    "10.200.20.1",
    "10.200.30.1",
    "10.200.30.1",
    "10.200.30.1",
    "10.200.40.1",
    "10.200.50.1",
    "10.200.60.1"
]

ip_huston = set(ip_huston)
ip_atlanta = set(ip_atlanta)
ip_chicago = set(ip_chicago)

print(ip_huston & ip_atlanta)
print(ip_huston & ip_atlanta & ip_chicago)
print(ip_chicago - ip_huston - ip_atlanta)

"""
Solution, https://github.com/ktbyers/pynet/blob/master/learning_python/lesson4/exercise2.py

from __future__ import unicode_literals, print_function

houston_ips = [
    "10.10.10.1",
    "10.10.20.1",
    "10.10.30.1",
    "10.10.40.1",
    "10.10.50.1",
    "10.10.60.1",
    "10.10.70.1",
    "10.10.80.1",
    "10.10.10.1",
    "10.10.20.1",
    "10.10.70.1",
]

atlanta_ips = [
    "10.10.10.1",
    "10.10.20.1",
    "10.10.30.1",
    "10.10.140.1",
    "10.10.150.1",
    "10.10.160.1",
    "10.10.170.1",
    "10.10.180.1",
]

chicago_ips = [
    "10.10.10.1",
    "10.10.20.1",
    "10.10.140.1",
    "10.10.150.1",
    "10.10.210.1",
    "10.10.220.1",
    "10.10.230.1",
    "10.10.240.1",
]

houston_ips = set(houston_ips)
atlanta_ips = set(atlanta_ips)
chicago_ips = set(chicago_ips)

# Duplicate IPs at both sites (set intersection)
print()
print("-" * 80)
print(
    "Duplicate IPs at Houston and Atlanta sites:\n\n{}".format(
        houston_ips & atlanta_ips
    )
)
print("-" * 80)
print()
print("-" * 80)
print(
    "Duplicate IPs at all three sites:\n\n{}".format(
        houston_ips & atlanta_ips & chicago_ips
    )
)
print("-" * 80)
print()

# Chicago unique IP addresses
print("-" * 80)
print(
    "Chicago unique IP addresses:\n\n{}".format(
        chicago_ips.difference(houston_ips).difference(atlanta_ips)
    )
)
print("-" * 80)
print()
"""

