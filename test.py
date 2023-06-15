import json

file = "C:/sem4/vs code/project blocks/block color data.json"

with open(file) as job:
    data = json.load(job)

for block in data:
    if block['color'][0] <10 or block['color'][0] >350:
        print(block['name'])