import numpy as np
import pandas as pd
from cmath import sqrt
import random

df = pd.read_csv('pomiary.xlsx')

g=9.8123
alfa = 0.1

ax = random.randrange(-100,100)
bx = random.randrange(-100,100)
ay = random.randrange(-100,100)
by = random.randrange(-100,100)
az = random.randrange(-100,100)
bz = random.randrange(-100,100)



xp = 
yp = 
zp = 

xr = ax*xp+bx
yr = ay*yp+by
zr = az*zp+bz

pier = sqrt(xr**2+yr**2+zr**2)

f=pier-g

fbx = (1/(2*pier))*2*xr
fby = (1/(2*pier))*2*yr
fbz = (1/(2*pier))*2*zr

fax = fbx*xp
fay = fby*yp
faz = fbz*zp

ax = ax - alfa * f/fax
bx = bx - alfa * f/fbx
ay = ay - alfa * f/fay
by = by - alfa * f/fby
az = az - alfa * f/faz
bz = bz - alfa * f/fbz