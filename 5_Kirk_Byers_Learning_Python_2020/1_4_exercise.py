"""
2020.12.30
4. Create a show_version variable that contains the following

 show_version = "*0        CISCO881-SEC-K9       FTX0000038X    " 

Remove all leading and trailing whitespace from the string.

Split the string and extract the model and serial_number from it.

Check if 'Cisco' is contained in the model string (ignore capitalization).

Check if '881' is in the model string.

Print out both the serial number and the model.

"""


show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "
#print(repr(show_version))
show_version = show_version.lstrip().rstrip()
#print(repr(show_version))
show_version = show_version.split()
model = show_version[1]
serial = show_version[2]
print("Model {}".format(model))
print("881 is present in model: {}".format('881' in model))
print("Serial number {}".format(serial))




"""
Solution, https://github.com/ktbyers/pynet/blob/master/learning_python/lesson1/exercise4.py

show_version = "*0  	  CISCO881-SEC-K9       FTX0000038X    "
show_version = show_version.strip()

fields = show_version.split()
model = fields[1]
serial_number = fields[2]

print()
vendor_cisco = "cisco" in model.lower()
print("Checking if model contains Cisco: {}".format(vendor_cisco))

model_881 = "881" in model
print("Checking if model contains 881: {}".format(model_881))

print("Serial Number: {}".format(serial_number))
print("Model: {}".format(model))
print()


"""