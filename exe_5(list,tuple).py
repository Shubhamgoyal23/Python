
"""
# Python Programming Questions – LIST
from itertools import count

# 1. Write a Python program to create a list of integers and print its elements.

li = [25,28,58,14,47,36,69]
print(li)
print(type(li))

# another way

li = [10,20,30,60,50,40]
print("ALL LIST ELEMENTS")
for i in li:
    print(i)


# 2. Write a program to find the sum and average of all elements in a list.

li = [10,20,30,60,50,40,90,80]

# sum
print(sum(li))

# average
print(sum(li)/len(li))

# 3. Write a program to find the largest and smallest element in a list.

li = [28,58,47,71,16,515,82,695,58]

#largest
print(max(li))

# smallest
print(min(li))

# 4. Write a Python program to count the number of elements in a list without using len().

li = [25,58,47,71,16,515,82,695,58]

count = 0

for i in li:
    count += 1

print(count)

# 5. Write a program to reverse a list without using built-in functions.

li = [25,58,47,71,16,515,82,695,58]

li.sort(reverse=True)
print(li)

# 6. Write a program to check if an element exists in a list.

li = [25,58,47,71,16,515,82,695,58]

element = int(input("Enter the element you want to check: "))

if element in li:
    print("Element is in the list")
else:
    print("Element is not in the list")


7. Write a Python program to remove duplicate elements from a list.


li =[21,23,36,65,45,96,85,74,54,45,58,85,74]

new_list = []

for i in li:
    if i not in new_list:
        new_list.append(i)

print(new_list)
print(len(new_list))


8. Write a program to sort a list in ascending and descending order.


li =[21,23,36,65,45,96,85,74,54,45,58,85,74]

#ascending
li.sort()
print(li)

# descending
li.sort(reverse=True)
print(li)

9. Write a program to merge two lists and remove duplicates.


li1 = [25,24,26,41,52,63,69,58,47,58,42,43,51,62]
li2 =[74,85,96,42,43,51,62,61,53,10]

li1.extend(li2)
print(li1)
print(len(li1))

new_merge_list = []

for i in li1:
    if i not in new_merge_list:
        new_merge_list.append(i)


print(new_merge_list)
print(len(new_merge_list))





10. Write a program to find common elements between two lists.



li1 = [25,24,26,41,52,63,69,58,47,58,42,43,51,62]
li2 =[74,85,96,42,43,51,62,61,53,10]

common_list = []

for i in li1:
    if i in li2:
        common_list.append(i)

print(common_list)



11. Write a program to split a list into even and odd numbers.


li = [1,2,3,4,5,6,7,8,9,10]

even_list =[]
odd_list = []

for i in li:
    if i%2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print(even_list)
print(odd_list)

12. Write a program to rotate a list by n positions.
13. Write a Python program to find the second largest number in a list.


numbers = [10, 20, 40, 30, 50]
numbers.sort()

print(numbers[-2])


li =[10,20,30,-60,-50,40,80,-90,70]

for i in range(len(li)):
    if li[i] < 0:
        li[i] = 0

print(li)





#  tuple


3. Write a Python program to create a tuple and print its elements.
TP = (10,20,30,60,50,40)
print(TP)



4. Write a program to find the length of a tuple.


TP = (10,20,30,60,50,40)
print(len(TP))


5. Write a program to find the maximum and minimum element in a tuple.



TP = (10,20,30,60,50,40)

print(min(TP))
print(max(TP))



6. Write a program to convert a tuple into a list.


TP = (10,20,30,60,50,40)

TP = list(TP)
print(TP)
print(type(TP))


7. Write a program to check if an element exists in a tuple.


# 50

element = int(input("Enter an Element to Find: "))
tp= (10,20,30,60,50,40,80)

if  element in tp:
    print("The element is found")
    print("It is",tp.index(element),"index")
else:
    print("The element is not in the Tuple")


# print(tp)


9. Write a program to slice a tuple and display the result.


start = int(input("Enter the staring index: "))
end= int(input("Enter the Ending index: "))

tp =(10,20,30,605,508,500,40)

print(tp[start:end])



30. Write a program to find repeated elements in a tuple.
"""


tp = (10,20,30,60,50,40,70,80,50,60,10,20)

tp2 = ()

