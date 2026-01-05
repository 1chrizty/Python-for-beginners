# string is indexed
# positive indexing starts at zero ie 0 1 2 3 , meanwhile negative indexing starts from -(n) -(n-1) -(n-2) ...... -2 -1

# in index we can specific values as [start:stop:step], same as in for loop

a = 'christy c mathai'
# print(a[0]) => return char at index 0
# print(a[0:11]) => from index 0 to 11
# print(a[1:16:2]) => from index 1 to 16 by skipping a char
# print(a[:7]) => starts from 0th index to 7, if starting index value is not provided
# print(a[6:]) => starts from index 6 to last index, if stopping index value is not provided
# print(a[-17:-1]) => negative indexing, from -17th index to -1th index, not prints the last char of string

# for reverse a string
# a = input('enter a name:')
# print(a[::-1])


# string is iterable, looping based on index

# a = "christy c mathai"
# print(len(a))
# for i in a:
#     print(i,end='')
# for i in range(0,len(a)):
#     print(i)
# for i in range(0,len(a)):
#     print(a[i])


'''print vowels from a sentence'''

# a = input('Enter a sentence:')
# for i in range(0,len(a)):
    # if a[i] == 'a' or a[i] =='e' or a[i] == 'i' or a[i] == 'o' or a[i] == 'u' or a[i] == 'A' or a[i] =='E' or a[i] == 'I' or a[i] == 'O' or a[i] == 'U':
    #     print(a[i],f'at position {i}')
    # if a[i] in 'aeiouAEIOU':
    #     print(f'{a[i]} in position {i}')
    

# v = 'aeiouAEIOU' #=> SOLVED WITH STRING
# for i in range(0,len(a)):
#     if a[i] in vowels:
#         print(f'{a[i]} in position {i}')

# vowels = ['a','e','i','o','u','A','E','I','O','U'] #=> SOLVED USING LIST
# for i in range(0,len(a)):
#     if a[i] in vowels:
#         print(f'{a[i]} in position {i}')

'''Reverse of a string without using [::-1]'''

# a = input('Enter a string:')
# for i in range(len(a)-1,-1,-1):
#     print(a[i],end='')
# print('\t')

# rev = ''
# for i in range(len(a)-1,-1,-1):
#     rev += a[i]
# print(rev)

# rev = ''      #for pattern printing of reverse
# for i in range(len(a)-1,-1,-1):
#     rev += a[i]
#     print(rev)