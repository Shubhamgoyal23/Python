"""
1. Print numbers from 1 to 10 using a while loop.

num = 1
while num <= 10:
    print(num)
    num =num+1

2. Print even numbers from 1 to 20.


num = 0
while num <= 20:
    if num % 2 == 0:
        print(num)
    num = num + 1

3. print odd numbers from 1 to 20


num = 0
while num <= 20:
    if num % 2 == 1:
        print(num)
    num = num + 1


4. Print numbers from 10 to 1 (reverse order).

i = 10

while i >= 1:
    print(i)
    i -= 1

5. Print multiplication table of 5 using while loop.

num = 1
while num <= 10:
    print(5,"*",num,"=",num*5)
    num += 1


#with input


no = int(input("Enter Any Number: "))

num = 1
while num <= 10:
    print(no,"*",num,"=",num*no)
    num += 1

6. Find the sum of first 10 natural numbers using while loop.




num = 1
sum = 0
while num<= 10:
    sum = sum+num
    num += 1
print(sum)



7. Find factorial of a number entered by user.


# 5


factorial = int(input("Enter Any Number:"))
num = 1
sum = 1
while num <= factorial:
    sum = sum*num
    num += 1
print("The Factorial of",factorial,"is",sum)



13. Ask user to enter password until correct password is entered.

correct_password = "python123"

password = input("Enter Password: ")

while password != correct_password:
    print("Wrong Password! Try Again.")
    password = input("Enter Password: ")

print("Login Successful!")

"""
