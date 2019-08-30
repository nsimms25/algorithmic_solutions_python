'''
Find whether a number is prime or not using a for loop. 

Param
number: number to be tested

Return
print the string indicating whether or not the number is prime. 
'''

# Example input() statement
number = int(input('Please enter a number: '))

prime = True

if(number == 2):
    prime = True
for i in range(1,number):
    if(i != 1 and number % i == 0):
        prime = False

if(prime == True):
    print('The number you inputted is a prime number.')
if(prime == False):
    print('The number you inputted is not a prime number.')
