'''
Find the list of unique words from a user inputted string.

Param
list1: string entered by the user. 

Return
Print the unique words list separated by ', '
'''

list1 = input('Please input the word list. ')

new_list1 = list1.split(', ')

set1 = set(new_list1)

unique = []

for i in set1:
    unique.append(i)

string = ', '.join(str(v) for v in unique)
print(string)
