import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re


def toRelativePath(path):
    obj = re.match("C:/sem4/vs code/import files/blocks",path)
    path = path.replace(path[obj.start():obj.end()+1],"../data/blocks/")
    return path

def convert_to_bool(x):
    temp = True
    for v in x:
        temp = temp&v
    return temp

data = pd.read_json("./JSON/block color data.json")
data["path"] = data["path"].apply(toRelativePath)
data["color"] = data["color"].apply(lambda x:np.array(x))

temp = data["color"].apply(lambda x : x>[19,0,0,0])
temp = temp.apply(convert_to_bool)
data[temp]
arr = [x for x in data[temp]["path"]]
print(arr)