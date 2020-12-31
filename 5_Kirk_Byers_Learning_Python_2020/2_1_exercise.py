"""
2020.12.31 
1. Open the "show_version.txt" file for reading. 
Use the .read() method to read in the entire file contents to a variable.
Print out the file contents to the screen. 
Also print out the type of the variable (you should have a string at this point).

Close the file.

Open the file a second time using a Python context manager (with statement). 
Read in the file contents using the .readlines() method. 
Print out the file contents to the screen. 
Also print out the type of the variable (you should have a list at this point).

"""

f = open("show_version.txt")

output = f.read()
print(output)
print("Data type: ", type(output))
f.close()

with open("show_version.txt") as f:
    output = f.readlines()

for line in output:
    print(line)
print("Data type: ", type(output))



"""
Solution, https://github.com/ktbyers/pynet/blob/master/learning_python/lesson2/exercise1.py

from __future__ import print_function, unicode_literals

banner = "-" * 80

f = open("show_version.txt")
show_ver = f.read()

print(banner)
print(show_ver)
print(banner)
print(type(show_ver))
print(banner)
f.close()

with open("show_version.txt") as f:
    show_ver = f.readlines()

print("\n" + banner)
print(show_ver)
print(banner)
print(type(show_ver))
print(banner + "\n")
"""