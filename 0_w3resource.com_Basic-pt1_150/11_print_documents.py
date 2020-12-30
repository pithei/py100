"""
11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.

"""

function_name = input("Please enter function name:")
print(type(function_name))
print("Result: ", function_name.__doc__)


"""
Solution, https://www.w3resource.com/python-exercises/python-basic-exercise-11.php
a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)

"""