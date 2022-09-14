#tell
#seek
f=open(r'D:\study\ML & DTAT A SCIENCE\test.txt')
print(f'Corsour position before: {f.tell()}')
print('\n')
print(f.read())
print('\n')
print(f'Corsour position After: {f.tell()}')
f.seek(30)

print(f'Corsour position before: {f.tell()}')
print('\n')
print(f.read())
print('\n')
print(f'Corsour position After: {f.tell()}')
f.close()
