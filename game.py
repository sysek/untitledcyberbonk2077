from os import system, name
from random import randint
from player import Player
from enemy import Enemy


class Game:
    def roll_d20(self):
        return randint(1, 20)

    def roll_d10(self):
        return randint(1, 10)

    def roll_d6(self):
        return randint(1, 6)

    def clean_screen(self):
        if name == "nt":
            _ = system("cls")
        else:
            _ = system("clear")

    def figth_mode(self, player: Player, enemy: Enemy):
        """
        --- FIGHT MODE ___
        player: Player Class
        enemy: Enemy Class

        Funkcja wykorzystywana w przypadku gdy gracz napotka na przeciwnika.
        Jest to bardzo wczesna funkcja do rozbudowania.
        """
        STATUS = None
        FIGHT = True
        MA = [1, 1]

        while FIGHT:
            print("### FIGHT MODE ###")
            print(f"{player.name} vs. {enemy.name}")

            INIT_PLAYER = self.roll_d10 + player.STATs["REF"]
            INIT_ENEMY = self.roll_d10()

            PLAYER_HP = player.HP
            ENEMY_HP = enemy.HP

            print(f"PLAYER ROLL: {INIT_PLAYER}")
            print(f"ENEMY ROLL: {INIT_ENEMY}")

            if INIT_PLAYER > INIT_ENEMY:
                print("FIGHT OFF, CHICKEN")
                STATUS = 0  # brak walki
            else:
                self.clean_screen()
                print("YOU GOT SOME TROUBLE, MATE")
                STATUS = 1  # walka

                count = MA.count(1)
                if count > 0:
                    count_left = count
                    print(f"You have {count}/{count_left} AP")
                    print(f"Your HP:  {player.hp}")
                    print(f"Enemy HP: {enemy.hp}")
                    print("What to do?")
                    choose = input(">___")

                    if choose == "h":
                        player_hit = self.roll_d6()
                        print(f"{player.name} hits {player_hit}")

        return STATUS

    def stats(self):
        """
        Funkcja do generowania statystyk dla gracza
        """

        STATs = {
            "INT": 0,
            "REF": 0,
            "DEX": 0,
            "TECH": 0,
            "COOL": 0,
            "WILL": 0,
            "LUCK": 0,
            "MOVE": 0,
            "BODY": 0,
            "EMP": 0
        }

        for k, v in STATs.items():
            STATs[k] = randint(1, 10)

        return STATs
