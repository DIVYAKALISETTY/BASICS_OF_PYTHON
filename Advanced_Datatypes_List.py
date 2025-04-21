#list--->which is used to store sequence of heterogeneous elements  in square brackets"[]"
#mutable,allows duplicates,ordered collections of elements
#create a list
list1=[10,"divya",20,"ratna",30,"jyothi"]#------->storing heterogeneous elements
list2=[1,2,3,4,5,6]#------->,strong homogeneous elements
print(list1)
print(type(list1))#-->type()-->function is used to know the type of the object
print(len(list1))#----->len()-->used to find the length of the string
print(list1[::-1])
print(list2[::-2])
#modifying element in a list
list1[0]="anjali"
print(list1)
list1[1:4]=1,2,3
print(list1)
print(list1[0]*list1[3])
#del list
del list1
print(list2)
list2.clear()
print(list2)
#create 2 list one with homogeneous elements and another with heterogeneous elements
#and concatenate both list
l1=[1,2,3,4]
l2=[1,"ammu",2.0,3+5j,True]
print(l1+l2*3)