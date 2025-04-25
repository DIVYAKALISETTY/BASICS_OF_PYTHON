# Tuple----> tuple is used to stored heterogenous elements
# immutable,allow duplicates,ordered collection
# allows indexing  and count
# create using paranthesis () it is not mandatory to mention ()
# Tuple packing
tup1=(1,2,3,"divya",8)
# Tuple unpacking
tup2=1,4,6,7,8  #----->tuple unpacking
print(type(tup2))
print(type(tup1))
count1=tup1.count(1)
print(count1)
# To store single element in tuple  we should place comma after the element
tup=(10,) # ------> tuple  < class  'tuple'>
tup1=(10) #  if we create like this it will treat as integer < class 'integer'>
print(type(tup))
print(type(tup1))
# Tuple supports  Indexing
tup2=(1,2,3,4,5,6,3,3,4,5)
print(tup2[-3:])
# count------> thus method counts number of accurances in tuple
print(tup2.count(3))




