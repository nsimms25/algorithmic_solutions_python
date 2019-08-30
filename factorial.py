'''
Find the factorial using a while loop.

print the factorial.
'''

# Example input() statement
number = int(input('Please enter a number: '))

#Perform factorial
result = 1
while(number != 1):
    result = result * number
    number = number - 1

print(result)
