# s1={1,2,3,3,4,5}
# print(s1)

# s1={1}
# print(type(s1))

# s3={1,2.5,'Jack',True}
# print(s3)

# s2=set([1,2,3,4,5])
# print(s2)

# s3=set('Python')
# print(s3)

# s4={}
# s4=set()
# print(s4)

# s1={10,20,30,40,50}
# s1.add(60)
# print(s1)
# s1.add((1,2,3))
# print(s1)
# s1.remove(60)
# print(s1)
# s1.pop()
# print(s1)
#
a={1,2,3,5,7}
b={5,7,9,10,11}

# c=a&b
# # print(c)
# c=a|b
# print(c)

s1={1,2,3,5,7}
s2={5,7,9,10,11}
# s3=s1.intersection(s2)
# print(s3)

# s3=s1.union(s2)
# print(s3)

# s1.intersection_update(s2)
# print(s1)

# s3=s1.difference(s2)
# print(s3)

# s1.difference_update(s2)
# print(s1)

# s3=s1.symmetric_difference(s2)
# print(s3)

# s1.symmetric_difference_update(s2)
# print(s1)

# s3=s1|s2
# print(s3)

# s3=s1&s2
# print(s3)

# s1&=s2
# print(s1)
# s3=s1-s2
# print(s3)

# s1-=s2
# print(s1)

# s3=s1^s2
# print(s3)

# s1^=s2
# print(s1)

# print(dir(set))

# set comprehension
# s={x for x in range(1,5)}
# print(s)
# s3={x**2 for x in range(1,5)}
# print(s3)

# s={x.lower() for x in 'PhiLlIPNs'}
# print(s)

# words_set={'plea','medical','listen','leap','decimal','silent','pale','enlist'}
#
# result=set()
# for word1 in words_set:
#     for word2 in words_set:
#         if word1 !=word2 and sorted(word1) == sorted(word2):
#             pair=tuple(sorted((word1,word2)))
#             result.add(pair)
# for pair in result:
#     print(pair)