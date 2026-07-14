"""
String = String is a sequence of characters and its behave like a tuple

String's method can returns new string, tuple can not


Syntax :-
st = "Aman"


st = 'Aman'
st =  "Aman"
st = '''aman 
is 
good 
boy
'''
st = """ """
st = """ """
st = str("Aman")
st = str('123')
st = str(123)
print(st)
print( type(st) )

from operator import index

string works ok index
    backward ,  forward
    

st ="AMANKUMAR"
print(st)
print(st[4])
print(st[-4])

# it also sliced

st ="AMANKUMAR"
print(st)
print(st[0:5:1])

String can be Replicate
st = "AMANKUMAR"
print( st )
print( st*3 )


String can be Traversed
st = "AMANKUMAR"
print( st )
for a in st:
    print(a)


st = "AMANKUMAR"
print( st )
for a in range(len(st)):
    print(st[a]*(a+1))


Build-in funtions
    sum , max , min , len



st = "AmanKumar"
print( st )
print( max(st) )
print( min(st) )
print( len(st) )

String's Operations
    * , +

st = "Aman"
print(st*3)      # Replicate
print(st+"Kumar")# Concatenation


String's Methods
    upper , lower , capitalize, title , strip , lstrip , rstrip

st ="AmanKumar"
print(st)
print(st.upper())
print(st.lower())
print(st.capitalize())
print(st.title())
st = "      aman    "
print(st)
print(st.lstrip())
print(st.rstrip())
print(st.strip())



st ="aman is a good boy"
print(st)

li= st.split()
print(li)

print( ' '.join(li) )

print(st.replace('good','bad'))

"""

# so now this part in day16 but we lear here

"""
String validation methods
    isdigit , isalpha , isalnum 
"""
# [string validation methods are give only bool value]


s = "2345"
print(s.isdigit()) # isdigit = all value are numerical
print(s.isalpha()) # isalpha =  all value are alphabet
print(s.isalnum()) # isalnum = all are both {alphabet,numerical}
st = "aman"
print( st.isdigit() )
print( st.isalpha() )
print( st.isalnum() )
st = 'aman123'
print( st.isdigit() )
print( st.isalpha() )
print( st.isalnum() )

st = "Amankumar123@gmail.com"
print( st.isdigit() )
print( st.isalpha() )
print( st.isalnum() )

