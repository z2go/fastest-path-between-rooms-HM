#Imports
import csv
import math


starting_room_name = "Olshan Lobby" #Stores starting room name
target_room_name = "Recording Studio Room 1" #Stores ending room name


all_adjacencies = {} #Stores all rooms' adjacencies
name_to_id = {} #Dictionary for converting name to id
id_to_name = {} #Dictionary for converting id to name
distances_from_origin = {} #Stores the distances away from the starting room

#The code below parses the CSV file into a dictionary with the adjacencies of each room.
#It also fills out the id_to_name and name_to_id dictionaries
#Finally, it sets all distances equal to infinity
with open("data.csv", 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        name_to_id[row[1]] = row[0]
        id_to_name[row[0]] = row[1]
        if row[0] != "idx": #Makes sure that the first row isn't put in the data
            distances_from_origin[row[0]] = math.inf
            all_adjacencies[row[0]] = row[2].split(',')


stem_room = {} #Keeps track of what the previous room to get to a room was

starting_room_id = name_to_id.get(starting_room_name)
target_room_id = name_to_id.get(target_room_name)

stack = [(starting_room_id, 0)] #The stack for DFS
visited_rooms = [] #Stores the rooms visited
distances_from_origin[starting_room_id] = 0 #Sets starting room distance to 0

# The while loop below runs while the stack isn't empty and adds more vetices to the stack whenever it detects that they haven't been used.

while stack:
    current_room_id, current_room_distance = stack.pop()

    if current_room_id not in visited_rooms:
        visited_rooms.append(current_room_id)

        for adj in all_adjacencies[current_room_id]:

            if adj not in visited_rooms:

                stem_room[adj] = current_room_id
                distances_from_origin[adj] = current_room_distance + 1
                stack.append((adj, current_room_distance + 1))

#This function gets the path of rooms from the starting room to a room
def get_previous_rooms(id):
    path = []
    while id in stem_room:
        path.append(id_to_name[id])
        id = stem_room[id]

    return path[::-1]

path = [starting_room_name] + get_previous_rooms(target_room_id)
#We have to add the starting room to the path because the path doesn't count the starting room

print(f"Distance to target room: {distances_from_origin[target_room_id]+1}") #Prints distance
for room in path: #Prints path
    print(room)
