from copy import copy
from random import randint

def fight(player, boss, hard=False):
    order = [player, boss]
    idx = 0

    while True:
        print("Next Turn")
        if hard and idx % 2 == 0:
            player.hit_points -= 1
        if any([x.alive == False for x in order]):
            break
        player._handle_recharge()
        player._handle_shield()
        boss._handle_poison()
        if any([x.alive == False for x in order]):
            break
        print(order)
        order[idx%2].attack(order[(idx+1)%2])
        idx += 1
        print(f"{player.mana} mana left.")
        print("")
    
    print(f"{[x for x in order if x.alive][0].__class__.__name__} wins.")
    if [x for x in order if x.alive][0].__class__.__name__ == "NPC":
        return 0
    else:
        return 1

class Unit:
    def __repr__(self):
        return f"{self.__class__.__name__}: {self.hit_points}"

class NPC(Unit):
    def __init__(self, hit_points, damage):
        self.speed = 100
        self.hit_points = hit_points
        self.damage = damage
        self._poison_state = False
        self._poison_duration = 0

    def _handle_poison(self):
        if self._poison_state:
            self._poison_duration -= 1
            self.hit_points -= 3
            print(f"Ticked 3 poison damage, {self._poison_duration} ticks remaining.")
            if self._poison_duration == 0:
                print("Poison faded.")
        if self._poison_duration == 0:
            self._poison_state = False

    @property
    def alive(self):
        if self.hit_points > 0:
            return True
        return False

    def attack(self, other):
        print(f"{self.__class__.__name__} attacked for {max(1, self.damage - other.armor)}")
        other.hit_points -= max(1, self.damage - other.armor)

class PC(Unit):
    def __init__(self, hit_points, mana, spell_priority=None):
        self.speed = 110

        self.armor = 0
        self.hit_points = hit_points
        self.mana = mana

        self._recharge_state = False
        self._recharge_duration = 0
        self._shield_state = False
        self._shield_duration = 0

        self.spell_priority = spell_priority

        self._mana_used = 0
    
    def mana_used(self, value):
        self.mana -= value
        self._mana_used += value

    def _handle_shield(self):
        if self._shield_state:
            self._shield_duration -= 1
            if self._shield_duration == 0:
                print("Shield has faded.")
                self.armor -= 7
            else:
                print(f"Shield has {self._shield_duration} ticks remaining.")
        if self._shield_duration == 0:
            self._shield_state = False

    def _handle_recharge(self):
        if self._recharge_state:
            self._recharge_duration -= 1
            self.mana += 101
            if self._recharge_duration > 0:
                print(f"Recharge has returned 101 mana. {self._recharge_duration} ticks remaining.")
            else:
                print("Recharge has returned 101 mana and faded.")
        if self._recharge_duration == 0:
            self._recharge_state = False

    def get_castable_spells(self, other):
        spells = []
        if self.mana >= 53:
            spells.append("missile")
        if self.mana >= 73:
            spells.append("drain")
        if self.mana >= 113 and self._shield_state == False:
            spells.append("shield")
        if self.mana >= 173 and other._poison_state == False:
            spells.append("poison")
        if self.mana >= 229 and self._recharge_state == False:
            spells.append("recharge")
        return spells

    def attack(self, other):
        possible_spells = self.get_castable_spells(other)
        spell = self.spell_priority(possible_spells)
        if spell == "missile":
            other.hit_points -= 4
            self.mana_used(53)
        elif spell == "drain":
            self.hit_points += 2
            other.hit_points -= 2
            self.mana_used(73)
        elif spell == "shield":
            self.armor += 7
            self._shield_duration = 6
            self._shield_state = True
            self.mana_used(113)
        elif spell == "poison":
            other._poison_duration = 6
            other._poison_state = True
            self.mana_used(173)
        elif spell == "recharge":
            self._recharge_duration = 5
            self._recharge_state = True
            self.mana_used(229)
        print(f">>> Casting: {spell}")

    @property
    def alive(self):
        if self.hit_points > 0:
            return True
        return False

priority = lambda x: x[randint(0, len(x)-1)]
def explicit_priority_test(spells):
    if "poison" in spells:
        return "poison"
    if "missile" in spells:
        return "missile"

cast_count = -1
def explicit_priority_test_two(spells):
    global cast_count
    cast_count += 1
    if "recharge" in spells:
        return "recharge"
    if "shield" in spells:
        return "shield"
    if "drain" in spells and cast_count <= 3:
        return "drain"
    if "poison" in spells and cast_count <= 5:
        return "poison"
    if "missile" in spells:
        return "missile"
    return spell

cast_count = -1
def day_one_priority(spells):
    global cast_count
    cast_count += 1
    spell = ["poison", "recharge", "shield", "poison", "missile", "missile", "missile", "missile", "missile"][cast_count]
    if spell in spells:
        return spell

cast_count = -1
def day_two_priority(spells):
    global cast_count
    p = ["shield", "recharge", "poison", "shield", "recharge", "poison", "missile", "missile", "missile"]
    p = ["poison", "recharge", "shield",  "poison", "missile","shield", "missile"]
    cast_count += 1
    spell = p[min(len(p)-1, cast_count)]
    if spell in spells:
        return spell


# player = PC(10, 250)
# boss = NPC(13, 8)
# player.spell_priority = explicit_priority_test
# fight(player, boss)

player = PC(10, 250)
boss = NPC(14, 8)
player.spell_priority = explicit_priority_test_two
fight(player, boss)

# player = PC(50, 500)
# boss = NPC(55, 8)
# player.spell_priority = day_one_priority
# fight(player, boss)

# player = PC(50, 500)
# boss = NPC(55, 8)
# player.spell_priority = day_two_priority
# fight(player, boss, True)

print(f"{player._mana_used} mana was used.")