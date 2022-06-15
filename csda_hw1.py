import math


#Longest Collatz sequence
maxval = 0
maxnum = 0

for x in range(2,1000000):
    #print("Start: " + str(x))
    if (x % 100000) == 0:
        print(x)
    y = x
    z = 1
    while y != 1:
        z += 1
        if (y % 2) == 0:
            y = y/2
        else:
            y = (y * 3) + 1
        #print(y)
    #print("End: " + str(z) + " numbers")
    if z > maxval:
        maxval = z
        maxnum = x
    
print("Max number is " + str(maxval) + " created by " + str(maxnum))


#Factorial Digit Sum
input = 100
fac = math.factorial(input)
dig = [int(x) for x in str(fac)]

sum = 0
for w in range(len(dig)):
    sum += dig[w]

print(fac)
print(dig)
print(sum)
