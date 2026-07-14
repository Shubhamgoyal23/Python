"""
UDF = User Defined Functions

# Function is a set\group of statement which perform a specific task and return a value

syntax :-
def function_name(parameters):
    definition\statement

function_name(arguments)


def greet():
    print("Good Morning")


greet()
greet()
greet()


def greet(val):
    print("Good",val)


greet("Morning")
greet("Night")
greet("After Noon")


def add(a,b):
    print(a+b)


add(10,20)
add(a=10,b=20)
add(b=20,a=5)




def add(a,b):
    return a+b


print( add(10,30))


def add (a,b,c,d,e,f):
    return a+b+c+d+e+f

print(add(10,20,30,40,50,60))
# print(add(10,50,60,58))

def add(a,b,c=0,d=0,e=0,f=0):
    return a+b+c+d+e+f

print(add(10,20))
print( add(10,20,45,78,89,67) )
print( add(10,20,45) )
# print( add(10) ) # at least two arguments


def add (a=0,b=0,c=0,d=0,e=0,f=0):
    return a+b+c+d+e+f

print(add(10,20,305,959,692))
print(add(10,20))
print(add(10))
print(add())




def add (*a): # now we have freedom to enter many values
    print(type(a)) # tuple
    return sum(a)

print(add(10,20,30,60,784,655))
print( add(10) )
print( add(10,34) )
print( add(10,34,5456,67,78,89,90,46) )



def add(**a):
    print(type(a))
    return a



print( add(name='Rahul Kumar' , course='B.Tech') )
print( add(name='Shubham Goyal' , course='B.C.A') )
print( add(name='Tina Royal' , course='B.Tech') )
print( add(name='Goggi Kumar' , course='M.Tech') )



# Recursion :-  A recursion is a property of a function in which a functions call
# itself

def hello():
    print("hello india")
    hello()

hello()



# WAP to add all the nutural number using recursion

def add(n):
    if n==1:
        return 1
    else:
        return n+add(n-1)

print(add(50))






def cube(num):
    return num**3

print(cube(9))
print(cube(5))


"""
