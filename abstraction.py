''' Abstraction '''

# inheritance
# base class (abstract class)

# child should override it
# abstractmethod is a decorator -> function which enhances other function

# from abc import ABC,abstractmethod
# class Animal(ABC):  #abstract class/base class
#     def __init__(self):
#         pass

#     @abstractmethod
#     def sound(self):
#         print('animal makes sound')

# class Dog(Animal):  #derived class/child class
#     def __init__(self):
#         pass
#     def sound(self):
#         print('woof wooff')
    
# d = Dog()
# d.sound()


# turtle & pygame for snake game

''' Access modifiers  Same_class    Same_package    Sub_class   Other_packages
    public              Y               Y               Y           Y
    protected           Y               Y               Y           N
    private             Y               N               N           N   '''

# class Student:
#     def __init__(self,name,m1,m2):
#         self.name = name    #public
#         self._m1 = m1   #protected
#         self.__m2 = m2  #private
#     def total(self):
#         self.tol = self._m1 + self.__m2
#         return self.tol
# s1 = Student('christy',10,9)
# print(s1._m1)