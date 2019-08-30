'''
Find the divisor of a number inputted by user.

print the number that divides into user number.
'''

# Example input() statement
number = int(input('Please enter a number: '))

divisor = 1
while(divisor <= number):
    if(number % divisor == 0):
        print(divisor)
    divisor = divisor + 1
