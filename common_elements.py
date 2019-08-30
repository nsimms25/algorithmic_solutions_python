'''
Find common numbers between 2 lists

return a sort list of the common elements.
'''

l1 = [0, 3, 6, 9, 10, 2, 5]
l2 = [2, 6, 4, 7, 8, 1, 15]

# An empty list
common = []

for i in range(0,len(l1)):
    if(l1[i] in l2):
        common.append(l1[i])

common.sort()

print(common)
