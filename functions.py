import re
import random

# def volume(length,breath,height):
#     vol=length*breath*height
#     return vol
#
# v=volume(10,5,3)
# print(v)

# v=volume(10,10,height=10)
# print(v)

# l1=[10,20,30,40,20,50,20]
# l=l1.index(20)
# l2=l1.index(20,2)
# print(l1)

# def volume(l=1,b=1,h=1):
#     v= l*b*h
#     return v
#
# v=volume()
# print(v)

# def fun(a,b,/,c,d):
#     print(a,b,c,d)
#
# fun(1,2,3,4)

# def fun(*,a,b,c,d):
#     print(a,b,c,d)
#
# fun(a=10,b=5,c=5,d=6)

# def max3(a,b,c):
#     ma=max(a,b,c)
#     return ma
# print(max3(1,2,3))

# def intrest(*,p,t,r):
#     si=p*t*r/100
#     return si
# print(intrest(p=400000,t=120,r=15))
# phrase='The quick brown fox jumps over the lazy dog'
# def panagram(phrase):
#     letters=re.sub(r'[^a-zA-Z]','',phrase)
#     letter_set=set(letters.lower())
#     if len(letter_set)==26:
#         return True
#     else:
#         return False
#
# print(panagram(phrase))

# variable length
# def fun(*args):
#     print(args)
#
# fun(2,10,5)

# def fun(a,b,c):
#     sum=a+b+c
#     prod=a*b*c
#     return sum,prod
#
# f=fun(2,3,4)
# print(f)

# def result(m1,m2,m3):
#     total=m1+m2+m3
#     avg=total/3
#     if avg>40:
#         grade='Pass'
#     else:
#         grade='Fail'
#     return total,avg,grade
# print(result(40,44,54))

# def unique_list(*args):
#     num=set(args)
#     return list(num)
#
# print('Enter num separated by spaces:')
# num=input('')
# unique_li=unique_list(*numbers)
# print('\n unique Numbers :')
# print(unique_li)

# Iterator,Generator & Recursion
# Iterators & Generators
l1=[5,6,10,11,15]

# for i in l1:
#     print(i)

# iter()
# next()

# l1=[5,6,7]
# it=iter(l1)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# t=(1,2,3,4)
# t1=iter(t)
# print(next(t1))

# s={3,4,5}
# s1=iter(s)
# print(next(s1))

# d1={1:'one',2:'two',3:'three',4:'four'}
# d=iter(d1)
# print(next(d))

# s='hello'
# s1=iter(s)
# print(next(s1))

# r=range(3,10)
# it=iter(l1)
# print(next(it))

# def myrange(n):
#     i=0
#     while i<n:
#         yield i
#         i=i+1
#
#
# m=myrange(4)
# print(next(m))
# print(next(m))