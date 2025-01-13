# from engine import Engine
from player import Player
from enemy import Enemy


class Game:
    def figth_mode(self, player: Player, enemy: Enemy):
        """
        --- FIGHT MODE ___
        player: Player Class
        enemy: Enemy Class
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

    def create_character(self):
        pass
