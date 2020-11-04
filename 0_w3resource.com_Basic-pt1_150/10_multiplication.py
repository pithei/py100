"""
10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
Sample value of n is 5
Expected Result : 615

"""

n = int(input("Please enter integer:"))
result = n + n*n + n*n*n
print("Result: ", result)