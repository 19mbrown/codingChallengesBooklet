# PROTOTYPE

horse = {
        "name": "Horse",
        "legs": 4,
        "land": "yes",
        "pet": "yes",
        "stripe": "no"
    }

dolphin = {
        "name": "Dolphin",
        "legs": 0,
        "land": "no",
        "pet": "no",
        "stripe": "no"
    }

userIn = dict()
userIn["legs"] = int(input("How many legs does it have? "))
userIn["land"] = input("Is it a land animal (yes/no)? ")
userIn["pet"] = input("Is it a pet? ")
userIn["stripe"] = input("Does it have stripes? ")

animals = [horse, dolphin]

for animal in animals:
    bak = animal.copy()
    bak.pop("name")
    if bak == userIn:
        print(animal["name"])
