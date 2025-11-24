# show=print
# show('Hello')

# def outer():
#     def inner():
#         print('Inner function')
#     inner()
# outer()

# def total_area(l,b,h):
#     def area(d1,d2):
#         return d1*d2
#     return 2*(area(l,b)+area(b,h)+area(l,h))
# print(total_area(1,2,3))

# function as parameter
def add(a,b):
    return a+b
def sub(a,b):
    return a-b

def arithmetic(f,x,y):
    return f(x,y)
#
add=arithmetic(add,2,3)
sub=arithmetic(sub,2,3)
print(add,sub)

# def outer():
#     def inner():
#         print('Welcome')
#     return inner()
# ou=outer()
# ou

# closer function
# def outer(msg):
#     # msg='Hello World'
#     def inner():
#         print('+'*10)
#         print(msg)
#         print('+'*10)
#     return inner()
#
# ou=outer('Hello World')
# ou


def get_counter():
    count=0

    def counter():
        nonlocal count
        count +=1
        return count
    return  counter

d1=get_counter()
d2=get_counter()
d3=get_counter()

print(d1(),d2(),d3())
print(d1(),d2(),d3())
print(d1(),d2(),d3())

# # Decorator function
# def outer(s):
#     def inner():
#         print('*'*10)
#         s()
#         print('+'*10)
#     return inner
# @outer
# def display():
#     print('Welcome')
#
# display()


def outer(f):
    def inner():
        print('*'*10)
        f()
        print('+'*10)
    return inner

@outer
def display():
    print('Hey Python!')

display()


        