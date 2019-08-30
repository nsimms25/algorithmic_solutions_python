'''
Remove vowels from a user inputted string. 

Param:
User inputted string.

Return
Print the new string.
'''

# Get the string
s = input('Please enter a string: ')

vowels = 'aeiou'

s = s.replace('a','')
s = s.replace('e','')
s = s.replace('i','')
s = s.replace('o','')
s = s.replace('u','')

print(s)
