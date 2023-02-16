# if statement
x=1
marks=49
grade=150
balance=3500
if(x>0):
    print("The number is positive")

# if .... else statement
if(marks>=50):
    print("You have passed the exams")
else:
    print("You have failed your exams")

# if ...elif ... else statement
if(grade>=0 and grade<=29):
    print("You failed")
elif grade>=30 and grade<=49:
    print("You have passed")
elif grade>=50 and grade<=79:
    print("You have a credit")
elif grade>=80 and grade<=100:
    print("You have distinction")
else:
    print("Wrong grade entered")
if(balance>=0 and balance<=500):
    print("Not enough money")
elif balance>=501 and balance<=700:
    print("Cannot withdraw")
elif balance>=900 and balance<=1999:
    print("Can withdraw only half")
elif balance>=2000 and balance<=2500:
    print("Can withdraw")
elif balance>=3000 and balance<=5000:
    print("Can withdraw  everything")
else:
    print("Invalid error")


