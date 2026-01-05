''' OOPS -> object oriented programming'''

# object = real world entity
# has 2 things -> attributes and behaviour

# attributes (variables) -> used to define an object
# behaviour (functions) -> functionalities of an object


''' CLASS '''
# blueprint to create an object

# class Pen:
#     def write():
#         print('writing')
#     def draw():
#         print('drawing')
# pen1 = Pen
# pen1.write()
# pen1.draw()
# pen2 = Pen
# pen2.write()
# pen2.draw()


# constructor -> is a method used to initialize an object
#   __init__()

# class Car:
#     def __init__(self): #   is automatically called whenever an object is created
#         # print('car is created')
#         self.name = 'swift'
#         self.color = 'grey'
#     def start(self):
#         print('car has started')
#     def stop(self):
#         print('car stopped')
# c1 = Car()
# print(c1.name,c1.color)

# class Lap:
#     def __init__(self):
#         self.brand = 'macBook'
#         self.color = 'grey'
#     def game(self):
#         print('gaming')
#     def code(self):
#         print('coding')
# lap1 = Lap()
# print(lap1.brand,lap1.color)
# lap1.game()
# lap1.code()


# class Car:
        #   points to current object
#     def __init__(self,n,c):
#         self.brand = n
#         self.color = c
#     def start(self):
#         print(f'{self.brand} has started')
#     def stop(self):
#         print(f'{self.brand} has stopped')
# car1 = Car('lamborghini','olive green')
# print(car1.brand)
# car1.start()
# car1.stop()
# car2 = Car('porsche','velvet red')
# print(car2.brand)
# car2.start()
# car2.stop()


''' create a student class with attributes->name,mark1,m2,m3,m4,m5 and behaviour->total(),average(),percentage(),details()'''
# class Stud:
#     def __init__(self,n,m1,m2,m3,m4,m5):
#         self.name = n
#         self.mark1 = m1
#         self.mark2 = m2
#         self.mark3 = m3
#         self.mark4 = m4
#         self.mark5 = m5
#     def total(self):
#         self.sum1 = self.mark1 + self.mark2 + self.mark3 + self.mark4 + self.mark5
#         print(f'Total mark->{self.sum1}')
#     def average(self):
#         self.avg = self.sum1 / 5
#         print(f'Average mark->{self.avg}')
#     def percentage(self):
#         self.per = (self.sum1/250) * 100
#         print(f'Percenatage->{self.per}')
#     def details(self):
#         print(f'Name:{self.name}')
#         print(f'Total Mark:{self.sum1}')
#         print(f'Average mark:{self.avg}')
#         print(f'Percenatage:{self.per}')
# stud1 = Stud('Christy',44,45,46,47,48)
# print(stud1.name)
# stud1.total()
# stud1.average()
# stud1.percentage()
# stud1.details()


class Stud:
    def __init__(self,n,m1,m2,m3,m4,m5):
        self.name = n
        self.mark1 = m1
        self.mark2 = m2
        self.mark3 = m3
        self.mark4 = m4
        self.mark5 = m5
    def total(self):
        sum1 = self.mark1 + self.mark2 + self.mark3 + self.mark4 + self.mark5
        return sum1
    def average(self):
        avg = self.total() / 5
        return avg
    def percentage(self):
        per = (self.total() / 250) * 100
        return per
    def details(self):
        print(f'Student {self.name} has secured a score of {self.total()} out of 250 at an average of {self.average()} with {self.percentage()} percentile.')
stud1 = Stud('Christy',44,45,46,47,48)
stud1.total()
stud1.average()
stud1.percentage()
stud1.details()