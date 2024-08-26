class fraction:
    def __init__(self, n, d):
        self.num = n
        self.den = d

    def __str__(self):
        return f"{self.num}/{self.den}"
    
    def __add__(self,other):
        temp_num = self.num * other.den + other.num* self.den
        temp_den = self.den*other.den
        return f"{temp_num}/{temp_den}"
    
    def __sub__(self, other):
        temp_num = self.num * other.den - other.num* self.den
        temp_den = self.den*other.den
        return f"{temp_num}/{temp_den}"
    
    def __mul__(self,other):
        temp_num = self.num* other.num
        temp_den = self.den* other.den
        return f"{temp_num}/{temp_den}"
    
    def __truediv__(self, other):
        temp_num = self.num *other.den
        temp_den = self.den * other.num
        return f"{temp_num}/{temp_den}"
'''
x = fraction(4,2)
print(x) ==>> <__main__.fraction object at 0x00000208BAD46C00>
it means that the python doesnot know how the object looks like

'''
x = fraction(4,2)
y = fraction(4,2)
print(x)
print(y)
print(x+y)
print(x-y)
print(x*y)
print(x/y)
