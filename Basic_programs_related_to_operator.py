#Read three numbers from the keyboard find arithmetic opeartions i.e,Addition,Substraction,Multiplication
num1=int(input("enter first number"))
num2=int(input("enter num2"))
num3=int(input("enter num3"))
add=num1+num2+num3
sub=num1-num2-num3
mul=num1*num2*num3
print("add:",add)
print("sub: ",sub)
print("mul: ",mul)
# Read principal,time and amount from the keyboard and find simple intrest
p=int(input("enter principal amount"))
r=int(input("enter rate"))
t=int(input("enter time"))
si=(p*r*t)/100
print("simple intrest:",si)
#read length and bredth from the keyboard find area and parametr of the rectangle
len=int(input("enter length"))
bre=int(input("enter bre"))
area=len*bre
parameter=2*(len+bre)
print("area of rec: ",area)
print("parameter of rec: ",parameter)
#read the radius from the keyboard and find the area of the circle
r=int(input("enter radius of the circle"))
pi=3.14
area_circle=pi*(r**2)
print("area of the circle:",area_circle)