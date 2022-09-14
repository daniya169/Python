#with open---> 'r'-->read, 'w'---> write, 'a'---> append
'''
with open('test.txt','r') as f:
    print(f.read())

with open('test.txt','w') as f:
    f.write('Hello student')

with open('test.txt','a') as f:
    f.write('\nIm chetan prakash')
'''

x=[]
y=[]

with open('test1.txt','r') as f:
    data=f.readlines()
    for col in data:
        x.append(col[0])
        y.append(col[2])

print(x)
print(y)
