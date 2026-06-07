'''
Looping :- we can execute a same task again and again using loop 
types  
for 
while
'''
#for 
'''syntax
for variale_name i range(start, stop, step):
    stetement'''

print(*range(1,11,1))
print(*range(1,11,2))

for a in range(1,5,1):
    print("hello")


for a in range(2,21,2):
    print(a)

'''by default step = 1
by defult start = 0'''


# WAP to print counting from 0 to 10

print(*range(0,11,1))
#or 

for a in range(0,11,1):
    print(a)

# WAP to print table of an number
num = int(input("Enter any number"))
for i in range(1,11,1):
    print(num*i)

    
# WAP to print table of a number
''' 3 * 1 = 3
    3 * 2 = 6
'''
num = int(input("Enter any number:"))
for i in range(1,11,1):
    print(num,"*",i,"=",i*num)

# WAP to print factors of a number
# HINT: 12 => 1,2,3,4,6,12

num = int(input("Enter A Number : "))
for i in range(1,num+1):
    if num%i==0:
        print(i)