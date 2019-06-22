import random

class Warrior:
    def __init__(self, name, attack_stat, defense_stat, health):
        self.name = name
        self.attack_stat = attack_stat
        self.defense_stat = defense_stat
        self.health = health
    def attack(self):
        attack_amt = self.attack_stat + random.randint(1,15)
        return attack_amt
    def defend(self):
        defense_amt = self.defense_stat + random.randint(1,15)
        return defense_amt
    
class Battle:
    def battleStart(self, Warrior1, Warrior2):
        playing = True
        while playing == True:
            self.turn = Warrior1
            if(self.turn == Warrior1):
                print("What would you like to do")
                print("1.Attack")
                print("2.Defend")
                selection = int(input("Make Selection: "))
                print("\n")
                if(selection == 1):
                    self.attacking(Warrior1, Warrior2)
                    if(self.attacking == "warrior has fallen"):
                        print("Game over")
                elif(selection == 2):
                    self.defending(Warrior1, Warrior2)
                self.turn = Warrior2
            if(self.turn == Warrior2):
                ai_choice = random.randint(1,2)
                if(ai_choice == 1):
                    self.attacking(Warrior1, Warrior2)
                    self.turn = Warrior1
                elif(ai_choice == 2):
                    self.defending(Warrior1, Warrior2)
                    self.turn = Warrior1

    def attacking(self, WarriorA, WarriorB):
        if(self.turn == WarriorA):
            print("Attack!")
            warriorA_attack = WarriorA.attack()
            WarriorB.health = WarriorB.health - warriorA_attack
            print("Battle Stats:")
            print("Iron Man Attack Amount: {}".format(warriorA_attack))
            print("Iron Man Health: {}".format(WarriorA.health))
            print("Cap America Health: {}\n".format(WarriorB.health))
        elif(self.turn == WarriorB):
            print("Attack!")
            warriorB_attack = WarriorB.attack()
            WarriorA.health = WarriorA.health - warriorB_attack
            print("Battle Stats:")
            print("Cap America Attack Amount: {}".format(warriorB_attack))
            print("Iron Man Health: {}".format(WarriorA.health))
            print("Cap America Health: {}\n".format(WarriorB.health))
        if(WarriorA.health <= 0 or WarriorB.health <= 0):
            return "warrior has fallen"
    def defending(self, WarriorA, WarriorB):
        if(self.turn == WarriorA):
            print("Defend!")
            warriorB_attack = WarriorB.attack()
            warriorA_defend = WarriorA.defend()
            WarriorA.health = WarriorA.health - warriorB_attack + warriorA_defend
            print("Battle Stats:")
            print("Iron Man Defend Amount: {}".format(warriorA_defend))
            print("Cap America Attack Amount: {}".format(warriorB_attack))
            print("Iron Man Health: {}".format(WarriorA.health))
            print("Cap America Health: {}\n".format(WarriorB.health))
        elif(self.turn == WarriorB):
            print("Defend!")
            warriorA_attack = WarriorA.attack()
            warriorB_defend = WarriorB.defend()
            WarriorB.health = WarriorB.health - warriorA_attack + warriorB_defend
            print("Battle Stats:")
            print("Cap America Defend Amount: {}".format(warriorB_defend))
            print("Iron Man Attack Amount: {}".format(warriorA_attack))
            print("Iron Man Health: {}".format(WarriorA.health))
            print("Cap America Health: {}\n".format(WarriorB.health))        

def main():
    Ironman = Warrior("IronMan", 2250, 1500, 20000)
    CapAmerica = Warrior("Captain America", 1750, 2000, 22000)

    battle = Battle()
    battle.battleStart(Ironman, CapAmerica)

main()