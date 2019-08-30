'''
Lists entered by user.

return sorted list of the common elements.
'''

l1 = []
l2 = []

print('Please input list of 7 elements and separate each element by enter: ')
for i in range(0, 7): 
    ele = int(input()) 
  
    l1.append(ele) # adding the element 

print('Please input a second list of 7 elements and separate each element by enter: ')
for i in range(0, 7): 
    ele = int(input()) 
  
    l2.append(ele) # adding the element 

common = []
for i in range(0,len(l1)):
    if(l1[i] in l2):
        common.append(l1[i])

common.sort()
print(common)
