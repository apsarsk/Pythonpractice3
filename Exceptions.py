# a=10
# b=0
# c=a//b
# print(c)

# a=10
# b='x'
# c=a//b
# print(c)

# l1=[3,6,9,12,15]
# print(l1[10])

# d={1:'one',2:'two',3:'three',4:'four'}
# print(d[5])

# a,b=5,0
# try:
#     c=a//b
#     print(c)
# except:
#     print('b not give to 0')
# print('End of Programe')

# l=[10,20,30,40,50]
# try:
#     index=9
#     print(l[index])
# except:
#     print('Index Out of Range Error')
# print('End of Program')

# multiple exceptions
# l=[10,20,30,40,50]
# try:
#     index=''
#     print(l[index])
# except (IndexError,TypeError) as e:
#     print(e)

# a=10
# b=5
# try:
#     c=a//b
# except:
#     print('b Should not be 0')
# else:
#     print(c)

# def fun():
#     try:
#         x=int('256')
#         return x
#     except Exception as e:
#         print(e)
#         print('End of function')
#     finally:
#         print('End of function')
#
# f=fun()
# print(f)

# class NegtiveError(Exception):
#     pass
#
# def area(length,width):
#     if length>=0 and width>0:
#         a= length*width
#         return a
#     else:
#         raise NegtiveError('-Ve Dimension')
#
# a=area(-10,9)
# print(a)

def validate_age(age):
    if age>18 and age<60:
        return True
    else:
        raise InvalidError("age must be between 18 and 60")
class InvalidError(Exception):
    pass

v=validate_age(17)
print(v)