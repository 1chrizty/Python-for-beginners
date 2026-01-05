''' Inheritance '''

''' Single level
    multi level
    multiple level'''

''' single level inheritance '''

# class Person1:  # parent / super class
#     def __init__(self):
#         print('person1')
#     def read(self):
#         print('person can read')
#     def write(self):
#         print('person can write')
# class Person2(Person1): # child class
#     def __init__(self):
#         pass
#     def jump(self):
#         print('person can jump')
#     def walk(self):
#         print('person can walk')
# p1 = Person1()
# p2 = Person2()
# p1.read()
# p2.read()
# p2.jump()

''' multi level inheritance '''

# class Person1:
#     def __init__(self):
#         print('person1')
#     def read(self):
#         print('person can read')
#     def write(self):
#         print('person can write')
# class Person2(Person1):
#     def __init__(self):
#         pass
#     def jump(self):
#         print('person can jump')
#     def walk(self):
#         print('person can walk')
# class Person3(Person2):
#     def __init__(self):
#         pass
#     def fly(self):
#         print('person can fly')
#     def swim(self):
#         print('person can swim')
# class Person4(Person3):
#     def __init__(self):
#         pass
#     def sleep(self):
#         print('person can sleep')
#     def speak(self):
#         print('person can speak')
# p1 = Person1()
# p2 = Person2()
# p3 =Person3()
# p4 = Person4()
# p4.fly()
# p4.read()
# p2.read()


''' super class for immediate upper class calling'''

# class Person1:
#     def __init__(self):
#         print('person1')
#     def read(self):
#         print('person can read')
#     def write(self):
#         print('person can write')
#     def communication(self):
#         print('person 1 can communicate')
# class Person2(Person1):
#     def __init__(self):
#         pass
#     def jump(self):
#         print('person can jump')
#     def walk(self):
#         print('person can walk')
#     def communication(self):
#         print('person 2 can communicate')
# class Person3(Person2):
#     def __init__(self):
#         pass
#     def fly(self):
#         print('person can fly')
#     def swim(self):
#         print('person can swim')
#     def communication(self):
#         print('person 3 can communicate')
# class Person4(Person3):
#     def __init__(self):
#         pass
#     def sleep(self):
#         print('person can sleep')
#     def speak(self):
#         print('person can speak')
#     def communication(self):
#         print('person 4 can communicate')
#         super().communication()
# p1 = Person1()
# p2 = Person2()
# p3 =Person3()
# p4 = Person4()
# p4.communication()

''' Multiple inheritance '''

class Person1:
    def __init__(self):
        print('person1')
    def read(self):
        print('person can read')
    def write(self):
        print('person can write')
    def communication(self):
        print('person 1 can communicate')
class Person2:
    def __init__(self):
        pass
    def jump(self):
        print('person can jump')
    def walk(self):
        print('person can walk')
    def communication(self):
        print('person 2 can communicate')
class Person3:
    def __init__(self):
        pass
    def fly(self):
        print('person can fly')
    def swim(self):
        print('person can swim')
    def communication(self):
        print('person 3 can communicate')
class Person4(Person1,Person2,Person3): #   MRO -> method resolution order
    def __init__(self):
        pass
    def sleep(self):
        print('person can sleep')
    def speak(self):
        print('person can speak')

p4 = Person4()
p4.communication()