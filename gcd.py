'''
Find the Greatest Common Denominator (GCD) of two user inputted numbers.

Print the GCD of the numbers to the screen.
'''

# Example input() statement
number = int(input('Please enter a number: '))
number2 = int(input('Please enter a number: '))

if(number > number2):
    smallest = number2
else:
    smallest = number

for i in range(1, smallest+1):
    if(number % i == 0) and (number2 % i ==0):
        result = i
print(result)
