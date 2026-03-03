user_input = " Peri institute of technology "


# Get characters from input string
for char in user_input:
    print(f'char {char}')


# replace string/char in given input string
updated_str = user_input.replace(" ",";")
print(updated_str)


# str to list
li = updated_str.split(";")
print(li)


# li to str
updated_str = ' '.join(li)
print(updated_str)


# upper and lower
print(f'ToUppercase {updated_str.upper()}')
print(f'ToLowercase {updated_str.lower()}')
print(f'Title {updated_str.title()}')


# length of the string
len_str = len(updated_str)
print(f'Length of the updated str {len_str}')


# for instance, trying to access string characters from idx 5 to 14
print(f'Characters b/w 5 to 14 {updated_str[5:13]}')


# string reverse
print(f'Reversed string {updated_str[::-1]}')


for i in updated_str.split(' '):
    print(f'Reverse substring is {i[::-1]}')


# removing trail & rear space
print(updated_str.strip())


import sys


user_password = sys.argv[1] #TestUser
print(f'Entered user_password {user_password}')


upper_valid = False
lower_valid = False
if len(user_password) >= 8:
    for c in user_password:
        if c.isupper():
            upper_valid = True
        if c.islower():
            lower_valid = True
        if upper_valid and lower_valid:
            print('Password is valid')
            break
    if not upper_valid or not lower_valid:
        print('Invalid password')
else:
    print('Len is not valid')