
def to_square(l):
    d={}
    for i in range(1,l+1):
        d[i]=i**2

    return d

print(to_square(10))


square={n:n**2 for n in range(1,11)}
print(square)
