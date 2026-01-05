''' POLYMORPHISM 
    poly - many
    morph - forms
    
    1. duck typing
    2. operator overloading
    3. method overloading
    4. method overriding'''

''' duck typing '''
# class Chicken:
#     def __init__(self) # -> magic functions:
#         pass
#     def walks(self):
#         print('Chicken walks!!')
#     def fly(self):
#         print('Chicken tries to flys')
# class Duck:
#     def __init__(self):
#         pass
#     def walks(self):
#         print('Duck walks..')
#     def quacks(self):
#         print('Quack quack')
# class Farmer:
#     def __init__(self):
#         pass
#     def cook(self,bird):
#         bird.walks()
#         bird.quacks()

# c = Chicken()
# d = Duck()
# f = Farmer()
# f.cook(d)

''' Operator Overloading '''

# class Stud:
#     def __init__(self,name,m1,m2):
#         self.name = name
#         self.m1 = m1
#         self.m2 = m2
#     def __add__(self,next):   #   these are methods
#         return (self.m1+self.m2,next.m1+next.m2)
#     def __mul__(self,next):
#         return (self.m1*self.m2,next.m1*next.m2)
#     def __sub__(self,next):
#         return (self.m1-self.m2,next.m1-next.m2)
#     def __truediv__(self,next):
#         return (self.m1/self.m2,next.m1/next.m2)
#     def __gt__(self,next):
#         return (self.m1>self.m2,next.m1>next.m2)
#     def __str__(self):
#         return self.name
# s1 = Stud('Christy',2,3)
# s2 = Stud('Mathai',4,5)
# print(s1+s2)
# print(s1-s2)
# print(s1*s2)
# print(s1/s2)
# print(s1>s2)
# print(s1,s2)


''' Method Overloading -> not in python'''

# class A:
#     def run(a,b):
#         print(a,b)
#     def run(x,y,z):
#         print(x,y,z)
# a = A
# a.run(2,3,4)
# a.run(1,2)

# name of methods are same but number of arguments are different

''' Method Overriding '''

# class A:
#     def hello():
#         print('A  helloooo!!')
# class B(A):
#     def hellos():
#         print('B  haiiii!!')
# b = B
# b.hello()
# b.hellos()


# multiple class will be there, child can inherit properties of parent and returns if when needed