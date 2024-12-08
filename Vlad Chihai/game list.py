class video_games:

    def __init__(game, name, tip, age):
        game.name = name
        game.tip = tip
        game.age = age
    def nname(game):
        print("Name:",game.name)
    def ttip(game):
        print("Tip:",game.tip)
    def aage(game):
        print("Age:",game.age)


game1 = video_games("Project Zomboid", "Zombie Survival", 11)
print("Select")
print("1 = Name")
print("2 = Tip")
print("3 = Age")
a = input()

if a == '1' :
    game1.nname()
if a == '2':
    game1.ttip()
if a == '3':
    game1.aage()
else:
    print("Error")
