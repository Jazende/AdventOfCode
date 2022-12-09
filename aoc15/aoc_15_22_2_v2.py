from copy import copy
from random import randint

def fight(player, boss, hard=False, log=True):
    order = [player, boss]
    idx = 0
    if log:
        print()
        print("---   ---   ---   ---")
        print("    Combat starts    ")
        print("---   ---   ---   ---")
        print()

    while True:
        if hard and idx % 2 == 0:
            if log:
                print("Player suffers 1 HM damage.")
            player.hit_points -= 1
        if any([x.alive == False for x in order]):
            break
        player._handle_recharge(log)
        player._handle_shield(log)
        boss._handle_poison(log)
        if any([x.alive == False for x in order]):
            break
        if log:
            print(order)
        order[idx%2].attack(order[(idx+1)%2], log)
        idx += 1
        if any([x.alive == False for x in order]):
            break
        if log:
            print(f"{player.mana} mana left.")
            print("")
    if log:
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

    def _handle_poison(self, log):
        if self._poison_state:
            self._poison_duration -= 1
            self.hit_points -= 3
            if log:
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

    def attack(self, other, log):
        if log:
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

    def _handle_shield(self, log):
        if self._shield_state:
            self._shield_duration -= 1
            if self._shield_duration == 0:
                if log:
                    print("Shield has faded.")
                self.armor -= 7
            else:
                if log:
                    print(f"Shield blocks 7 damage. {self._shield_duration} ticks remaining.")
        if self._shield_duration == 0:
            self._shield_state = False

    def _handle_recharge(self, log):
        if self._recharge_state:
            self._recharge_duration -= 1
            self.mana += 101
            if log:
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

    def attack(self, other, log):
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
        if log:
            print(f">>> Casting: {spell}")

    @property
    def alive(self):
        if self.hit_points > 0:
            return True
        return False

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
    p = ["poison", "recharge", "shield", "poison", "recharge", "drain", "poison", "drain", "missile"]
    cast_count += 1
    spell = p[min(len(p)-1, cast_count)]
    if spell in spells:
        return spell

player = PC(50, 500)
boss = NPC(55, 8)
player.spell_priority = day_two_priority
fight(player, boss, hard=True, log=False)

print(f"{player._mana_used} mana was used.")