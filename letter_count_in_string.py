'''
Find a letter's appearance count in a user inputted string

Params:
string: s
string: l

Print the number of times l appears in s to the screen.
'''

# First get the string
s = input('Please enter a string: ')
# Then get the letter to count
l = input('Please enter a letter to count: ')

s = str.lower(s)
l = str.lower(l)

count = 0
for i in range(0,len(s)):
    if(s[i] == l):
        count = count + 1

print(count)
