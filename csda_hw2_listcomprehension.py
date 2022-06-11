import pandas as pd

price = []
maintenance_cost = []
num_doors = []
num_passengers = []
luggage_cap = []
safety_rating = []
vehicle_classification = []

f = open("cars-sample35.txt", "r")
for x in f:
    #print(x)
    y = x.split(",")
    #print(y)
    price.append(y[0])
    maintenance_cost.append(y[1])
    num_doors.append(y[2])
    num_passengers.append(y[3])
    luggage_cap.append(y[4])
    safety_rating.append(y[5])
    #y[6].replace("\n", "")
    vehicle_classification.append(y[6])

f.close

#print(price)
#print(vehicle_classification)

data = {
    "Price": price,
    "Maintenence Cost": maintenance_cost,
    "Number of Doors": num_doors,
    "Number of Passengers": num_passengers,
    "Luggage Capacity": luggage_cap,
    "Safety Rating": safety_rating,
    "Classification of Vehicle": vehicle_classification
}

df = pd.DataFrame(data)
print(df)

# number3
price_med = []
i = 0
for a in price:
    if a == "med":
        price_med.append(i)
    i += 1
print(price_med)

# number6 (incomplete)
price_med2 = [price.index(z) for z in price if z == "med"]
print(price_med2)

# number4
num_pass_price_med = []
for a in price_med:
    num_pass_price_med.append(num_passengers[a])
print(num_pass_price_med)

# number7
num_pass_price_med2 = [num_passengers[z] for z in price_med]
print(num_pass_price_med2)

#number5
price_high = []
i = 0
for a in price:
    if a == "high":
        price_high.append(i)
    i += 1
#print(price_high)
high_price_high_maintenance = []
for a in price_high:
    if maintenance_cost[a] != "low":
        high_price_high_maintenance.append(a)
print(high_price_high_maintenance)

#number8
high_price_high_maintenance2 =[z for z in price_high if maintenance_cost[z] != "low"]
print(high_price_high_maintenance2)

#number9
nlist = [[1,2,3],['A','B','C'],[4,5],['D','E']]
nlist2 = [z for z in nlist for z in z]
print(nlist2)