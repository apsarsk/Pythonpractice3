# file=open('myfile.txt','r+')
# st='sample data in file'
# data=file.read()
# file.seek(0,0)
# print(data)
# file.close()

# file=open('myfile.txt','w+')
# st='sample data in file'
# data=file.read()
# file.seek(0,0)
# file.close()

class Rectangle:
    count=1
    def __init__(self,l,b):
        self.l = l
        self.b=b
    # Rectangle.count +=1
    def area(self):
        return self.l*self.b
    def perimeter(self):
        return 2*(self.l*self.b)

    @classmethod
    def get_count(cls):
        return cls.count

print(Rectangle.get_count())



