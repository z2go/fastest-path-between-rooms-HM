import csv

dict = {}


def parse_data():
    with open("data.csv",'r') as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] != "idx":
                adjacencies = []
                adjacency = ""
                for char in row[2]:
                    if char.isnumeric():
                        adjacency = adjacency+char
                    else:
                        adjacencies.append(adjacency)
                adjacencies.append(adjacency)
                dict[row[1]] = adjacencies

parse_data()

print(dict)