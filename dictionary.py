''' Dictionary -> dict is a collection of datas and is a key value pairs'''

# dict = { key: value, key : value}
# has no index
# unique keys

# user = {'name':'christy','location':'thiruvalla','age':21}
# print(user)
# print(user['name'])
# print(user['age'])

# {} for empty pyhton consider this as dict

# a ={}
# print(type(a))

# a= {}
# a['name'] = 'christy'
# a['location'] = 'thiruvalla'
# a['age'] = 21
# a['name'] = 'christ'
# print(a)

''' restrictions 
    1. key should be unique
    2. key should be of type immutable -> not list dict'''


''' inbuilt method 
    1. dict.get('key') -> for getting key value
    2. dict.keys() -> list of keys are printed => these are not perfect list but can be converted to list by calling list(u.keys())
    3. dict.values() -> list of values in keys are printed 
    4. dict.items() -> prints a tuple of key-value pair'''


user = {'name':'christy','location':'thiruvalla','age':21}
# print(user.get('name'))
# print(user.keys())
# print(user.values())
# print(user.items())


# for i in user:
#     print(i)    #   prints keys

# for i in user:
#     print(user[i])  #   prints values
