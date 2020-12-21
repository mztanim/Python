
print("Input lengths of the triangle sides: ")

user_input1 = input (" X ")
user_input2= input (" Y ")
user_input3= input (" Z ")

x= int (user_input1)
y= int (user_input2)
z= int (user_input3)

if x==y==z:
    print ("It is a equlateral triangle")
elif x==y or y==z or z==x:
    print ("It is a Isosceles triangle")
else:
    print ("It is a scalene triangle")