'''
Collection =  List,tuple,dictionry,string,set

sequnce datatype
    List , Tuple
    
List= List is collection of hetrogenous(diffrent) elements

syntax= 
list_name = [1,2,3,4,5]

ex
li = [1,2,3,45]
li = [1,23,45,67,89,78,65,4443,,443,True,'A','shubam']
li = [] # empty list
li = list()
li = list([1,2,34,,44])
li = list((22,23,442,4334,243))
print(li)
print(type(li))


# asseccing the elementa

list woke on index
forward = 0,1,2,3,4....
backward =  ...-3,-2,-1
list_name[index]

Slicing
     list_name[start_index:stop_index:step_index]# start:stop:step
# step defult  = 1



li = [23,34,45,67,78,899,548,548]
print(li)
print(li[3:6:1])
print(li[3:5])
print(li[3:5:2])


#Replication
li = [1,2,3,4,5]
print(li)
print(li*3) # it will repeat all elamenta from 3 times



# Traversing

li = [23,4345,67,423,213]
print(li)
# to travers the list = loop
for x in li:
    print(x)



# build in funtions

    sum,max,min,len

    li = [23,4345,67,423,213]
print(li)

print(sum(li))
print(max(li))
print(min(li))
print(len(li))
print(sum(li)/len(li))


# list methods(opretion)
     append ,extend , insert


li =[21,25,58,64,56,585,9266,556]
print(li)

li.append(99) # .append  = add the element in last of the list
print(li)

li.insert(2,58) # .insert =  add the element anywhere in list using index
print(li)

li2 =[258,256,245,155]
li.extend(li2)  # .entend  = combinition the two or more  lists
print(li)


    pop ,remove, del , clear


li = [234,456,78,7,654,7,32]
print(li)
li.pop()  # delete last element by default
print(li)
li.pop(2)   # pop(index)
print(li)
li.remove(7)   # remove(value)
print(li)
del li[1]     # del keyword
print(li)
li.clear()
print(li)


        sort , reverse

li = [78,23,67,45,682,63]
print(li)
li.reverse()
print(li)
li.sort()
print(li)
li.sort(reverse=True)
print(li)


  index , count

li = [23,67,89,63,48,35,63,457,76,45,63]
print(li)
print( li.count(63) )

print( li.index(48) )
print( li.index(63,4) )
 print( li.index(63,4,7) )


'''

