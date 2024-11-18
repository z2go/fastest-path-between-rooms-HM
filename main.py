import csv
import math

starting_room_name = "Olshan Lobby"
target_room_name = "Recording Studio Room 1"

all_adjacencies = {}
name_to_id = {}
id_to_name = {}

distances_from_origin = {}

with open("data.csv",'r') as file:
    reader = csv.reader(file)

    for row in reader:
        name_to_id[row[1]] = row[0]
        id_to_name[row[0]] = row[1]
        if row[0] != "idx":
            distances_from_origin[row[0]] = math.inf
            adjacencies = []
            adjacency = ""
            for char in row[2]:
                if char.isnumeric():
                    adjacency = adjacency+char
                else:
                    adjacencies.append(adjacency)
                    adjacency = ""
            adjacencies.append(adjacency)
            all_adjacencies[row[0]] = adjacencies



desired_room_id = name_to_id[starting_room_name]
starting_room_id = name_to_id[target_room_name]

queue = [starting_room_id]
visited_rooms = []

distances_from_origin[starting_room_id] = 0
while len(queue) > 0:
    current_room_id = queue[0]
    visited_rooms.append(current_room_id)



    queue.pop(0)


print(all_adjacencies)