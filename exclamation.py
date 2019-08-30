'''
If an exclamation mark is detected capitalize the whole string.
If not lowercase the whole string.

Print the new string based on the user inputted string.
'''

# Get the string
s = input('Please enter a string: ')

length = len(s)

#If exclamation point Uppercase all letters.
#Else lowercase entire string.
if(s[length - 1] == '!'):
    s = str.upper(s)
else:
    s = str.lower(s)
print(s)
