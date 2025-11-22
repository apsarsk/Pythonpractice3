# def fun(n):
#     if n>0:
#         print(n)
#         fun(n-1)
#
# fun(5)

# factorial of numbers

def fact(n):
    if n<=0:
        return  1
    else:
        return n*fact(n-1)
print(fact(4))