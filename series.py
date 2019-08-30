'''
Find the solution to the series A(i) = 2 * A(i-1) + 1.

Param
N: Find the Nth element of the series.

Return
Print the resulting Nth element of the series. 
'''

#Find solution to the series A(i) = 2 * A(i-1) + 1
number = int(input('Please enter a value for N: '))


if(number == 0):
    result = 2 * 0 + 1
else:
    i = 1
    result = 1
    while(i <= number):
        result = 2 * result + 1
        i = i + 1

# Use print() to print the result, like this:
print(result)
