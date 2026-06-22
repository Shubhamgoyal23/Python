"""
now we disscus about the dictionary

Dictionary:- Dictionary is a collection of key:value pair which is
called item.
{1:2,3:4}
1 = key
2 = value
1,2  = pair

key can not be duplicate
values can be duplicate


d = {1:232,2:567,5:677,'A':677,'Aman':568}
print(d)
print(type(d))
print(d['A'])


dictionary do not support Index
dictionary works on key
dictionary can not be sliced
dictionary can not be replicate
but, dictionary can be traverce


d = {1:232,2:567,5:677,'A':677,'Aman':568}
print(d)
for i in d: # by defult key travers
    print(i)



Dictionary's Methods
    keys , values , items


d= {1:258,2:568,3:569,'A':685,'Aman':568}
print(d)

# .keys
for i in d.keys():
    print(i)

# simple way

for i in d:
    print(i)

# it use for only print keys

#  .value
for i in d.values():
    print(i)

# .items =  print pairs
for i in d.items():
    print(i)

for k,v in d.items():
    print(k , v)



Dictionary's Methods
    get , pop , update




d = {1:232,2:567,5:677,'A':677,'Aman':568,}
print(d)
print(d[2])
# print(d[200])  # raise en error because of 200 key is not available
print(d.get(2))
print(d.get(200 , "not exist"))

d.pop('A')
print(d)

d2 = {3:99 , 4:88 , 5:66}
d.update(d2)
print(d)

"""
