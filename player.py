

class Player:
    STATs = {
        "INT": 5,
        "REF": 7,
        "DEX": 7,
        "TECH": 7,
        "COOL": 7,
        "WILL": 5,
        "LUCK": 8,
        "MOVE": 6,
        "BODY": 5,
        "EMP": 5
    }

    HP = 0
    HP_MAX = 0
    
    def __init__(self, name):
        self.HP = 35
        self.HP_MAX = 35
        self.name = name
    
    def show_stats(self):
        print(f"Name: {self.name}")
        print(f"HP: {self.HP}/{self.HP_MAX}")

        for k, v in self.STATs.items():
            print(f"{k}: {v}")
        
