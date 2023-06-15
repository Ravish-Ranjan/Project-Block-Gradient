from PIL import Image
import json

base = "C:/sem4/vs code/import files/blocks/"
file = "C:/sem4/vs code/project blocks/scandir.json"

with open(file) as job:
    data = json.load(job)


for png in data['files']:
    path = base + png
    img = Image.open(path)
    if (img.height != 16) or (img.width != 16):
        print(f"{png}\t {img.height} \t {img.width}")

