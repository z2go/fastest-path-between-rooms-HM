#Imports
import csv
import math

eccentricity = 0

room_ids = []

all_adjacencies = {} #Stores all rooms' adjacencies

distances_from_origin = {} #Stores the distances away from the starting room

#The code below parses the CSV file into a dictionary with the adjacencies of each room.
#It also fills out the id_to_name and name_to_id dictionaries
#Finally, it sets all distances equal to infinity
with open("data.csv", 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] != "idx": #Makes sure that the first row isn't put in the data
            room_ids.append(row[0])
            distances_from_origin[row[0]] = math.inf
            all_adjacencies[row[0]] = row[2].split(',')

# The while loop below runs while the queue isn't empty and adds more vetices to the queue whenever it detects that they haven't been used.
for room in room_ids:
    queue = [(room, 0)]  # The queue for BFS
    visited_rooms = []  # Stores the rooms visited
    distances_from_origin[room] = 0  # Sets starting room distance to 0
    while queue:
        current_room_id, current_room_distance = queue.pop(0)

        if current_room_id not in visited_rooms:
            visited_rooms.append(current_room_id)

            for adj in all_adjacencies[current_room_id]:

                if (distances_from_origin[adj] > current_room_distance + 1
                    and adj not in visited_rooms):

                    distances_from_origin[adj] = current_room_distance + 1
                    queue.append((adj, current_room_distance + 1))
    for id in room_ids:
        eccentricity = max(eccentricity,distances_from_origin[id])
        distances_from_origin[id] = math.inf

print(eccentricity)



