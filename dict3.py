# how to apply function in dict

def to_square(l):
    d={}
    for i in range(1,l+1):
        d[i]=i**2

    return d

print(to_square(10))
