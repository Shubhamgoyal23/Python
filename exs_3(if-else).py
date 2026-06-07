'''
# if (single condition)

#1.WAP tp cheak if a number is positive

num = int(input("Enter any number: "))
if num>0:
    print("positive")
    
#2. WAP to cheak "eligible to vote" if age is 18 and plus

age = int(input("Enter your age: "))
if age>=18:
    print("YOU ARE ELIGIBLE FOR VOTING")
    
#3. WAP to check if a number id divisible by 7
num = int(input("Enter any number: "))

if num%7==0:
    print("yes")

#5. print pass if the marsk greter then 40

marks = int(input("Enter your marks: "))
if marks>40:
    print("pass")

# 6. diplay a msg if tempertucher id exceed above the 45^C

tepm = int(input("Enter current temp in C: "))

if tepm>45:
    print("THE TEMPERATURE IS TO HIGHT\nstey in home")

# 7. Print "Logged In" if password matches "admin123".

# simple

passw= input("Enter your password: ")
if passw == "admin123":
    print("Logged In\nWelcome")

# adv(if-else)

username = input("Enter your username: ")  # username= shubham
password = input("Enter your password: ")  # password = 2016031

if username == "shubham":
    if password == "2016031":
        print("Welcome")
    else:
        print("password is incorrect")
else:
    print("username is incoorect")
    


#9. Check if a number is a multiple of 10.

num =int(input("Enter any number: "))

if num%10==0:
    print("The number is multiple of 10")
    
    

#10. Print a warning if balance is below minimum limit. 

# min limit = 500

bank_balance =  int(input("Enter your current balace: "))
if bank_balance<=500:
    print("REMERING BALANCE IS BELOW THE LIMIT")


#IF–ELSE (Two Conditions)

#12. Find the largest of two numbers.

# simple
a = 100
b = 200


if a>b:
    print("The greter number is",a)
else:
    print("The greter number is",b)


# input

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


if a>b:
    print("The greter number is",a)
else:
    print("The greter number is",b)



#13. Check whether a person is eligible for driving license.


name= input("Enter your full name: ")
age =  int(input("Enter your current age: "))

if age >=18:
    print(name,"eligible your driving license")
else:
    print("YOU ARE NOT ELIGIBLE FOR DRIVING LICENSE")
    

#15. Check whether a number is positive or negative.

num = int(input("Enter any number: "))

if num >0:
    print("The number is positive")
else:
    print("The number is negative")

# 0 ko bhi as a positive bolega 
    # correct  = if-efil-else


    
#17. Check if a year is leap or not.

year = int(input("Eter current year: "))

if year%4==0:
    print("The year is leap year")
else:
    print("The year is not leap year")

'''


# ELIF (Multiple Conditions)

# 
