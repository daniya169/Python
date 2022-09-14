#raise
'''def add(a,b):
    return a+b

print(add(2,3))
print(add('2','7'))
print(add('2',7))
'''
def add(a,b):
    if (type(a) is int and type(b) is int):
        return a+b
    #return 'you have enter the worng datatype'
    raise TypeError ('you have enter the worng datatype')

print(add(2,3))
print(add(2,'7'))
