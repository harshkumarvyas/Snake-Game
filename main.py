from turtle import Turtle, Screen

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('My snake game')

starting_positions = [(0, 0),(-20, 0), (-40, 0)]

# Screen Setup and Creating a Snake Body
for position in starting_positions:
    new_turtle = Turtle('square')
    new_turtle.color('white')
    new_turtle.goto(position)


screen.exitonclick()