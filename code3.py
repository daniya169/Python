#readline
#readlines
'''
f=open('test.txt')
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

'''
f=open('test.txt')
#print(f.readlines())
data=f.readlines()
for line in data:
    print(line)
f.close()
