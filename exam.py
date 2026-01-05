''' 2x2 matrix addition '''

# a = [[1,2],[3,4]]
# b = [[1,2],[3,4]]
# c = [[0,0],[0,0]]
# c[0][0] = a[0][0] + b[0][0]
# c[0][1] = a[0][1] + b[0][1]
# c[1][0] = a[1][0] + b[1][0]
# c[1][1] = a[1][1] + b[1][1]
# print(c)


# a = [[1,2],[3,4]]
# b = [[1,2],[3,4]]
# c = [[0,0],[0,0]]
# for i in range(2):
#     for j in range(2):
#         c[i][j] = a[i][j] + b[i][j]
# print(c)

''' anagram '''

# a = input('enter 1st string:')
# b = input('enter 2nd string:')
# a1 = {''}
# b1 = {''}
# if len(a) == len(b):
#     for i in a:
#         a1.add(i)
#     for j in b:
#         b1.add(j)
#     if a1 == b1:
#         print('Is an anagram')
#     else:
#         print('Not an anagram')
# else:
#     print('Not an anagram')


''' second largest num '''
# a = [1,1,1,3,3,3]
# temp = max(a)
# second = 0
# for i in a:
#     if i > second and i != temp:
#         second = i
# print(second)

''' white space '''
a = input('enter string:')
temp =''
for i in a:
    if a[i] != ' ':
        temp += a[i]
print(temp)



''' pattern printing '''

# row = int(input('Enter a value:'))
# for i in range(1, row + 1):
#     for j in range(row-i):
#         print(' ', end='')
#     for k in range(2 * i - 1):
#         print(i, end='')
#     print()
