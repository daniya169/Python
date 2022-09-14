#dictionary--->unordered database
# all type of data
#data--> key:value
# dict is denoted by--->{}

user={'name':'Chetan','age':31}
print(user)
print(type(user))

user1=dict(name='Chetan',age=31)
print(user1)
print(type(user1))

user_info={
        'name':'chetan',
        'age':31
    }
print(user_info)
print(type(user_info))


# how to add data to dict

d={}

d['Name']='Chetan'
d['age']=31
print(d)


# how to apply if and else in dict

user1={'Name':'chetan','age':31}
'''
if 'Name' in user1:
    print('Present')

else:
    print('Not Present')
'''


#values method
if 'chetan' in user1.values():
    print('Present')

else:
    print('Not Present')









