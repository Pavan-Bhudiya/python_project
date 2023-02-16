# creating of a function
def emobilis():
    print("This is my first function")
emobilis()

def calculatesquare():
    x=5
    y=6
    print(x*y)
calculatesquare()

# function of majina
def majina(fname, lname, age):
    print(fname + lname + age)
majina(" Erick "," Were "," 6 ")

# function of addition
def calculator(num1 , numn2):
    print("The sum is "+str(num1+numn2))
calculator(12,21)

# function of triangle area
def triangle_area(height,base):
    print("The area of the triangle is "+str(0.5*height*base))
triangle_area(25,15)

# maximum function
def maximum(a,b,c,d,e):
    return max(a,b,c,d,e)
result=maximum(5,15,67,9,89)
print(result)

# minimum function
def minimum(a,b,c,d,e):
    return min(a,b,c,d,e)
result=minimum(5,15,-1,67,89)
print(result)

# range of numbers function
def print_numbers(nambari1):
    for i in range(nambari1):
        print(i)
print(10)



