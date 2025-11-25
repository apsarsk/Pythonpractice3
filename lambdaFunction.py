# def double(x):
#     return x * 2
# print((lambda x:x*2)(5))
#
# l1=[1,2,3,4,5,6,7,8,9]
# f=filter(lambda x:x%3==0,l1)
# print(list(f))

# l1=[1,2,3,4]
# l2=list(map(lambda x:-x,l1))
# print(l2)

# l1=[1,2,3,4,5,6,7,8,9,10]
# k=lambda x:x if x%2==0 else -x
# print(list(map(k,l1)))

# l1=[[4,2,'Six'],[1,4,'Five'],[2,2,'Four']]


# print(sorted(l1,key=lambda x:x[0]+x[1]))
# l1=[[4,2,'Six'],[1,4,'Five'],[2,2,'Four']]
# print(sorted(l1,key=lambda x:x[0]+x[1]))

# class Day:
#     def __init__(self):
#         self.days={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
#     def __call__(self, dayno):
#         return self.days[dayno]
#
# d=Day()
# print(d(6))

# class Day:
#     def __init__(self):
#         self.days={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
#
#     def __call__(self,dayno):
#         return self.days[dayno]
# d=Day()
# print(d(5))
