#basic Data types in python------>immutable
#int
#float
#complex
#boolean
#string
# Read the input data from key board
input1=input("enter")#---> To take string as input
#Dispay the output using output function
print(input1)
# Taking different types of inputs using input() functio
input2=int(input("enter integer number"))# to take integer as input
input=float(input("enter float number"))# To take float number as a input
# Type casting
#from int to other datatypes
x=10
y=float(x)# int to float
y1=complex(x)# int to complext
y2=bool(x)# int to bool
print(y)
print(y1)
print(y2)
#from float to other datatypes
s=10.0
y3=int(s)# float--->int
y4=complex(s)#float----->complex
y5=bool(s)# float --->bool
#from complx to other data types
s1=3+4j
#y6=int(s1)# we can't convert complex to int
y7=bool(s1)
#y8=float(s1)# cnt't convert complex to float
#print(y6)
print(y7)
#print(y8)
#bool to other data types
s2=True
y9=int(s2)
y10=float(s2)
y11=complex(s2)
print(y9)
print(y10)
print(y11)