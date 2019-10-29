import turtle

print("Available commands: up, down, left, right, forward, pivotright, pivotleft")

while True:
    turtle.showturtle()
    turtle_input = input("turtle@turtle-desktop:~$ ")
    if turtle_input == "up" or turtle_input == "u":
        turtle.penup()
    elif turtle_input == "down" or turtle_input == "d":
        turtle.pendown()
    elif turtle_input == "right" or turtle_input == "r":
        turtle.right(90)
        turtle.forward(100)
    elif turtle_input == "left" or turtle_input == "l":
        turtle.left(90)
        turtle.forward(100)
    elif turtle_input == "forward" or turtle_input == "f":
        turtle.forward(100)
    elif turtle_input == "pivotright" or turtle_input == "pr":
        turtle.right(45)
    elif turtle_input == "pivotleft" or turtle_input == "pl":
        turtle.left(45)
    elif turtle_input == "exit":
        break
    else:
        print("Invalid command. Try one of the following: up, down, left, right, forward")