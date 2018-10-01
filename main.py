# Importing the brains behind the code
import room
from character import Enemy

# Create a character
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("*Zombie Noises*")
dave.set_weakness("Hammer")

# Setting up first room description
kitchen = room.Room("kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

# Setting as start room
kitchen.describe()

# Setting other room descriptions
dining_hall = room.Room("Dining Hall")
dining_hall.set_description("A brightly lit corridor like room covered in paintings")

# Setting Dave to appear in the dining hall
dining_hall.set_character(dave)

ballroom = room.Room("Ballroom")
ballroom.set_description("A vast room with shiny wooden flooring. Huge candlesticks guard the entrance.")

# Setting directions for rooms links
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

# On startup, make kitchen default room
current_room = kitchen

while True:
    print("\n")
    # Displaying the current room's information
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    # Allows user to act
    command = input("> ")
    # Takes what was inputted and tries to run that using room.py
    current_room = current_room.move(command)