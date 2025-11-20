# x=65
#
# for i in range(0,127):
#     char=chr(i)
#     print(char)
#     print(ord(char))
import sys

# print(dir(''))
print(ord('A'))

#escape sequence
# print('\N{dollar sign}')
# print('\N{grinning face}')

# print('Hello World',sep='',end='\n',file=sys.stdout,flush=False)

# item='memory'
# size=32
# price=11.75
# print('cost of %d GB %s is $%f'%(size,item,price))

# formatted printing in python
name='Raj'
roll=10
avg=78.5

# print('{0:5}...{1}....{2}'.format(name,roll,avg))

item='memory'
size=32
price=11.75

print(f'{size} GB { item : ^10} in ${price}')