'''
Zip the list based on even and odd numbers. 

Param
User entered list of numbers.

Return:
Print the list of zipped numbers.
'''

nums = input('''Please enter a series of numbers separated by commas. \n Hit enter when you are done. ''')

nums_list = nums.split(',')

new_list = [int(i) for i in nums_list]

odds = []
evens = []

for i in range(0,len(new_list)):
    if(i % 2 == 0):
        odds.append(new_list[i])
    if(i % 2 == 1):
        evens.append(new_list[i])

zipped = zip(odds, evens)
zipped_list = list(zipped)

print(zipped_list)
