# t1=(1,2,3,4,5,6)
# t2=tuple([1,2,3,4,5,6])
# print(id(t1),id(t2))

# t3=()
# print(type(t3))
#
# t4=(3)
# print(type(t4))

# t1=(6,5,4,2,3,2)
# t1[2]=10

# tuple Comprehension
# t=(*(x for x in range(1,5)),)
# print(t)
# t1=tuple(x for x in range(1,5))
# print(t1)
#
# t2=tuple(x**2 for x in range(1,5))
# print(t2)

# t3=(*(x.lower() for x in 'PyThOn'),)
# print(t3)

# t4=(*(int(x) for x in '1234'),)
# print(t4)

# t1=(3,6,9,112,15,18,21)
# print(t1[3])
# print(t1[::2])

# packing and Unpacking
# t1=(1,2,3)
# t2=(4,5,6)
# t3=t1+t2
# print(t3)

# repetation
# t1=(1,2,3)
# print(t1*3)

# packing and unpacking
# t1=1,2,3,4,5
# print(t1)
t1=1,2,3,4,5
# a,b,c,d,e=t1
# print(a,b,c,d,e)
# a,b,*c=t1
# print(a)
# print(b)
# print(c)

*a,b,c=t1
print(a)