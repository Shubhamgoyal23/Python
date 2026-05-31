#day5 
''' Data types
1- Number
    - int (integer)   54 , -56 , 0
    - float (decimal value) 345.67 , -45.67 , 5/2 , 34.0
    - complex  a+bj , 3+8j
        a = 4+8j
        print(a)
        print( a.real )
        print( a.imag )
    - binary (101001011) 0b11011
        a = 0b10011
        print(a)
    - Octal Number (01234567)  0o344 , 0o215
        a = 0o165
        print( a )
    - Hexadecimal Number (0123456789ABCDEF) 0x234 , 0x125AC
        a = 0x1FA     
        print( a )
2. string 
    - 'A' , "A" , 'Aman' , "Aman" , 'AMAN' all are string
3. boolean
    - True , False
4. seqence Data type
    - List , Tuple
        a = [3,67,56]  List
        a = (34,67,89)  Tuple
5- Hash Data Type
    - Set , Dictionary
        a = {34,56,89}    Set
        a = {1:34,2:56,3:678}  Dictionary
        
       Dictionary = key:value:pare '''




# now we start day6
'''
Bulid-in funtion = print, input , int , float , type
 '''
'''WAP to calculate gross salary of an employee where HRA is
20% and DA is 30% of his basic salary.
HINT:- Gross Salary  = Basic Salary + HRA + DA'''
 
# BS= float(input("ENTER YOUR TOTAL SALARY: "))
# hra = BS*0.20
# da = BS*0.30
# GS = BS + hra + da
# print("GROSS SALARY :",GS)

# conditional statements
'''if ,
if-else, 
nested-if-else, 
if-elif-else,
complex condition'''

#IF
''' syntax 
if condition:
    true statements'''

if 10>5:
    print("Hello")   # it will print hello (cond it True)

if 10>50:
    print("Hello")  # it will print nothing (cond is False)


'''if_else
if condition:
    True_Statement
else:
    False_Statement'''

if 10>50:
    print("HELLO JI")
else:
    print("BYE BYE JI")


if 10>50:
    print("HELLO")
else:
    print("INDIA")
print("IS BEYOUTYFILL")


# WAP to find a greater value b/w two
 
a = 100
b = 200
if a>b:
    print("Greter value",a)
else:
    print("Greter value",b)

# code with input
a = int(input("Enter any number: "))
b= int(input("Enter any number: "))

if a>b:
    print("Greter value",a)
else:
    print("Greter value",b)
    
'''
WAP to ckeak an entersd number id EVEN|ODD
'''
num = int(input("ENTER ANY NUMBER: "))
 # % opreter gives rimender

if num%2 == 0:
    print("ENTERED number is EVEN")
else:
    print("ENTERED number is ODD")

# if-elif-esle

# if-elif-esle stement is use to create multiple conditions programm

'''
SYNTAX=
if cond:
    print("")
elif more cond:
    print("")
elif more cond:
    print("")
else:
    print("")
'''

# WAP to check an entered character is vowel/consonant

#let assume :- A,E,I,O,U(vowel)

ch = input("enter any character: ")

if ch == 'A':
    print(" vowel ")
elif ch == 'E':
    print(" vowel ")
elif ch == 'I':
    print(" vowel ")
elif ch == 'U':
    print(" vowel ")
elif ch == 'O':
    print(" vowel ")
else:
    print("consonant")

'''
Nested if else
Syntax:-

if condition:
    if condition:
        true_statement
    else:
        false_statement
else:
    if condition:
        true_statement
    else:
        false_statement
'''

# WAP to check a number is positive , negative or zero
num = int(input("Enter any number: "))

if num>0:
    print("number is positive")
else:
    if num<0:
        print("number is negitive")
    else:
        print("number is Zero!")


# complex conditons #  (write all conditions together using logical operator)  

# WAP to check an entered character is vowel/consonant
# Lets Assume :-   A,E,I,O,U (Vowel)

CH = 'E'
if CH == "A" or CH == "E" or ch=='I' or ch=='O' or ch=='U':
    print("Vowel")
else:
    print("Consonenat")
