# Range ----> range is used to generate a numbers in specific  range
# Range(x) --> it is used to generate a numbers from 0 to x-1
# Range(x,y) --> it is used to generate numbers from x to y-1
# Range(x,y,z) ---> x is start value y is stop value and z is stepsize here it is used to generate numbers from x to y-1 with the increment of  z by default step size is 1

# generate  list of numbers upto 100 using Range
x=list(range(101))
print(x)
# generate  list of numbers from 100 to 200
print(list(range(100,201)))
# generate  tuple of elements from 200 to 300 with increments of 2
print(tuple(range(100,201,2)))

