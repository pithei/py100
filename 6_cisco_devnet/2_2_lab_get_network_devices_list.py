
T
Me
Cisco platforms and development
Module Overview
Introduction to Cisco platforms
Cisco SDKs
Understanding network programmability and device models
Cisco network management
Network management platforms
Cisco IOS XE
Cisco DNA Center
Cisco DNA Center hands-on Lab
...
Introduction
1
Cisco DNA Center Authentication API
2
Get Device List and Get Device Count
3
Get client health
Cisco ACI
Cisco ACI hands-on Lab
Cisco Meraki
Meraki Dashboard API
Cisco NX-OS platform
Cisco NSO
Cisco NSO hands-on Lab
Cisco SD-WAN
Cisco SD-WAN hands-on Lab
Quiz for Cisco network management
Cisco compute management
Cisco collaboration platforms
Cisco security platforms
Resources for further study
Quiz for Cisco platforms and development
Module Summary
Get Device List and Get Device Count
Get Device List and Get Device Count
The Get Device List (GET /dna/intent/api/v1/network-device) API request returns an array with details of network devices.
If additional parameters are specified the method will filter based on that criteria.
If no parameters are provided, it will return information for all known network devices.

Documentation for this method is in DevNet Cisco DNA Center Intent API.

GET Device List

Figure 1. Get Device List

We'll build on the authentication logic already completed and add a call to GET Device List.
As with the Authenticate, we'll first create a GET Network Device API function as we'll end up calling it in different ways.

If you are not already in the ~/src/dna-center directory, change to it now.

cd ~/src/dna-center
Click on the file ~/src/dna-center/get_network_devices_list.py to open it for edit,
and use the copy widget to copy the following Python code into it.

import requests
# requests documentation: https://requests.readthedocs.io/en/master/
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json
import sys
​
##### Cisco DNA Center URL and Authentication Credentials
# In a 'real' application, this information might be in a 'config.py' file
# to keep authentication and target information out of the primary logic
# - Authentication to DevAsc DNA Center
dnacip = "devasc-dnacenter-1.cisco.com"
username = "devnetuser"
password = "C!3c0d$Y"
#####
​
# define Authentication method
def get_X_auth_token(dnacip,username,password):
    """
    Authenticate to remote Cisco DNA Center
​
    Parameters
    ----------
    dnacip (str): dnac routable DNS address or ip
    username (str): dnac user name
    password (str): password
​
    Return:
    ----------
    str: dnac access token
    """
​
    # Supress credential warning for this exercise
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
​
    # Authentication API full URI
    post_uri = "https://"+dnacip+"/dna/system/api/v1/auth/token"
    print ("\nAuthenticate: POST %s"%(post_uri))
​
    try:
        # verify=False to suppress verify server's TLS certificate
        #  In production code this should be left to default to 'True'
        r = requests.post(post_uri, auth=(username, password), verify=False)
        return r.json()["Token"]
    except:
        # Failed to obtain access token
        print ("Status: %s"%r.status_code)
        print ("Response: %s"%r.text)
        sys.exit ()
​
# Get Network Device API wrapper
def get_network_device(dnacip, headers, params, modifier):
    """
    Get Network Device API wrapper
    This function returns the response from a Get Network Device request
    if Status = 200
    else it prints the Status and reponse and aborts.
​
    Parameters
    ----------
    dnacip (str): dnac routable DNS address or ip
    headers: headers for request
    params: parameters to be added to the GET request.
​
    Return:
    ----------
    response
    """
​
    # Get Network Device URI
    uri = "https://"+dnacip+"/dna/intent/api/v1/network-device"+modifier
    try:
        if params == "":
            print ("\n---\nGET %s"%(uri))
        else:
            print ("\n---\nGET %s?%s"%(uri,params))
​
        resp = requests.get(uri,headers=headers,params=params,verify = False)
        return resp
    except:
        # Failed to obtain access token
        print ("Status: %s"%r.status_code)
        print ("Response: %s"%r.text)
        sys.exit ()
​
# Authenticate to the Cisco DNA Center
# and obtain an authentication token
token = get_X_auth_token(dnacip, username, password)
print ("returned Authentication Token: ", (token))
​
# assign the authentication token to a header key value pair
# 'x-auth-token'={{token}}
headers = {"x-auth-token": token}
​
# Start by getting a count of all devices of all types known to the Cisco DNA Center
# by appending "/count" to the Get Network_Devices URI
params=""
modifier="/count"
resp = get_network_device(dnacip, headers, params, modifier)
print ("All devices count: ",json.dumps(resp.json()["response"]))
​
# Lets look at the full set of information:
params=""
modifier=""
resp = get_network_device(dnacip, headers, params, modifier)
print(json.dumps(resp.json()["response"],indent=4))
The new code in this section is the get_network_device() and some lines of code that follow after printing the token.
(In get_network_device() there is logic to print the combined URI to standard output.
That logic is for learning purposes only so that we can see whats going on.
In a production environment that information might be omitted, or redirected to a log file, or suppressed in some manner.)

After the authentication section, the obtained token is assigned to a simple JSON dictionary (header) that is a name-value pair defining the 'x-auth-token'.
When the header structure is provided to the requests.get() function,
it generates the actual HTTP request with the correct authentication header.

The get_network_device() function is used twice.
To create the GET Device Count request, the function is called with the modifier (/count) .
This actually changes the URI request from /dna/intent/api/v1/network-device to /dna/intent/api/v1/network-device/count which returns a count of network devices.
No filter is specified so the value returned should be a count of the all known devices.

To obtain the device information, the code then calls get_network_device() a second time without the modifier (/count) so that it requests an array of all known network devices. This is the GET Device List request.

Run this script:

python get_network_devices_list.py
The output result will look similar to the following:

 Output
All the information on all devices, produces a lot of output, and if this
was a real production environment, it could be too much to effectively use.
It's better to narrow down the request by specifying that we want a subset of devices.

For this next section, rather than printing the complete response, we'll parse the response for specific values.
We'll use the device count to cycle through each element of the returned array to extract key information.

Finally we'll parse out the associated 'Vlan' values for each Cisco 9300 Series device.
For this last request, we'll add a modifier such that the get_network_device() constructs and issues a GET Device Interface VLANS request.

Start this section by first opening the file src/dna-center/get_network_devices.py
and use the copy widget to copy the following Python code into it.

import requests
# requests documentation: https://requests.readthedocs.io/en/master/
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json
import sys
​
##### Cisco DNA Center URL and Authentication Credentials
# In a 'real' application, this information might be in a 'config.py' file
# to keep authentication and target information out of the primary logic
# - Authentication to DevAsc DNA Center
dnacip = "devasc-dnacenter-1.cisco.com"
username = "devnetuser"
password = "C!3c0d$Y"
#####
​
# define Authentication method
def get_X_auth_token(dnacip,username,password):
    """
    Authenticate to remote Cisco DNA Center
​
    Parameters
    ----------
    dnacip (str): dnac routable DNS address or ip
    username (str): dnac user name
    password (str): password
​
    Return:
    ----------
    str: dnac access token
    """
​
    # Suppress credential warning for this exercise
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
​
    # Authentication API full URI
    post_uri = "https://"+dnacip+"/dna/system/api/v1/auth/token"
    print ("\nAuthenticate: POST %s"%(post_uri))
​
    try:
        # verify=False to suppress verify server's TLS certificate
        #  In production code this should be left to default to 'True'
        r = requests.post(post_uri, auth=(username, password), verify=False)
        return r.json()["Token"]
    except:
        # Failed to obtain access token
        print ("Status: %s"%r.status_code)
        print ("Response: %s"%r.text)
        sys.exit ()
​
# Get Network Device API wrapper
def get_network_device(dnacip, headers, params, modifier):
    """
    GET Network Device API wrapper
    This function returns the response from a Get Network Device request
    if Status = 200
    else it prints the Status and response and aborts.
​
    Parameters
    ----------
    dnacip (str): dnac routable DNS address or ip
    headers: headers for request
    params: parameters to be added to the GET request.
​
    Return:
    ----------
    response
    """
​
    # Get Network Device URI
    uri = "https://"+dnacip+"/dna/intent/api/v1/network-device"+modifier
    try:
        if params == "":
            print ("\n---\nGET %s"%(uri))
        else:
            print ("\n---\nGET %s?%s"%(uri,params))
​
        resp = requests.get(uri,headers=headers,params=params,verify = False)
        return resp
    except:
        # Something went wrong. Provide status informaton and terminate
        print ("Status: %s"%r.status_code)
        print ("Response: %s"%r.text)
        sys.exit ()
​
# Authenticate to the Cisco DNA Center
# and obtain an authentication token
token = get_X_auth_token(dnacip, username, password)
print ("returned Authentication Token: ", (token))
​
# assign the authentication token to a header key value pair
# 'x-auth-token'={{token}}
headers = {"x-auth-token": token}
​
# Start by getting a count of all devices of all types known to the Cisco DNA Center
# by appending "/count" to the Get Network_Devices URI
params=""
modifier="/count"
resp = get_network_device(dnacip, headers, params, modifier)
print ("All devices count: ",json.dumps(resp.json()["response"]))
​
# Focus on just those devices that are Cisco 9300 Switches.
# Use a filter to limit responses to '9300 Series Switches'
​
# Start with a count of those devices
params="series=Cisco Catalyst 9300 Series Switches"
modifier="/count"
resp = get_network_device(dnacip, headers, params, modifier)
​
switch_count = int(json.dumps(resp.json()["response"]))
print ("Catalyst 9300 Switch count: ",switch_count)
​
# Request a list of the Cisco 9300 Switches
# (remove the '/count' modifier, but leave the filter in place)
modifier = ""
resp = get_network_device(dnacip, headers, params, modifier)
print ("Catalyst 9300 Switch list: ",json.dumps(resp.json()["response"], indent=4))
​
# Focus in on key information from these devices and pull out just
# key identifying information such as device Type, Id, serial number, and IPv4
​
json_resp = resp.json()["response"]
​
for i in range(0, switch_count):
    print("Switch %d:  Type: %s.  Serial Number: %s.  DeviceId: %s. Mgmt IPv4: %s"
      %(i, json_resp[i]['type'], json_resp[i]['serialNumber'],json_resp[i]['id'],
        json_resp[i]['managementIpAddress']))
​
# Finally, use each device identifier to discover the VLANs associated to that switch
params = ""
​
for i in range(0, switch_count):
    modifier = "/"+json_resp[i]['id']+"/vlan"
    resp = get_network_device(dnacip, headers, params, modifier)
    print("Device Serial Number %s is attached to VLANs:"%(json_resp[i]['serialNumber']))
    print(json.dumps(resp.json()["response"],indent=4))
This code starts where we left off, but drops the last section that obtains and prints all information from all known devices.

Instead, a filter is used to select a subset of devices,
by looking for just those devices that are part of the "Cisco Catalyst 9300 Series Switches" series.
We first get a count of this subset, and then use that count to iterate through the results
to extract out just the fields of interest: Type, Serial Number, Device Id, and Management IP address.

Finally, the deviceId for each of these switches is used to obtain information
about its associated VLANs.
This demonstrates the ability to navigate, via the Intent API,
through a DNA Center device object model to
learn more and find associate entities, such as VLANs.

Run this script:

python get_network_devices.py
The output result will look similar to the following:

 Output
Ready to go!
Environment spun up in 2s.
Code as you learn!
Continue the learning lab to unlock the full interactive experience.
Search ...
get_network_devices_list.py
79
        return resp
80
    except:
81
        # Failed to obtain access token
82
        print ("Status: %s"%r.status_code)
83
        print ("Response: %s"%r.text)
84
        sys.exit ()
85
​
86
# Authenticate to the Cisco DNA Center
87
# and obtain an authentication token
88
token = get_X_auth_token(dnacip, username, password)
89
print ("returned Authentication Token: ", (token))
90
​
91
# assign the authentication token to a header key value pair
92
# 'x-auth-token'={{token}}
93
headers = {"x-auth-token": token}
94
​
95
# Start by getting a count of all devices of all types known to the Cisco DNA Center
96
# by appending "/count" to the Get Network_Devices URI
97
params=""
98
modifier="/count"
99
resp = get_network_device(dnacip, headers, params, modifier)
100
print ("All devices count: ",json.dumps(resp.json()["response"]))
101
​
102
# Lets look at the full set of information:
103
params=""
104
modifier=""
105
resp = get_network_device(dnacip, headers, params, modifier)
106
print(json.dumps(resp.json()["response"],indent=4))
107
​
Terminal
