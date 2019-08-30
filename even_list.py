'''
Find the list of numbers that divide evenly into user inputted number.

Print the list of numbers that divide evenly.
'''

# An empty list
l = []

#Get number
n = int(input('Please enter a number: '))

for i in range(0,n):
    if(i % 2 == 0):
        l.append(i)

print(l)
