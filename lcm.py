'''
Find the Lowest Common Multiple (LCM) of two user inputted numbers.

Print the result to the screen.
'''

# Example input() statement
number = int(input('Please enter a number: '))
number2 = int(input('Please enter a number: '))

#find greater number
if(number > number2):
    greatest = number
if(number2 > number):
    greatest = number2
while(True):
    if(greatest % number == 0) and (greatest % number2 == 0):
        result = greatest
        break
    greatest = greatest + 1
print(result)
