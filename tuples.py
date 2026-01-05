''' Tuple -> collection of data ()'''

''' similarities 
    1. ordered
    2. duplicates allow
    3. indexed
    4. any element of size
    5. can be nested'''

''' tuples are immutable => no change in defined tuple '''

# a = (1,2,3,4,5,'ch')
# b = list(a)
# print(f'tuple:{a}\nlist:{b}')
# print(a[3])

''' set -> collection of unique data {}'''

# a = {1,2,3,4,5}
# print(a)
# print(type(a))

''' similarities => is iterable so loop can be used but not in range
    1. unordered
    2. unindexed
    3. no duplicate values allowed'''

# a = {1,2,3,4}
# b = {4,2,3,1}
# print(a == b)

# num = {'one','two','three','four','five'}
# for i in num:
#     print(i)


''' operations '''

# Union => a.union(b) or a | b
# Intersection => a.intersection(b) or a & b
# Difference => a - b

# a = {1,2,3,4,5}
# b = {4,5,6,7,8,9}

# print(a.union(b))
# print( a | b )

# print(a.intersection(b))
# print( a & b )

# print( a - b )
# print(b.difference(a))

