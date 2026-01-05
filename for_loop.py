# for loop

# Syntax
# for item in range(0,10):
#     condition

# range(start,stop,step)

# for i in range(0,13,3):
#     print(i)

# for i in range(10,0,-1):          start will be default 0 if only stop is provided
#     print(i)                      step will be bydefault 1 if no value applied
# for decrementing


# even and odd numbers

# print('odd numbers')
# for i in range(1,101,2):
#     print(i,end =' ')
# print('\neven numbers')
# for j in range(2,101,2):
#     print(j,end = ' ')


# for i in range(1,101):
#     if i % 2 == 0:
#         print('even',i)
#     else:
#         print('odd',i)


'''multiplication table'''

# j = int(input('enter a number:'))
# for i in range(1,11):
#     print(f'{j}x{i}={j*i}')


'''factorial'''

# j = int(input('enter a number:'))
# fact = 1
# for i in range(1,j+1):
#     fact *= i
# print(fact)


'''prime or not'''

# num = int(input('enter a number:'))
# flag = 0
# if num == 1 or num == 0:
#     print('not prime')
# else:
#     for i in range(2,num//2):
#         if num % i == 0:
#             flag = 1
#             break
#     if flag == 0:
#         print('prime number')
#     else:
#         print('not prime')


'''armstrong number'''


num = int(input('enter a number:'))
temp = num
num1 = num
arm = 0
sum = 0
digit = 0
temp1 = 0
temp2 = 0
while num > 0:
    temp1 = num % 10
    digit += 1
    num //= 10
while num1 > 0:
    temp2 = num1 % 10
    arm = temp2**digit
    sum = sum + arm
    num1 = num1 // 10
if sum == temp:
    print('armstrong number')
else:
    print('not armstrong number')

