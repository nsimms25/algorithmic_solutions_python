'''
Find whether a number is prime or not using a while loop. 

Param
number: number to be tested

Return
print the string indicating whether or not the number is prime. 
'''

number = int(input('Please enter a number: '))

prime = True
i = 2
while(i < number):
    if(number % i == 0):
        prime = False
        break
    i = i + 1

if(prime == False):
    print('The number you inputted is not a prime number.')
else:
    print('The number you inputted is a prime number.')
