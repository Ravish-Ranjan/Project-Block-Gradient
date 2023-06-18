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

def check(x,p,q,r,y):
    temp = (p*x[0]+q*x[1]+r*x[2] - p*y[0]+q*y[1]+r*y[2] == 0)
    return temp

def generateResponse(f,t,b):    
    data = pd.read_json("./JSON/block color data.json")
    data["path"] = data["path"].apply(toRelativePath)
    data["color"] = data["color"].apply(lambda x:np.array(x))
    
    lower = np.array([float(f['h']),float(f['s']),float(f['l'])])
    upper = np.array([float(t['h']),float(t['s']),float(t['l'])])
    
    res = np.random.uniform(0,255,3).round(0)
    a = lower-res
    b = upper-res
    [p,q,r] = np.cross(a,b)
    
    temp = data["color"].apply(lambda x: check(x,p,q,r,lower)).sort_index()
    
    arr = [x for x in data[temp]["path"]]

    return arr

# from_color = {"h":85,"s":"0.31","l":"0.45"}
# to_color = {"h":257,"s":"0.34","l":"0.32"}
# blocks = 5
from_color = json.loads(sys.argv[1])
to_color = json.loads(sys.argv[2])
blocks = int(sys.argv[3])
print(generateResponse(from_color,to_color,blocks)[:blocks])