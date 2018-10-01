# Declare a new importable class
class Room():

    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None

    # Set character
    def set_character(self, new_character):
        self.character = new_character

    # Get the character
    def get_character(self):
        return self.character

    # Set room name
    def set_name(self, room_name):
        self.name = room_name

    # Get the room's name when entering it
    def get_name(self):
        return self.name

    # Set room description
    def set_description(self, room_description):
        self.description = room_description

    # Get the room's description when entering
    def get_description(self):
        return self.description

    # Takes the room's description and prints it to console
    def describe(self):
        print(self.description)

    # Used for changing rooms, sets the directions
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    # Gets the details about nearby rooms and prints it to console
    def get_details(self):
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)

    # Used to move from one room to another, if movement is not permitted, give the message "You can't go there!"
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go there!")
            return self

