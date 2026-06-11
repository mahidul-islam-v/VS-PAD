my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}


vehicle2 = my_vehicle.copy()

print(vehicle2.items())

vehicle2['number_of_tires'] = 3

vehicle2.pop("mileage")

for x,y in vehicle2.items():
    print(x)