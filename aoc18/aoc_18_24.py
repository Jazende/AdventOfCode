import re
from functools import partial
import operator
import time

with open(r'aoc_18_24.txt', 'r') as f:
    raw_input = f.read()

# with open(r'aoc_18_24_test.txt', 'r') as f:
#     raw_input = f.read()

re_units = re.compile('(?P<units>\d*) units each with (?P<hp>\d*) hit points\s?\(?.*?\)?\s?with an attack that does (?P<dmg>\d*) (?P<type>\w*) damage at initiative (\d*)')
re_weak = re.compile('weak to (\w+),?\s?(\w+)?') 
re_immune = re.compile('immune to (\w+),?\s?(\w+)?') 


def not_empty(func):
    def dec(*args, **kwargs):
        if args[1] == "":
            return
        return func(*args, **kwargs)
    return dec

def calculate_damage(unit_targetted, unit_attacking):
    damage_inflicted = unit_attacking.effective_power
    if unit_attacking.type in unit_targetted.weak:
        damage_inflicted *= 2
    if unit_attacking.type in unit_targetted.immune:
        damage_inflicted *= 0
    return damage_inflicted

class Fighter:
    @staticmethod
    def infection_lives():
        return sum([group.units for group in Fighter.faction_infection])
    @staticmethod
    def immune_lives():
        return sum([group.units for group in Fighter.faction_immune])

    faction_immune = []
    faction_infection = []

    @property
    def effective_power(self):
        return self.units * self.damage

    def target(self):
        possible_targets_group = Fighter.faction_immune if self.side == "infection" else Fighter.faction_infection
        eligible_targets = [target for target in possible_targets_group if target.targeted_by is None and not self.type in target.immune]
        if len(eligible_targets) == 0:
            return None
        target = max(eligible_targets, key = lambda x: self.targeting_priority(x))
        if calculate_damage(target, self) == 0:
            return
        self.targetting = target
        target.targeted_by = self
        return

    def targeting_priority(self, target):
        dmg = calculate_damage(target, self) * 1000
        dmg += target.effective_power
        dmg += target.initiative / 1000
        return dmg

    def __init__(self, units, hp, damage, type, initiative, side):
        self.id = len(Fighter.faction_immune) + 1 if side == "immune" else len(Fighter.faction_infection) + 1
        self.units = int(units)
        self.hp = int(hp)
        self.damage = int(damage)
        self.type = type
        self.initiative = int(initiative)
        self.side = side
        self.weak = []
        self.immune = []
        self.targeted_by = None
        self.targetting = None

        if side == "immune":
            Fighter.faction_immune.append(self)
        if side == "infection":
            Fighter.faction_infection.append(self)

    @not_empty
    def add_weakness(self, type):
        self.weak.append(type)
    
    @not_empty
    def add_immunity(self, type):
        self.immune.append(type)

    def __repr__(self):
        return f'{self.side} {self.id}'

    def attack(self):
        damage_inflicted = calculate_damage(self.targetting, self)
        units_killed = min(damage_inflicted // self.targetting.hp, self.targetting.units)
        self.targetting.units -= units_killed

def make_groups(raw_input):
    fighters = []
    side = None

    for line in raw_input.strip().split('\n'):
        side = "immune" if "Immune" in line else "infection" if "Infection" in line else side

        settings = re_units.findall(line)
        if not settings:
            continue
        
        weak = re_weak.findall(line)
        immune = re_immune.findall(line)

        fighter = Fighter(units=settings[0][0], hp=settings[0][1], damage=settings[0][2], type=settings[0][3], initiative=settings[0][4], side=side)

        if weak:
            for weakness in weak[0]:
                fighter.add_weakness(weakness)
        if immune:
            for immunity in immune[0]:
                fighter.add_immunity(immunity)
        
        fighters.append(fighter)
    
    return fighters

def solution(raw_input, boost=0):
    Fighter.faction_immune = []
    Fighter.faction_infection = []

    fighters = make_groups(raw_input)

    # Boost immune system
    if boost > 0:
        for group in Fighter.faction_immune:
            group.damage += boost

    while True:
        # Cleanup
        fighters = [fighter for fighter in fighters if fighter.units > 0]
        for fighter in fighters:
            fighter.targetting = None
            fighter.targeted_by = None

        # targetting Phase
        targeting_order = sorted(fighters, key=lambda tar: tar.effective_power*1000 + tar.initiative/1000, reverse=True)
        for fighter in targeting_order:
            fighter.target()
        
        # Attacking
        attacking_order = sorted(fighters, key=lambda attacker: attacker.initiative, reverse=True)
        for fighter in attacking_order:
            if fighter.targetting is None:
                continue
            if fighter.units > 0:
                fighter.attack()

        if Fighter.infection_lives() == 0:
            return Fighter.immune_lives()
        if Fighter.immune_lives() == 0:
            return 0 - Fighter.infection_lives()
        
        if all([calculate_damage(fighter.targetting, fighter) < fighter.targetting.hp for fighter in fighters if not fighter.targetting is None]):
            return -1


def day_one(raw_input):
    answer = abs(solution(raw_input))
    print(answer)
    return answer

def day_two(raw_input):
    boost = 0
    while True:
        if solution(raw_input, boost=boost) > 0:
            break
        boost += 1
    print(boost)
    return boost

day_one(raw_input)
day_two(raw_input)