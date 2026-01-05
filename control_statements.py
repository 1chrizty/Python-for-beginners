'''while loop'''

# a = 1
# while a <= 10:
#     print(a)
#     a = a + 1

# a = 1
# sum = 0
# num = int(input("Enter a number:"))
# while a < num+1:
#     sum += a 
#     a += 1
# print(f'Sum of first {num} natural numbers = {sum}')


# sum of odd and even numbers sum in first 1000 numbers

# sum_odd = 0
# sum_even = 0
# num = 1
# while num < 1001:
#     if num % 2 == 0:
#         sum_even = sum_even + num
#     else:
#         sum_odd = sum_odd + num
#     num = num + 1
# print(f'Sum of odd numbers is {sum_odd} and Sum of even numbers is {sum_even}')


# Factorial of a number

# num = int(input('Enter a number:'))
# fact = 1
# i = 1
# while i <= num:
#     fact = fact * i
#     i += 1
# print(f'Factorial of {num} is {fact}')


# sum of digits of numbers

# num = int(input('Enter a number:'))
# sum = 0
# digit = 0
# while num > 0:
#     digit = num % 10
#     sum += digit
#     num //= 10
# print(sum)


# reverse of a number

# num = int(input('Enter a number:'))
# num1 = num
# rev = 0
# temp = 0
# while num > 0:
#     temp = num % 10
#     rev = (rev * 10) + temp
#     num //= 10
# print(f'Reverse of {num1} is {rev}')


# Fibonocci series

count = int(input('Enter a number:'))
a = 0
b = 1
i = 0
while i < count:
    print(a, end=' ')
    a, b = b, a + b
    i += 1

