# Set --> It is an advanced data type it isused to store the data in unordered manner
# it is used to created by {}
# Set does not allow indexing
# set does not allow duplicates
# Set is mutable and set elements are immutable
# -----------------------------------------------------------------------#

# create a empty set
x= set()
y={} # we should not create emty set like this because it will trreat as dictionary
print(type(x)) #----> <class 'set'>
print(type(y)) # ----> <class 'dict'>
# create a set
set1={10,20,30,40,60}
print(set1)
print(type(set1)) # <class 'set'>
print(len(set1)) # 5
#set does not allow indexing
#print(set1[5]) ----> it will trow an error
# set does not allow duplates
set4={1,2,2,3,5,6,7,4,6}
print(set4)# ---> it will remove duplicates and provide output as #{1,2,3,4,5,6,7}
# set2={10,3,4,5,[10,30,40]}  -----> it will trow an  Type error because list elements are mutable
# print(set2)
set3={10,30,304,40,(40,50)}
print(set3)
# sets are faster than lists and tuples because sets stores elements in random order


