
fighters = []
heal_power = 10

class character():
    Name = ""
    Hp = 0
    Armor = 0
    Power = 0
    def __init__ (self,Name, Hp, Armor, Power):
        self.Name = Name
        self.Hp = Hp
        self.Armor = Armor
        self.Power = Power

class game(character):

    def heal(self):
        global heal_power
        self.Hp += heal_power
        print(self.Name + " Have ", self.Hp, " Hp left")

    def attacked(self,Damage):
        if self.Hp - Damage > 0:
            self.Hp -= Damage
            print(self.Name + " have ", self.Hp, " Hp lest")
            return True
        else:
            print(self.Name, "if death")
            return False

while 1:
    try:
        nr = int(input("How many personage are in the game?"))
        break

    except:
        print("Wrong data type")
        continue

for i in range(0, nr):
    name = input("Name: ")
    Hp = int(input("HP: "))
    Armor = int(input("Armor: "))
    Power = int(input("Power: "))
    fighters.append(game(name,Hp,Armor,Power))

alive = True
player1 = fighters[0]
player2 = fighters[1]

cur_player = player1
next_player = player2

while alive:
    print("Turn to chose for", cur_player.Name)
    print("Enter 1 for attack other player")
    print("Enter 2 for heall")
    print("Enter 3 to continue")
    move = int(input())

    if move == 1:
        alive = next_player.attacked(cur_player.Power)
    elif move == 2:
        cur_player.heal()
    elif move == 3:
        continue

    if cur_player == player1:
        cur_player = player2
        next_player = player1
    else:
        cur_player = player1
        next_player = player2