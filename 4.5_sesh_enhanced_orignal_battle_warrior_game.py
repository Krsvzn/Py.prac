import time
import random
class Warrior:
    def __init__(self,name,hp,attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def attack2(self,enemy):
        enemy.hp -= self.attack

    def hud(self):
        print("\n",self.name,"'s HP ->",self.hp,"\n",self.name,"'s Damage ->",self.attack)
    
class Mage(Warrior):
    def heal(self):
        self.hp += 20

    def ability_hud(self):
        print("\n",self.name,"'s HP ->",self.hp,"\n",self.name,"'s Ability ->","+20HP")
      
warrior1 = Warrior("Thor",random.randint(60,100),random.randint(4,10))
warrior2 = Mage("Mage",random.randint(45,70),random.randint(3,7))
Round = 0

while True:
    time.sleep(1)
    Round += 1
    print("\n::::: Round ->",Round,":::::")
    warrior1.hud()
    warrior1.attack2(warrior2)
    if warrior2.hp <= 0:
        print("\nThor Wins With a Thunderous Victory!\n")
        break
    else:
        special_ability = random.randint(1,6)
        if special_ability == 1:
            warrior2.ability_hud()
            warrior2.heal()
        else:
         warrior2.hud()
         warrior2.attack2(warrior1)
        if warrior1.hp <=0:
            print("\nMage Wins In A Magical Victory!\n")
            break
        
