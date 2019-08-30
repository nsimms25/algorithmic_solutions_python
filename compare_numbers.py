'''
Two numbers entered by the user to compare.

print a statement depending on the comparison.
"The first number is larger"
"The second number is larger"
"Thw two numbers are equal"
'''

# Example input() statement
number = int(input('Please enter a number: '))
number2 = int(input('Please enter a number: '))

if(number > number2):
    print('The first number is larger.')

if(number < number2):
    print('The second number is larger.')

if (number == number2):
    print('The two numbers are equal.')
