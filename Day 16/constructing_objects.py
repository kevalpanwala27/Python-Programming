from turtle import Turtle, Screen

timmy = Turtle()  # timmy here is an object and Turtle() here is a class
print(timmy)
timmy.shape("turtle")
timmy.color("red")
timmy.forward(100)
my_screen = Screen()
print(my_screen.canvheight)  # my_screen is an object and canvheight is an attribute - means properties.

print(my_screen.exitonclick())  # my_screen is an object and exitonclick() is a method - means function.


# How to install package and import it.

from prettytable import PrettyTable

jack = PrettyTable()
print(jack)
