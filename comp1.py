# comprehension command--->list
'''
num=list(range(1,11))
print(num)

new=[]
for i in num:
    new.append(i**2)

print(new)

Square=[i**2 for i in range(1,11)]

print(Square)
'''


num=list(range(1,11))
print(num)

new=[]
for i in num:
    if i%2==0:
        new.append(i**2)

    else:
        new.append(-i)

print(new)


square=[i**2 if i%2==0 else -i for i in range(1,11) ]
print(square)






