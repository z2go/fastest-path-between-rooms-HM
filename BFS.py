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

stem_room = {}

desired_room_id = name_to_id[target_room_name]
starting_room_id = name_to_id[starting_room_name]

queue = [[starting_room_id,0]]
visited_rooms = []



distances_from_origin[starting_room_id] = 0

def get_previous_rooms(depth, id):
   if depth == 0:
       return []
   else:
       return get_previous_rooms(depth-1,stem_room[id]) + [id_to_name[id]]

while len(queue) > 0:
    current_room_id = queue[0][0]
    current_room_distance = queue[0][1]

    if not current_room_id in visited_rooms:
        visited_rooms.append(current_room_id)

    for adj in all_adjacencies[current_room_id]:
        if distances_from_origin[adj] > current_room_distance+1:
            stem_room[adj] = current_room_id
            distances_from_origin[adj] = current_room_distance + 1
        #distances_from_origin[adj] = min(distances_from_origin[adj], current_room_distance + 1)
        if not adj in visited_rooms:
            queue.append([adj,current_room_distance+1])
    queue.pop(0)

#print(distances_from_origin)
#print(all_adjacencies)
#print(distances_from_origin[desired_room_id])
path = [starting_room_name] + get_previous_rooms(distances_from_origin[desired_room_id],desired_room_id)

for room in path:
    print(room)

