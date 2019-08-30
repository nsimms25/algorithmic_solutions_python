'''
Create a dictionary of the inputted numbers and their squares.

Param
List of numbers separated by '-'

Return
Print the dictionary of numbers and resulting squares.
'''

nums = input('''Please enter a series of numbers separated by '-'. \n Hit enter when you are done. ''')

nums_list = nums.split('-')

new_list = [int(i) for i in nums_list]

square_dict = {}

for i in range(0,len(new_list)):
    key = new_list[i]
    value = new_list[i] * new_list[i]
    square_dict[key] = value

print(square_dict)
