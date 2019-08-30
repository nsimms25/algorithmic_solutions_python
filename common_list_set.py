'''
Two lists entered by the user.
Use python sets to find the union of the sets.

return sorted list of common elements.
'''

list1 = input('Please input the first list to be compared. ')
list2 = input('Please input the second list to be compared. ')

new_list1 = list1.split(', ')
new_list2 = list2.split(', ')

set1 = set(new_list1)
set2 = set(new_list2)

intersection = []

for i in set.intersection(set1, set2):
    intersection.append(int(i))

intersection.sort()

string = ', '.join(str(v) for v in intersection)
print(string)
