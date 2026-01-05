# a = input('Enter a string:')
# rev = ''      #for pattern printing of reverse
# for i in range(len(a)-1,-1,-1):
#     rev += a[i]
#     print(rev)

# normal string pattern printing

# a = input('Enter a string:')
# rev = ''
# for i in range(len(a)):
#     rev += a[i]
#     print(rev)

'''Pattern printing'''

# for i in range(1,6):
#     for j in range(1,6):
#         print(i,j)

'''Star printing'''

# for i in range(1,6):
#     for j in range(1,i+1):
#         print('*',end='')
#     print()

'''reverse printing'''

# for i in range(6,1,-1):
#     for j in range(1,i):
#         print('*',end='')
#     print()

# for i in range(1,6):
#     for j in range(5,i-1,-1):
#         print('*',end='')
#     print()

'''pyramid pattern'''

'''Chessboard pattern'''

# for i in range(1,9):
#     for j in range(1,9):
#         if (i == 1 or i == 3 or i == 5 or i == 7):
#             if j % 2 == 0:
#                 print('B',end=' ')
#             else:
#                 print('W',end=' ')
#         elif(i ==2 or i == 4 or i == 6 or i == 8):
#             if j % 2 == 0:
#                 print('W',end=' ')
#             else:
#                 print('B',end=' ')
#     print()


# for i in range(1,9):
#     for j in range(1,9):
#         if (i+j)%2 == 0:
#             print('W',end=' ')
#         else:
#             print('B',end=' ')
#     print()

'''Shape pattern'''

'''C'''

# for i in range(1,6):
#     for j in range(1,6):
#         if i == 1 or i == 5 or j == 1:
#             print('*',end='')
#         else:
#             print('',end='')
#     print()

'''S'''

# for i in range(1,6):
#     for j in range(1,6):
#         if i == 1 or i == 3 or i == 5:
#             print('*',end='')
#         elif i == 2 and j == 1:
#             print('*',end='')
#         elif i == 4 and j == 5:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print()


'''I'''

# for i in range(1,6):
#     for j in range(1,6):
#         if i == 1 or i == 5 or j == 3:
#             print('*',end='')
#         elif j < 3:
#             print(' ',end='')
#         else:
#             print('',end='')
#     print()

'''H'''

# for i in range(1,6):
#     for j in range(1,6):
#         if i == 3 or j == 1 or j ==5:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print()

'''Pyraimid'''


# row = int(input('Enter a value:'))
# for i in range(1, row + 1):
#     for j in range(row-i):
#         print(' ', end='')
#     for k in range(2 * i - 1):
#         print('*', end='')
#     print()


# row = 5
# for i in range(1, row + 1):
#     for j in range(row-i):
#         print(' ', end='')
#     for k in range(1,i+1):
#         print('* ', end='')
#     print()


# row = 5
# for i in range(1, row + 1):
#     for j in range(row-i):
#         print(' ', end='')
#     for k in range(1,i+1):
#         print('* ', end='')
#     print()
# for i in range(row,0,-1):
#     for j in range(row-i):
#         print(' ', end='')
#     for k in range(1,i+1):
#         print('* ', end='')
#     print()
# for i in range(1, row + 1):
#     for j in range(row-i):
#         print(' ', end='')
#     for k in range(1,i+1):
#         print('* ', end='')
#     print()