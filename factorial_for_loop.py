'''
Find the factorial of a user inputted number.

print the factorial.
'''

# Example input() statement
number = int(input('Please enter a number: '))

result = 1
for i in range(1, number+1):
    result = result * i

print(result)
