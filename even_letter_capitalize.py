'''
Capitalize the even numbered letters in a string given by a user.

Print the new capitalized string.
'''

# Get the string
s = input('Please enter a string: ')

s = str.lower(s)
new_s = ''
new_s = new_s + s[0]

for i in range(1,len(s)):
    if(i % 2 == 1):
        letter = s[i]
        uppercase = str.upper(letter)
        new_s = new_s + uppercase
    else:
        letter = s[i]
        new_s = new_s + letter

print(new_s)
