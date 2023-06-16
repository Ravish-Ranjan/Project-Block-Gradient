import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re
import sys
import json


def toRelativePath(path):
    obj = re.match("C:/sem4/vs code/import files/blocks",path)
    path = path.replace(path[obj.start():obj.end()+1],"media/blocks/")
    return path

def convert_to_bool(x):
    temp = True
    for v in x:
        temp = temp and v
    return temp

def generateResponse(f,t,b):
    data = pd.read_json("./JSON/block color data.json")
    data["path"] = data["path"].apply(toRelativePath)
    data["color"] = data["color"].apply(lambda x:np.array(x))
    
    lower = np.array([float(f['h']),float(f['s']),float(f['l'])])
    upper = np.array([float(t['h']),float(t['s']),float(t['l'])])

    temp1 = data["color"].apply(lambda x : x[:-1]<upper)
    temp2 = data["color"].apply(lambda x : x[:-1]>lower)
    temp1 = temp1.apply(convert_to_bool)
    temp2 = temp2.apply(convert_to_bool)
    
    temp = temp1 & temp2
    arr = [x for x in data[temp]["path"]]
    return arr

from_color = json.loads(sys.argv[1])
to_color = json.loads(sys.argv[2])
blocks = sys.argv[3]
print(generateResponse(from_color,to_color,blocks))