import numpy as np
import pandas as pd



# problem 1
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
distinct = []
used = []
for n in a:
    if n not in used:
        for m in b:
            if m == n:
                distinct.append(n)
                break
        used.append(n)
print(distinct)

# problem 2
c = np.arange(1,16)
c = c.reshape(3,5)
c = c.T
print(c)

# problem 3
d = c.T
d = d.reshape(-1)
print(d)

# problem 4 (incomplete)
e = c.reshape(3,5,1)
#print(e)

# problem 5 (incomplete)
f = e.reshape(5,3)
#print(f)

# problem 6
g = np.array([12,5,7,15,3,1,8])
h = np.array([14,6,3,11,19,12,5])
print(g)
print(h)
index = 0
delval = []
for i in g:
    for j in h:
        if j == i:
            delval.append(index)
            break
    index += 1
g = np.delete(g,delval)
print(g)

# problem 7
print()
df = pd.read_excel('Module6_Data.xlsx')
#arr = df.to_numpy()
print(df)
print()
#print(arr)
print()
print("Max yearly NYC consumption of water(millions of gallons per day): ")
print(df['NYC Consumption(Million gallons per day)'].max())
print()
print("Number of calendar years represented: ", df.shape[0])
print()
print("Average per capita NYC consumption of water: ")
print(df['Per Capita(Gallons per person per day)'].mean())
print()
print("Standard deviation: ")
print(df['Per Capita(Gallons per person per day)'].std())
print()
z = np.array(df.loc[:, 'New York City Population'])
pop_diff = np.diff(z)
print(pop_diff)



