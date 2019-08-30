'''
Find the list of numbers that divide by an inputted number.

Param
n1: number to gate the list
n2: divisor

Return
list of numbers that evenly divide into [0,n1) by n2.
'''

# An empty list
l = []

# Get the numbers
n1 = int(input('Please enter a number: '))
n2 = int(input('Please enter a number to divide by: '))

for i in range(0,n1):
    if(i % n2 == 0):
        l.append(i)

print(l)
