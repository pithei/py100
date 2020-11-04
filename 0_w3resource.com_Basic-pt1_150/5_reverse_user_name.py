"""
Write a Python program which accepts the user's first and last name 
and print them in reverse order with a space between them

"""
user_first_name = input("Enter Your First Name:")
user_last_name = input("Enter Your Last Name:")

print(user_first_name[::-1], user_last_name[::-1])