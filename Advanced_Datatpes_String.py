#String: String is used to store multiple characters eighter in singke quotes or doule quotes
#Indexing = positive indexing,negative indexing
str1="divya is a good girl"
pos_index=str1[0]
neg_index=str1[-1]
print(str1)
print(pos_index)
print(neg_index)
#-------------------------------------------------------------------------------------
#slicing---->accessing sub characters in the string from one range to another range
#[start:stop:stepsize]
print(str1[0:5])
print(str1[1:-1])
print(str1[:])
print(str1[::])
print(str1[::-1])#--->to reverse a string
print(str1[-1::-2])
#-------------------------------------------------------------------------------------
#Mathematics with string
# '+' is used to concatenate two strings
#'-' is used to multiply the values
# while using '*' factor one value must be an integer
x="palle"
y="python"
print(x+y)
print(y+x)
print(x*5)
print(x*3+y)
#print(x*3*y)#---->error
#print(x+5)----->error
#----------------------------------------------------------------------
# string formatting techniques
# 1.normal format
# 2.  .format
# 3.f""strings
x=10
y=11
sum1=x+y
print("sum of",x ,"and",y,"is",sum1)
print("sum of {} and {} is {}".format(x,y,x+y))
print(f"sum of {x} and {y} is {x+y}")



