import time
import random
class Warrior:
    def __init__(self,name,hp,attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def attack2(self,enemy):
        enemy.hp -= self.attack

    def w1hud(self):
        print("\nThor's HP:",self.hp,"\nThor's Damage:",self.attack)
    
    def w2hud(self):
        print("\nHulk's HP:",self.hp,"\nHulk's Damage:",self.attack)
      
warrior1 = Warrior("Thor",random.randint(60,100),random.randint(4,10))
warrior2 = Warrior("Hulk",random.randint(75,130),random.randint(2,8))
Round = 0

while True:
    time.sleep(1)
    Round += 1
    print("\n::::: Round ->",Round,":::::")
    warrior1.w1hud()
    warrior1.attack2(warrior2)
    if warrior2.hp <= 0:
        print("\nThor Wins With a Thunderous Victory!\n")
        break
    else:
        warrior2.w2hud()
        warrior2.attack2(warrior1)
        if warrior1.hp <=0:
            print("\nHulk Wins In A Smashing Victory!\n")
            break
        
