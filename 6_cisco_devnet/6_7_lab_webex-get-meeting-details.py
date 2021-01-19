
room_id = '' # Make sure you add the room ID value that was returned from the previous call you made
url = 'https://api.ciscospark.com/v1/rooms/{}/meetingInfo'.format(room_id)
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
print(res.json())
