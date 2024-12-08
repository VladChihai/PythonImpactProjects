class MyPet:

    def __init__(pet, name, age, color):
        pet.name = name
        pet.age = age
        pet.color = color
cat = MyPet("Ciorni", 1, "Black")
print("    My Cat")
print("Name =", cat.name)
print("Age =",cat.age)
print("Color =",cat.color)

