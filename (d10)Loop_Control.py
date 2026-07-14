'''
loop ko control karne ke liye kuch statements
1.break
2.pass
3.continue
4.esle


# 1, break = it will taje exit from the current loop

for i in range(1,6):
    if i==3:
        break
    print(i)


for x in range(1,11):
    if x==10:
        break
    print(x)


# 2. continue = continue take the cursor to the next itteration

                --------
# Ex= --------- continue-------- =  lopp

for i in range(0,11):
    if i ==10:
        continue
    print(i)


for x in range(5,51,5):
    if x==30:
        continue
    print(x)

# 3. pass= pass do nothing{pass apke code ko rokh ta nhi hai}


for i in range(1,6):
    if i ==3:
        pass
    print(i)

#
if 10>5:
    pass

print("hello")



#4. else

for i in range(1,7):
    print(i)
else:
    print("Loop is end")


# esle is noy working with break

for x in range(1,7):
    if x==3:
        break
    print(x)
else:
    print(0)


# try with while loop)


i  = 1
while i<=5:
    print(i)
    i = i+1
    if i==4:
        break
else:
    print(0)

    print(0)



i = 1
while i<=5:
    print(i)
    if i==3:
        continue
    i=i+1
else:
    print(0)



i = 1
while i<=5:
    print(i)
    if i==3:
        pass
    i=i+1
else:
    print(0)
'''
