#decorator--> enance the functionlity of other function
#@
def decorator(any_function):
    def wrapper():
        print('Im calling main function')
        any_function()
    return wrapper


# 'Im calling main function'
@decorator
def func1():
    print('This is function 1')

func1()

# 'Im calling main function'
@decorator
def func2():
    print('This is fuction 2')

func2()

#var=decorator(func1)
#var()

#var1=decorator(func2)
#var1()





