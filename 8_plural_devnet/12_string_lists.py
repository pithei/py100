"""
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
"""

data = list(input("Please provide text:"))
data_original = data.copy()
data.reverse()

if (data == data_original):
    print("This is Polyndrome.")
else:
    print("This is Not Polyndrome.")

"""
Solution, https://www.practicepython.org/solution/2014/03/19/06-string-lists-solutions.html
A sample solution using string reversal
wrd=str(wrd)
rvs=wrd[::-1]
print(rvs)
if wrd == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")


A sample solution using for loops
def reverse(word):
	x = ''
	for i in range(len(word)):
		x += word[len(word)-1-i]
	return x

word = input('give me a word:\n')
x = reverse(word)
if x == word:
	print('This is a Palindrome')
else:
	print('This is NOT a Palindrome')
"""