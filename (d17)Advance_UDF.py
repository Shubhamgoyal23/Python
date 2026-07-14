"""
Advance pyhton
Lambda Expression
    map , filter , reduce

function_name = Lambda parameter : definition

# Lambda Expression



cube = lambda num :num**3

print(cube(5))
print(cube(9))


# def cheakeven(num):
#     if num%2 == 0:
#         return "even"
#     else:
#         return "odd"
    

cheakeven = lambda num: 'even' if num%2==0 else 'odd'

li =[23,45,67,78,7665,43,32,4,56,78]
for i in li:
    print( i,'\t',cheakeven(i))


# cheakeven = lambda num: 'even' if num%2==0 else 'odd'




    map , filter , reduce



square  = lambda num:num**2
li = [23,45,67,78,76,65,43,32,4,56,78]
res  = list(map(square,li))
print(res)


cube = lambda num:num**3
li = [23,45,67,78,76,65,43,32,4,56,78]
res = tuple(map(cube,li))
print(res)




cheakeven = lambda num:num%2 == 0
li =[23,45,67,78,76,65,43,32,4,56,78]
for i in li:
    if cheakeven(i):
        print(i)

        
    filter

            
 checkEven = lambda num : num%2==0
li = [23,56,89,57,3,2,54,5,8,86,64,35]
res = list( filter(checkEven , li) )
print(res)


add  = lambda a,b:a+b
li  = [1,2,3,4,5,6,7,8,9,10]
res = 0
for i in li:
    res = add(res,i)
print(res)

"""
    # reduce

from functools import reduce
add  = lambda a,b:a+b
li = [1,2,3,4,5,6,7,8,9,10]
res = reduce(add , li)
print( res )