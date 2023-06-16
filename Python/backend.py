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
    iter = 0
    while iter<10:
        filter_s1 = 0.5
        filter_s2 = 0.45
        
        data = pd.read_json("./JSON/block color data.json")
        data["path"] = data["path"].apply(toRelativePath)
        data["color"] = data["color"].apply(lambda x:np.array(x))
        
        lower = np.array([float(f['h']),float(f['s']),float(f['l'])])
        upper = np.array([float(t['h']),float(t['s']),float(t['l'])])
        
        
        h1 = data["color"].apply(lambda x : x[0]<upper[0])
        h2 = data["color"].apply(lambda x : x[0]>lower[0])
        
        s1 = data["color"].apply(lambda x: x[1]<filter_s1)
        s2 = data["color"].apply(lambda x: x[1]>filter_s2)
        
        temp = h1 & h2 & s1 & s2
        if(data[temp].size==0):
            filter_s1 += 0.05
            filter_s2 -= 0.05
            iter+=1
        else:
            break
    arr = [x for x in data[temp]["path"].head(b)]
    return arr


from_color = json.loads(sys.argv[1])
to_color = json.loads(sys.argv[2])
blocks = int(sys.argv[3])
print(generateResponse(from_color,to_color,blocks))