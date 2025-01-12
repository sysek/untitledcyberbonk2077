from engine import Engine
from player import Player
from enemy import Enemy

# ENGINE SECTIONS
eng = Engine()

# PLAYER SECTION
player = Player("キーウィ")

# DUMMY SECTION
dummykid = Enemy()


# GAME TEST 

player.show_stats()
print("")
dummykid.show_dummy()

roll = eng.roll_d20()

if roll < 10:
    eng.figth_mode(player, dummykid)
    
