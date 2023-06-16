import random
from json import load

get = random.random


from_,to = [[0,0.99,0.71],[281,0.79,0.43]]

n = int(input("Enter the no. of blocks : "))

factors = -((from_[0]-to[0])//(n-1))

colors = [  [round(from_[0]+(a*factors),2),from_[1],from_[2]] for a in range(n) ]
