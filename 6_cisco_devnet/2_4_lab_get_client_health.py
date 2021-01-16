
import requests
# requests documentation: https://requests.readthedocs.io/en/master/
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json
import sys

##### Cisco DNA Center URL and Authentication Credentials
# In a 'real' application, this information might be in a 'config.py' file
# to keep authentication and target information out of the primary logic
# - Authentication to DevAsc DNA Center
dnacip = "devasc-dnacenter-1.cisco.com"
username = "devnetuser"
password = "C!3c0d$Y"
#####

# define Authentication method
def get_X_auth_token(dnacip,username,password):
    """
    Authenticate to remote Cisco DNA Center

    Parameters
    ----------
    dnacip (str): dnac routable DNS address or ip
    username (str): dnac user name
    password (str): password

    Return:
    ----------
    str: dnac access token
    """

    # Suppress credential warning for this exercise
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    # Authentication API full URI
    post_uri = "https://"+dnacip+"/dna/system/api/v1/auth/token"
    print ("\nAuthenticate: POST %s"%(post_uri))

    try:
        # verify=False to suppress verify server's TLS certificate
        #  In production code, verify should be set as default to 'True'
        r = requests.post(post_uri, auth=(username, password), verify=False)
        return r.json()["Token"]
    except:
        # Failed to obtain access token
        print ("Status: %s"%r.status_code)
        print ("Response: %s"%r.text)
        sys.exit ()

# Get Client Health API wrapper
def get_client_health(dnacip, headers, params):
    """
    Get Client Health API wrapper
    This function returns the response from a Get Client Health request
    if Status = 200
    else it prints the Status and response and aborts.

    Parameters
    ----------
    dnacip (str): dnac routable DNS address or ip
    headers: headers for request
    params: parameters to be added to the GET request.

    Return:
    ----------
    response
    """

    # Get Client Health URI
    uri = "https://"+dnacip+"/dna/intent/api/v1/client-health"
    try:
        if params == "":
            print ("\n---\nGET %s"%(uri))
        else:
            print ("\n---\nGET %s?%s"%(uri,params))

        resp = requests.get(uri,headers=headers,params=params,verify = False)
        return resp
    except:
        # Failed to obtain access token
        print ("Status: %s"%r.status_code)
        print ("Response: %s"%r.text)
        sys.exit ()

# Authenticate to the Cisco DNA Center
# and obtain an authentication token
token = get_X_auth_token(dnacip, username, password)
print ("returned Authentication Token: ", (token))

# assign the authentication token to a header key value pair
# 'x-auth-token'={{token}}
headers = {"x-auth-token": token}

# Start by getting a count of all devices of all types known to the Cisco DNA Center
# by appending "/count" to the Get Network_Devices URI
params=""
resp = get_client_health(dnacip, headers, params)
print ("All clients health: ",json.dumps(resp.json()["response"], indent=4))
