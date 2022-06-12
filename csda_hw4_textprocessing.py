import numpy as np
import pandas as pd
import re

tp =  "555-1239Dr. Bernard Lander(636) 555-0113Hollingdorp, Donnatella555-6542Fitzgerald, F. Sco\
tt555 8904Rev. Martin Luther King636-555-3226Snodgrass, Theodore5553642Carlamina Scarfoni" 

#print(tp)


# problem 1
pn = re.compile('\({,1}[0-9]{,3}\){,1}\-{,1}\ {,1}[0-9]{3}\-{,1}\ {,1}[0-9]{4}')
one = pn.findall(tp)
print(one)

# problem 2
name = re.compile('[a-zA-Z]+\.{,1}')
two = name.findall(tp)
print(two)

# problem 3
wholename = re.compile('[a-zA-Z.]{,}\ {,1}[a-zA-Z,.]+\ {,1}[a-zA-Z,.]{,}\ {,1}[a-zA-Z,.]{,}')
three = wholename.findall(tp)
print(three)

#problem 4
title = re.compile('[a-zA-Z]{2,3}\.{1}\ {1}[a-zA-Z,.]+\ {,1}[a-zA-Z,.]{,}\ {,1}[a-zA-Z,.]{,}')
four = title.findall(tp)
print(four)

#problem 5
secondname = re.compile('[a-zA-Z.]{,}\ {,1}[a-zA-Z,.]+\ {1}[a-zA-Z,.]+\ {1}[a-zA-Z,.]+')
five = secondname.findall(tp)
print(five)

#\ {,1}[a-zA-Z]+{,15}\ {,1}[a-zA-Z]+{,15}