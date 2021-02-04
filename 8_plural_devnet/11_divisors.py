"""
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

"""

data = int(input("Please enter number: "))
print(data)

for i in range(1, data+1):
    remainder = data % i
    if(remainder == 0):
        print("{} is divisor of number {}".format(i, data))

"""
Solution, https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

__author__ = 'jeffreyhunt'

num = int(input("Please choose a number to divide: "))

listRange = list(range(1,num+1))

divisorList = []

for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print(divisorList)
"""