class Player:

    """
    Zmienna BODY - wykorzystywana do ubioru bohatera, trzymania broni etc.
    """
    BODY = {
        "HEAD": 0,
        "CHEST": 0,
        "LEFT_HAND": 0,
        "RIGHT_HAND": 0,
        "LEFT_LEG": 0,
        "RIGHT_LEG": 0
    }

    HP = 0
    HP_MAX = 0

    def __init__(self, name):
        self.HP = 35
        self.HP_MAX = 35
        self.name = name

    def show_stats(self, stats=None):
        print(f"Name: {self.name}")
        print(f"HP: {self.HP}/{self.HP_MAX}")

        for k, v in stats.items():
            print(k, v)
