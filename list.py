'''List'''

# collection of elements / objects  [ ]

''' Properties '''      #=> values in list can be repeated
# 1. list is ordered
# 2. list can contain any object of any time
# 3. lists are indexed
# 4. lists are dynamic
# 5. lists are mutable
# 6. lists are nested

''' 1 '''
# a = [1,2,3,4]
# b = [3,4,1,2]
# print(a == b)

''' 2 '''
# a = [10,5.5,'christy',True,[1,2,3,4],3212]
# print(a)

''' 3 '''
# b = [10,11,12,13,14,15,16,17,18,19,20]
# print(b[0])
# print(b[0:6:2])
# print(b[::2])
# print(b[::-1])
# print(b[-1])        #=> starts from the end of list

# [start:stop:step]

''' 6 '''
# a = [10,5.5,['christy',True,[1,2,3],'python'],[1,2,3,4],3212]
# print(a[2][3])

# list can be nultiple indexed

''' 4 '''
# a = [1,2,3,4,5,6]
# a[2:4] = [100,200,300,400,500,600,700]
# print(a)

''' 5 '''

# mutable -> changable
# string -> immutable

# name = 'christy'      # string is immutable, cannot change values
# name[0] = 'd'
# print(name)

# a = [0,1,2,3,4,5,6]      # numbers in list are mutable, they can be changed
# a[0] = 999
# print(a)

# a = [0,1,2,3,4,5,6]
# append() -> adds an element to end of list
# a.append(100)
# print(a)

# extend([iterable]) -> string list
# a.extend('christy')
# print(a)

# insert(index,value)  -> to insert in a specific position
# a.insert(1,'christy')
# print(a)

# remove(element)
# a = [3,0,1,2,3,4,5,6]   # removes the element that comes first, if duplicate is present
# a.remove(3)
# print(a)

# pop() -> remove an element from end of a list
# pop(index)    -> removes element from particular index position
# a = [0,1,2,3,4,5,6]
# a.pop()
# # a.pop(0)
# print(a)

# name ='pythonjune'
# for i in range(len(name)):
#     print(i,name[i])

# z = [1,2,3,4,5,6,7,8,9]
# for i in range(len(z)):
#     print(i,z[i])