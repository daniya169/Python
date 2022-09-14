user={'Name':'Chetan','age':31}
print(user)

# items method

if ('Chetan','Name') in user.items():
    print('Present')

else:
    print('Not Present')


# how to apply loops in dict

for i in user:
    print(i)

#Keys method
    
for i in user.keys():
    print(i)

#values Method

for i in user.values():
    print(i)


#items Methods
for i,j in user.items():
    print(f'{i}:{j}')

for i in user.items():
    print(i)
    






    




    
