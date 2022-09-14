#lambda function

# lambda variable:operation

add=lambda a,b:a+b
print(add(2,3))


square=lambda a:a**2
print(square(5))

# map Function

#map(function, input)

num=[1,2,3,4,5]
def square(a):
    return a**2

print(list(map(square,num)))

print(list(map(lambda a:a**2  ,num)))
