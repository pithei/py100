"""
https://www.w3resource.com/python-exercises/python-basic-exercises.php

Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14

"""
from datetime import datetime

now = datetime.now()
datetime_str = now.strftime("%Y-%m-%d %H:%M:%S")

print("Current date and time:")
print(datetime_str)

	