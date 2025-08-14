from turtle import Turtle, Screen
import random

# Create the screen where the race will happen
screen = Screen()
screen.setup(width=500, height=400)

# Ask the player to bet on a turtle's color
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# List of turtle colors (each turtle gets a unique one)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Starting y positions so the turtles are spaced evenly vertically
y_positions = [-70, -40, -10, 20, 50, 80]

# List to store all turtle racers
all_turtles = []

# Create and position the turtles
for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")      # Create a new turtle object
    new_turtle.color(colors[turtle_index])   # Assign a unique color
    new_turtle.penup()                        # Lift pen so it doesn't draw lines
    new_turtle.goto(x=-230, y=y_positions[turtle_index])  # Move to starting position
    all_turtles.append(new_turtle)            # Add to the racers list

# Flag to control the race loop
is_race_on = False

# Start the race only if the user placed a bet
if user_bet:
    is_race_on = True

# Race loop
while is_race_on:
    for turtle in all_turtles:
        # Check if a turtle has crossed the finish line (x > 230)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()  # Get the color of the winning turtle
            
            # Announce results
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle won the race.")

        # Move the turtle forward by a random distance (0 to 10 pixels)
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# Keep the screen open until the user clicks
screen.exitonclick()
