# Fill in this file with the authentication code from the Webex Teams exercise
# https://developer.webex.com/
# If you don't have an account yet, click Sign Up then Try Meetings Free and follow the instructions.
import requests
import json
# This access token may be a (limited duration) personal access token, a Bot token, or an OAuth token from an Integration or Guest Issuer application.
# IMPORTANT
# Make sure to replace access_token with YOUR access token.
access_token = ''
url = 'https://api.ciscospark.com/v1/people/me'
headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
