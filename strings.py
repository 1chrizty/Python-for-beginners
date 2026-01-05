'''escape sequence'''

# \   - ' -
# \n  - new line
# \b  - backspace
# \t  - tab space
# \\  - consider as a single slash when any unwanted escape sequence popup
# r   - infront of string, make the string a raw string without considering the escape sequence


# a = 'hari\'s resume'        -- \ is used to determine the string has a quote
# print(a)

# b = 'gandhi once said that \"say no to violence"'
# b = 'gandhi once said that \n"say no to violence"'
# b = 'gandhi once said that \b"say no to violence"'
# b = 'gandhi once said that \t"say no to violence"'
# b = r'gandhi once said that \t"say no to violence"'
# print(b)

# string formatting

# name = input('Name:')         -- for string direct input function is only needed
# age = int(input('Age:'))
# rating = float(input('Rating:'))
# married_status = int(input('Status:'))

# print(f'My name is {name}, am {age} years old, has a rating of {rating} and married status is {bool(married_status)}.')


''''type casting / type conversion'''

# python is a dynamically typed language whereas C is a statically typed language
# statically - determines the type of variable before running
# dynamically - not determinig the vaiable type

'''2 types'''

# implicit & explicit

# a = '8'
# b = 6
# c = True
# print(int(a)+b)
# print(int(c),c)



'''string multiplication'''

# a = 'hello'
# b = 3
# print(a * b)


'''in operator for string     --   membership'''

# name = 'christy'
# print('ch' in name) -- if correct substring is present retur True, else False


# boolean value of empty string is False, 
# otherwise blankspace or anyother symbols conisders as a character and returns True
# name = ' '
# print(bool(name))
# name = ''
# print(bool(name))


'''input function'''

# a = input('Name:')
# b = int(input('Enter a number:'))
# c = int(input('Enter a number:'))
# print(a)
# print(b+c)

''' sum and average of n numbers'''

# count = int(input('Enter count:'))
# i = 0
# sum = 0
# avg = 0
# for i in range(1,count+1):
#     a = int(input(f'Enter number {i}:'))
#     sum += a
# avg = sum / count
# print(f'Sum = {sum} \nAverage = {avg}')