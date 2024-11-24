import csv
import math

starting_room_name = "Olshan Lobby"
target_room_name = "Recording Studio Room 1"

all_adjacencies = {}
name_to_id = {}
id_to_name = {}
distances_from_origin = {}

with open("data.csv", 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        name_to_id[row[1]] = row[0]
        id_to_name[row[0]] = row[1]
        if row[0] != "idx":
            distances_from_origin[row[0]] = math.inf
            adjacencies = row[2].split(',')
            all_adjacencies[row[0]] = adjacencies


stem_room = {}

starting_room_id = name_to_id.get(starting_room_name)
target_room_id = name_to_id.get(target_room_name)

queue = [(starting_room_id, 0)]
visited_rooms = set()
distances_from_origin[starting_room_id] = 0

while queue:
    current_room_id, current_room_distance = queue.pop(0)

    if current_room_id not in visited_rooms:
        visited_rooms.add(current_room_id)

        for adj in all_adjacencies.get(current_room_id, []):
            if distances_from_origin[adj] > current_room_distance + 1:
                stem_room[adj] = current_room_id
                distances_from_origin[adj] = current_room_distance + 1
                queue.append((adj, current_room_distance + 1))

def get_previous_rooms(id):
    path = []
    while id in stem_room:
        path.append(id_to_name[id])
        id = stem_room[id]
    return path[::-1]

path = [starting_room_name] + get_previous_rooms(target_room_id)

print(f"Distance to target room: {distances_from_origin[target_room_id]}")
for room in path:
    print(room)
