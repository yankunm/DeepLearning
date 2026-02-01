from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)
print(timmy.position())

my_screen = Screen()
print(my_screen.canvheight) # attribute

my_screen.exitonclick()

