import random
from player import Player
from enemy import Enemy
from time import sleep

class Engine:
    def roll_d20(self):
        return random.randint(1,20)

    
    def roll_d10(self):
        return random.randint(1,10)


    def roll_d6(self):
        return random.randint(1,6)


    def figth_mode(self, player: Player, enemy: Enemy):
        """
        --- FIGHT MODE ___
        player: PlayerClass
        enemy: EnemyClass
        """

        print("--- FIGHT MODE ___")
        print(f"{player.name} vs. {enemy.name}")

        INIT_PLAYER = self.roll_d10()
        INIT_ENEMY = self.roll_d10()

        if INIT_PLAYER > INIT_ENEMY:
            print(f"PLAYER ROLL: {INIT_PLAYER}")
            print(f"ENEMY ROLL: {INIT_ENEMY}")
            print("FIGHT OFF, CHICKEN")
        else:
            print("YOU GOT SOME TROUBLE, MATE")
            
        
