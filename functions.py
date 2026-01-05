''' Function '''

#   functions are block of codes which are executed when it is called

#   syntax

# def funtion_name(<arguments>):
#     .
#     .
#     body of function
#     code to be executed


''' main use of function 
    1.  reusability - dry cnocept
    2.  modularity'''

# def hello():
#     print('hello world!!!')
# # hello()

# a = hello
# a()


# a = print
# a('hello world')

''' arguments or parameters -> values to be passed to a function'''

# def add(a,b): # fromer arguments
#     print(a+b)

# add(3,4)  #   actual arguments


# def fullname(fname,mname,lname):
#     print(fname+' '+mname+' '+lname)

# fullname('christy','c','mathai')

#   stub    -> an empty function

''' Factorial using function '''

# def fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     print(fact)
# fact(5)


''' Calculator using function '''

# def calc(a,b):
#     print(f'sum={a+b}')
#     print(f'diff={a-b}')
#     print(f'mul={a*b}')
#     print(f'div={a/b}')
#     print(f'rem={a%b}')
# calc(10,5)

# def calc(a,b):
#     s = input('enter operation:')
#     if s == '+':
#         print(f'Sum={a+b}')
#     elif s == '-':
#         print(f'Sub={a-b}')
#     elif s == '*':
#         print(f'Product={a*b}')
#     elif s == '/':
#         print(f'Div={a/b}')
#     elif s == '%':
#         print(f'Rem={a%b}')
#     else:
#         print('error')
# calc(10,5)


''' types of arguments
    1. positional aruguments
    2. keyword arguments -> giving values while calling arguments'''

# def add(a=0,b=0):
#     print(a,b)
# add()

''' return sattement -> return assigns as the value of function'''

#   None is a value in python means null

# def add(a,b):
#     c = a+b
#     return c

# print(add(1,2))
# d = add(2,3) * 5
# print(d)


# def add(a,b):
#     c = a+b
#     return 'christy'

# print(add(1,2))


def sum(x,y):
    return x + y

def diff(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    return x / y


def main():
    while True: # runs in infinite loop
        x = int(input('enter first number:'))
        y = int(input('enter second number:'))
        ch = int(input('Operations:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit\n'))
        if ch == 1:
            print(sum(x,y))
        elif ch == 2:
            print(diff(x,y))
        elif ch == 3:
            print(mul(x,y))
        elif ch == 4:
            print(div(x,y))
        elif ch == 5:
            break
        else:
            print('Invalid input')
main()