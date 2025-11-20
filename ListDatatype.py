# l1=[1,2,3,4,5,6]
# l2=[1.8,1.8,3.5,4.6,5.7]
# l3=['john','marry','anil']
# l2=list((3,5,7,9))
# print(l2)

# l3=list('abcde')
# print(l3)

l1=[1,2,3,4]
# l2=list('abcde')
# l3=list((1,2,3,4))
# print(l3)

# l1=[7,3.2,'John',True,5+6j]
# for i in l1:
#     print(i)

# l1[2]=15
# print(l1)
#
# l1.append(5)
# print(l1)
# l1.remove(5)
# print(l1)

# indexing for read
# l1=[3,6,9,12,15,18,21]
# print(l1[4])
# print(l1[::3])
# print(l1[::-1])
# print(l1[-3:-7:-1])

# l1=[1,2,3,4,5]
# l1[3]=10
# print(l1)

# l1[3]=[10,11]
# print(l1)

l1=[1,2,3,4,5]
# l1[0:0]=[10]
# l1[3:3]=[10]
# print(l1)

# l1[9:9]=[10]
# print(l1)

# l1[3:3]=[10,11,12]
# l1[1:4]=[10,11,12,13,14,15]
# print(l1)

# List concatenation&Repetation
# concatenation +
# repetation *
# membership in and not in
# list comparison
# <, <=, >, >=, == ,!=

l1=[1,2,3,4,5]
# l2=[8,9,10]
# l3=l1+l2
# print(l3)

# print(l1+[4])

# l1.extend([4,5,6])
# print(l1)

# print(l1*3)
# print(l1*2.5)

# print(5 in l1)
n_l1=[[1,2],[3,4],5]
# print([3,4] in n_l1)
# l1=['red','green','blue']
# for x in l1:
#     print(x)

# l1=[1,2,3]
# l2=[1,2,3]
# l3=[3,2,1]
# print(l3==l2)
# print(l3!=l2)

# l1=[1,2,3]
# l2=[1,2,3,4]
# l3=[1,2,1]
# print(l1>l2)
# print(l1>l3)

# l1=[2]
# l2=[1,2,3,4]
# l3=[1,2,1]
# print(l2>l3)

# list Traversing
l1=[5,6,7,8,9]
# for i in l1:
#     print(i)

# for i in range(len(l1)):
#     print(i,l1[i])

# for i in range(len(l1)):
#     print(l1[i])

# i=0
# while i<len(l1):
#     print(l1[i])
#     i+=1

# l1=[1,2,3,4,5]
# l1.append(6)
# l1.append(6,7)
# append will not more the one element
# print(l1)
l1=[1,2,3,4]
# l1.append(6)
# l1.append('python')
# l1.append([1,2])
# l1.append([1,2])
# l1[5:5]=[10]
# l1[len(l1):]=[5,6,7]
# l1=[1,2]

#extend
# l1.extend(range(5,8))
# print(l1)

# insert
# l1.insert(0,50)
# print(l1)

# insert at given index
# l1.insert(70,'python')
# print(l1)
# l1=[1,2,3,4]
# l1[2:2]=[55]
# print(l1)

# copy()
# l2=l1.copy()
# print(l1,l2)

# {'mon':8,'tue':7,'wed':8,'thu':8,'fri':9,'sat':9,'sun':9}

# hours=input("Enter Hours:")
# wags=int(input("Enter hourly wages :"))
# hours=hours.split()
# week_hours=[int(x) for x in hours]
# total_hours=sum(week_hours)
# if total_hours<=40:
#     total_wages=total_hours*wags
# else:
#     overtime=total_hours-40
#     total_wages=40*wags*overtime*wags*1.5
#     print("Total wages:",total_wages)

# Remove Duplicates
# l1=[3,5,7,9,6,2]
# n=int(input('Enter a number :'))
# print(l1[n:]+l1[:n])
# lst = [5, 4, 3, 3, 4, 5]
# # rev=lst[::-1]
# rev=list(reversed(lst))
# if lst==rev:
#     print('Palindrome')
# else:
#     print('Not Palindrome')

# l1=[1,2,3,4,5,6]
# del l1[1:4]
# print(l1)

# indexing and sorting
# print(l1.index(6,3,))
# print(l1.count(3))
# rev=l1.reverse()
# print(l1)

# l1.sort(reverse=True)
# print(l1)

# l2=[10,20,30,40,50,60]
# l2.sort(reverse=True)
# print(l2)

# ll=['coat','python','black','cat']
# ll.sort(reverse=False,key=len)
# print(ll)
#
# l1=['apple','Bat','cat','Dog']
# l1.sort(key=str.lower)
# print(l1)

import random as rd
lst=[6,2,5,3,1,4]
# print(rd.random())

# print(rd.randint(1,100))
# print(rd.randrange(1,10,2))
# for i in range(5):
#     print(rd.randint(1,100))

# l=['a','b',10,12,1.5,2.7,True]
# unique_vars = rd.sample(l, 1)

# print(unique_vars)

# import itertools as it
# lst=['A','B','C']
# per=it.permutations(lst,2)
# print(list(per))

# print(list(it.combinations(lst,2)))
# print(list(it.product([1,2,3],['A','B','C'])))

# import statistics as st
# ls=[6,8,4,9,3,10,8,11,5,7,8,4,2]
# median=st.median(ls)
# mean=st.mean(ls)
# mode=st.mode(ls)
# print('Median is :',median)
# print('Mean is :',mean)
# print('Mode is :',mode)

# list comprehesion
# l=[x for x in 'python']
# l3=[x.lower() for x in 'PyThON']
# print(l3)
# l4=[int(x) for x in '1234']
# print(l4)
# l5=[x for x in 'ab*cd7e' if x.isalpha()]
# print(l5)


# l1=[['Lux','soap',123],['Sunsilk','Shampoo',200],['CloseUp','ToothPaste',200],['Fair&lovely','Face cream',250]]
# for i in range(len(l1)):
#     print(l1[i])

# nums=[4,8,3,5,10,7,2,9,13,6]
# odd=[x for x in nums if x%2!=0]
# even=[i for i in nums if i%2==0]
# print(odd)
# print(even)

# find lonest number in Lost

# lst=[[1,2,3],[1,1,1,1,1],[2,2,3,3]]
# max_length=max(lst,key=len)
# print(max_length)




