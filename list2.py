# print a list of first 100 numbers

# a = []
# o = []
# e = []
# for i in range(1,101):
#     a.append(i)
#     if i % 2 == 0:
#         e.append(i)
#     else:
#         o.append(i)
# print(a)
# print(f'Even list: {e}\nOdd list: {o}')

''' Given a list check numbers in a list are positive, negative or zero'''

z = [3,5,6,-1,0,12,-6,-7]
# for i in range(0,len(z)):
#     if z[i] > 0:
#         print(f'{z[i]} positivie')
#     elif z[i] < 0:
#         print(f'{z[i]} negative')
#     else:
#         print('Zero')

# for i in z:
#     if i > 0:
#         print(f'{i} is positivie')
#     elif i < 0:
#         print(f'{i} is negative')
#     else:
#         print(f'{i} is Zero')

''' print without duplicates '''

# z = [1,2,3,3,2,1,1,2,3,4,5,6]
# m = []
# for i in z:
#     if i not in m:
#         m.append(i)
# print(m)

# for i in z:
#     if i in m:
#         continue
#     else:
#         m.append(i)
# print(m)


''' print largest and smallest element from list '''

# p = [100,0,-7,600,-10,-999]

# print(f'Max: {max(p)}')
# print(f'Min: {min(p)}')

# max = 0
# min = 0
# for i in p:
#     if i > max:
#         max = i
#     elif i < min:
#         min = i
# print(f'max:{max},min:{min}')

''' divide list in half '''

# c = [10,11,12,13,14,15,16,17,18,19,20]

# op = [10,11,12,13,14,15] [16,17,18,19,20]

# c1 = []
# c2 = []
# for i in range(0,len(c)):
#     if i < len(c)//2+1:
#         c1.append(c[i])
#     else:
#         c2.append(c[i])
# print(c1,c2)


''' sort list '''

# p = [100,0,-7,600,-10,-999]
# for i in range(0,len(p)):
#     for j in range(i,len(p)):   #range starts from 0 descending order and for i ascending order
#         if p[i] > p[j]:
#             temp = p[i]
#             p[i] = p[j]
#             p[j] = temp
# print(p)

# p.sort()
# print(p)