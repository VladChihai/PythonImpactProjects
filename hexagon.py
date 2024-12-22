import turtle

polygon = turtle.Turtle()
num_side = 6
side_length = 75
angle = 360 / num_side

for i in range(num_side):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.exitonclick()