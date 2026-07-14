"""

SET :- Set is also a collection of unique hetreogenous
elements

Syntax:-
s = {34,45,67,78,90}

s = {23,3,56,787,654}
s = {234,567.323,'Aman',True}
s = set()
s = set([34,56,677,89,57])
print(s)
print(type(s))

s = {34,56,77,45,897,65,65,42}
print(s)  # print elements on random positions

s = {21,34,34,45,54,23,32,4,23,23,23,45,45}
print(s) # remove duplicate element


Order is not preserved in set
SET has no Index
SET can not be sliced
SET con not be Replicate
But, Set can be traverse

se = {32,545,25,25,454,87}
print(se)
for i in se:
    print(i)


Built-in functions
    sum , max , min , len

s = {32,34,67,789,89,89,76}
print(s)
print( sum(s) )
print( max(s) )
print( min(s) )
print( len(s) )



# set's Methods
        add , pop , remove , discard , clear



s=  {10,155,518,58,58,595,5411,0,2}
print(s)
s.add(99)
print(s)
s.pop() # .pop is remove the elements randomly
print(s)


# .remove raise an error if the enter key is not available


# .discard will not raise any error if the enter key is not available

s.clear()
print(s)



SET's Methods
intersection , union , difference , symmetric_difference




s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}

print(s1.intersection(s2)) # common elements
print(s1.union(s2)) # elements of both sets( remove duplicatis)
print(s1.difference(s2)) # will remove elements from s1 which are also in s2
print(s1.symmetric_difference(s2)) # remove the common elements



set's opretion



s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}
print(s1&s2) # & = intersecction
print(s1|s2) # | = union
print(s1-s2) # - = diff
print(s1^s2) # ^ = symmetric_difference

"""
