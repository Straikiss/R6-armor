from player import Player
from weapon import Weapon

weapon = Weapon()
weapon.set_damage(28)
weapon.set_hits(3)

player = Player()
player.set_health(100)

health = int(player.hit_body_heavy(player.get_health(), weapon.get_hits(), weapon.get_damage()))

if health < 0:
    health = 0

print('Health left: ' + str(health))