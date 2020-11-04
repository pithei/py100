"""
6. Write a Python program which accepts a sequence of comma-separated numbers from user 
and generate a list and a tuple with those numbers. Go to the editor
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')

"""

data = input("Please enter sequence, e.g: 1, 2, 3:: ")

data_list = data.split(",")

print("List: ", data_list)
print("Tuple: ", tuple(data_list))