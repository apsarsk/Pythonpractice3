# d1={1:'one',2:'two',3:'three',4:'four'}
# print(d1[3])
# update
# d1[3]='tree'
# print(d1)
import uuid

# write
# d1[5]='five'
# print(d1)

# Traversing
# for i in d1:
#     print(i,d1[i])

# d1={1:3.5,2.5:True,(5+6j):'abc'}
d1={1:'one',2:'two',3:'three',4:'four'}
# print(type(d1))
# d=dict([(1,'one'),(2,'two'),(3,'three'),(4,'four')])
# print(type(d))

# l1=[1,2,3,4]
# l2=['one','two','three','four']
# d=dict(zip(l1,l2))
# print(type(d))

# enumerate function

# l1=['one','two','three','four']
# d=dict(enumerate(l1,start=1))
# print(d)

# Dictionary Comprehension
# d1={1:'one',2:'two',3:'three',4:'four'}
# l1=[(1,'one'),(2,'two'),(3,'three'),(4,'four')]
# d={x:y for x,y in l1 }
# print(d)

# l1=[1,2,3,4]
# l2=['one','two','three','four']
# d={x:y for x,y in zip(l1,l2)}
# print(d)

# l1=['one','two','three','four']

# d={x:y for x,y in enumerate(l2,start=1)}
# print(d)

d1={1:'one',2:'two',3:'three',4:'four'}
# print(d1.keys())
# print(d1.values())
# print(d1.items())

# for key in d1.keys():
#     print(key)

# for value in d1.values():
#     print(value)

# for x,y in d1.items():
#     print(x,y)

# print(d1.get(5,'Missing'))

# d1.setdefault(5,'undefined')
# print(d1)

# d2={5:'five'}
# d1.update(d2)
# print(d1)

# l1=[1,2,3,4]
# d=dict.fromkeys(l1,'unknown')
# print(d)

# d1.pop(2)
# print(d1)

d1.popitem()
print(d1)

d1.clear()
print(d1)

# Dynamic Key Generation
# uuid.uuid1()--current time and computer mac address
# uuid.uuid4()--psuedo-rnadom numbers
# uuid.uuid3() -- md5 algorithma
# uuid.uuid5() --sha algoritham
