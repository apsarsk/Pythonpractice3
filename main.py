# for i in range(10,5,-1):
#     print(i)
# from curses.ascii import isalpha

# s1='python'
# for x in s1:
#     print(x)

# n=6
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print("Sum:",sum)

# n=4
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print('Sum:',sum)

# n=5
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print('Fact of n :',fact)

# n=5
# fact=1
# for i in range(1,n+1):
#     fact=fact *i
# print('Fact of n :',fact)

# n=4
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print('Fact of N :',fact)

# n= int(input('Enter a Number:'))
# a=0
# b=1
# for i in range(0,n):
#     c=a+b
#     a=b
#     b=c
# print(a)

# n=6
# a=0
# b=1
# for i in range(0,n):
#     c=a+b
#     a=b
#     b=c
# print(a)

# n=int(input("Enter a number"))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

# n= int(input('Enter a number:'))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

# n= int(input("Enter a number: "))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count=count+1
# if count==2:
#     print('Prime')
# else:
#     print('Not prime')

# n=int(input("Enter a number :"))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count=count+1
# if count==2:
#     print('Prime')
# else:
#     print('Not prime')
#
# n= int(input('Enter a Number :'))
# sum=0
# for i in range(1,n+1):
#     if n%i==0:
#         sum=sum+1
# if sum==2:
#     print('Prime Number')
# else:
#     print('Not Prime Number')

# for i in range(1,4):
#     for j in range(1,4):
#         print(i,'-',j)

# for i in range(1,4):
#     for j in range(1,4):
#         print(i,',',j,end='')
#     print('')
# n=5
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count=count+1
# if count==2:
#     print(n)

# for n in range(1,101):
#     count=0
#     for i in range(1,n+1):
#         if n%i==0:
#             count+=1
#     if count== 2:
#         print(n)

# for n in range(1,101):
#     count=0
#     for i in range(1,n+1):
#         if n%i==0:
#             count+=1
#     if count==2:
#         print(n)

# for i in range(1,6):
#     for j in range(1,6):
#         if i>=j:
#             print('*',end='')
#     print('')


# for i in range(1,6):
#     for j in range(1,6):
#         if i>=j:
#             print('*',end='')
#     print('')

# for i in range(1,6):
#     for j in range(1,6):
#         if i>=j:
#             print('*',end='')
#     print('')

# for i in range(1,6):
#     for j in range(1,i+1):
#         print('*',end="")
#     print('')

# for i in range(1,6):
#     for j in range(1,6-(i-1)):
#         print('*',end='')
#     print('')

# for i in range(1,6):
#     print('*'*(6-i))

# for i in range(1,6):
#     print('*'*(6-i))

# for i in range(1,6):
#     print(''*(i-1))
#     print('*'*(5-(i-1)))

# for i in range(1,6):
#     print(''*(i-1))
#     print('*'*(5-(i-1)))

# for i in range(1,6):
#     print('*'*(6-i))

# for i in range(1,6):
#     print(''*(i-1))
#     print('*'*(5-(i-1)))

# dayNo=int(input("Enter day number: "))
# if dayNo==0:
#     print('Monday')
# elif dayNo==1:
#     print('Tuesday')
# elif dayNo==2:
#     print('Wednesday')
# elif dayNo==3:
#     print('Thursday')
# elif dayNo==4:
#     print('Friday')
# elif dayNo==5:
#     print('Saturday')
# elif dayNo==6:
#     print('Sunday')
# else:
#     print('Invalid Day Number')

# dayNo=int(input("Enter day number: "))
# match dayNo:
#     case 0:
#         print("Monday")
#     case 1:
#         print("Tuesday")
#     case 2:
#         print("Wednesday")
#     case 3:
#         print("Thursday")
#     case 4:
#         print("Friday")
#     case 5:
#         print("Saturday")
#     case 6:
#         print("Sunday")

# dayNo=int(input('Enter a Number :'))
# match dayNo:
#     case 0:
#         print('Sunday')
#     case 1:
#         print('Monday')
#     case 2:
#         print('Tuesday')
#     case 3:
#         print('Wednesday')
#     case 4:
#         print('Thursday')
#     case 5:
#         print('Friday')
#     case 6:
#         print('Saturday')
#     case _:
#         print('Invalid Input')

# s1='Hello'

# for x in s1:
#     print(x)

# for x in range(len(s1)):
#     print(s1[x])

# s1='Hello'
# s2="Hello"
# s3='''Hello'''
# s4="""Hello"""
# s5="""Hello
#         world !"""
# s6='Clark"s'
# s7="Clark's"
#
# print(s1)
# print(s2)
# print(s3)
# print(s4)
# print(s5)
# print(s6)

# s1='Hello World'
# # s1[0]='m'
# # print(s1)
#
# print(s1[0:11:2])
# print(s1[8:2:-1])
# print(s1[3:7])
# print(s1[-8:-4])
# print(s1[2:7:2])
# print(s1[::-1])

# s1='Wel'
# s2='Come'
# s3=s1+s2
# print(s3)
# s1='x'
# s2=s1*10
# print(s2)

# s1='abcdef'
# print('z' not in s1)

# print('Python'<'apple')
#
# s1="apsar@gmail.com"

# x=s1.strip('&#$%^*')
# print(s1.replace('gmail','yahoo'))
#
# s1='xyz'
# s2='abc'
# print(s1.join(s2))
#
# s3='john-smith-Ajay-khan-james'
# print(s3.split('-',3))

# s1='Rossum@gmail.com'
# print(s1.startswith('Rossum'))
# print(s1.removeprefix('Ros'))
# print(s1.removesuffix('@gmail.com'))

# s1='python is easy'
#
# s2=s1.rpartition('s')
# print(s2)

# case conversion
# s1='\n\v\r'
# print(s1.capitalize())
# print(s1.upper())
# print(s1.swapcase())
# print(s1.casefold())
# print(s1.title())

# Inquiry methods
# s1='7\u20823\u2075'
# s1='-71.23AB'
# x=s1.isprintable()
# x=s1.isdigit()
# x=s1.isdecimal()
# print(x)

# print(help("".split))

# s='\u0969\u096A\u096B'
# print(s)

# s='37542'
# print(s.isnumeric())

# s='\u00BE\u215E'
# print(s.isnumeric())
# s='\x00-\x7f'
# print(s.isascii())





