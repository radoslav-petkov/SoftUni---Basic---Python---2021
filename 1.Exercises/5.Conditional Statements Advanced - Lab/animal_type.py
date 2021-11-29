animal = input()

if animal == "dog":
    animal_type = "mammal"
elif animal in "crocodile tortoise snake":
    animal_type = "reptile"
else:
    animal_type = "unknown"

print(animal_type)
