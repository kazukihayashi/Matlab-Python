import numpy as np

def Show_Text(text):
    print('Input value is {0}'.format(text))

def Plus(a,b):
    return a+b

class TestClass():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def Multiply_Values(self):
        return self.a*self.b