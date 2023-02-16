class Person:
    def __init__(self, name, age):
        self.name = name
        self.age=  age
    def say_hello(self):
        print(f"Hello, my name is {self.name} and my age is {self.age} ")
# creating my object
person1=Person("Erick",30)
person1.say_hello()

person2=Person("Claris",17)
person2.say_hello()

person3=Person("Pavan",21)
person3.say_hello()

# creating a class called cars with the following attributes/properties
# make,model,year then create a function that prints make,model and year
# then create three objects

class Cars:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def display(self):
        print(f"{self.make,self.model,self.year}Are details of the cars available in our store")

car1=Cars("Rover","Range",2015)
car1.display()

car2=Cars("BMW","Mercedez",2019)
car2.display()

car3=Cars("Royals","Royce",2021)
car3.display()

class AirlineBookings:
    def __init__(self,airline,flyingdate,returndate):
        self.airline = airline
        self.flyingdate = flyingdate
        self.returndate = returndate

    def print_details(self):
        print(f"This are the details of {self.airline}. Your date of flying {self.flyingdate} and the date of return {self.returndate}.")

passenger1 = AirlineBookings("Qatar", "26th January 2015", "15th February 2015")
passenger1.print_details()

passenger2 = AirlineBookings("Kenya Airways","15th March 2012", "16th April 2012")
passenger2.print_details()

passenger3 = AirlineBookings("Air India", "12th February 2021", "26th April 2021")
passenger3.print_details()

passenger4 = AirlineBookings("Saudi Arabia", "12th December 2022", "26th January 2023")
passenger4.print_details()



