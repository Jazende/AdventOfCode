from copy import copy

def fight(one, two):
    first = copy(max([one, two], key=lambda x: x.speed))
    second = copy(min([one, two], key=lambda x: x.speed))
    order = [first, second]
    idx = 0

    while True:
        if any([x.alive == False for x in order]):
            break
        order[idx%2].attack(order[(idx+1)%2])
        idx += 1
    # print(f"{[x for x in order if x.alive][0].__class__.__name__} wins.")
    if [x for x in order if x.alive][0].__class__.__name__ == "NPC":
        return 0
    else:
        return 1

class NPC:
    def __init__(self, hit_points, damage, armor):
        self.speed = 100
        self.hit_points = hit_points

        self.base_armor = armor
        self.base_damage = damage

        self.item_weapon = None
        self.item_armor = None
        self.item_ring_one = None
        self.item_ring_two = None

    @property
    def armor(self):
        armor = self.item_armor.armor if self.item_armor else 0
        ring_one = self.item_ring_one.armor if self.item_ring_one else 0
        ring_two = self.item_ring_two.armor if self.item_ring_two else 0
        return self.base_armor + armor + ring_one + ring_two

    @property
    def damage(self):
        weapon = self.item_weapon.damage if self.item_weapon else 0
        ring_one = self.item_ring_one.damage if self.item_ring_one else 0
        ring_two = self.item_ring_two.damage if self.item_ring_two else 0
        return self.base_damage + weapon + ring_one + ring_two

    @property
    def alive(self):
        if self.hit_points > 0:
            return True
        return False

    def attack(self, other):
        other.hit_points -= max(1, self.damage - other.armor)

    def __str__(self):
        return f"{self.__class__.__name__}: {self.hit_points} HP, {self.armor} A, {self.damage} D."

class PC(NPC):
    def __init__(self, *args):
        super().__init__(*args)
        self.speed = 110

class Item:
    def __init__(self, cost, damage, armor):
        self.cost = cost
        self.damage = damage
        self.armor = armor
        self.type = "Item"

    def __repr__(self):
        if self.cost == 0:
            return f"No {self.type}"
        else:
            rep = f"{self.type} ({self.cost}g):"
            if self.damage > 0:
                rep += f" +{self.damage}D"
            if self.armor > 0:
                rep += f" +{self.armor}A"
        return rep

class Weapon(Item):
    def __init__(self, *args):
        super().__init__(*args)
        self.type = "Weapon"
        
class Armor(Item):
    def __init__(self, *args):
        super().__init__(*args)
        self.type = "Armor"

class Ring(Item):
    def __init__(self, *args):
        super().__init__(*args)
        self.type = "Ring"

weapons = [
    Weapon(10, 5, 0),
    Weapon(25, 6, 0),
    Weapon(40, 7, 0),
    Weapon(74, 8, 0),
    Weapon(8, 4, 0), 
]

armors = [
    Armor(13, 0, 1),
    Armor(31, 0, 2),
    Armor(53, 0, 3),
    Armor(75, 0, 4),
    Armor(102, 0, 5),
    Armor(0, 0, 0),
]

rings = [
    Ring(25, 1, 0),
    Ring(50, 2, 0),
    Ring(100, 3, 0),
    Ring(20, 0, 1),
    Ring(40, 0, 2),
    Ring(80, 0, 3),
    Ring(0, 0, 0),
    Ring(0, 0, 0),
]

def all_valid_combinations():
    for weapon in weapons:
        for armor in armors:
            for ring in rings:
                other_rings = [x for x in rings if not x == ring]
                for o_ring in other_rings:
                    outfit = [weapon, armor, ring, o_ring]
                    yield outfit
    return

gen = all_valid_combinations()
loses = []
wins = []
while True:
    try:
        outfit = next(gen)
    except StopIteration:
        break
    new_player = PC(100, 0, 0)
    new_boss = NPC(100, 8, 2)
    new_player.item_weapon = outfit[0]
    new_player.item_armor = outfit[1]
    new_player.item_ring_one = outfit[2]
    new_player.item_ring_two = outfit[3]
    fight_result = fight(new_player, new_boss)

    if fight(new_player, new_boss) == 0:
        loses.append(outfit)
    else:
        wins.append(outfit)

print(min(wins, key=lambda x: sum([i.cost for i in x])))
m = min(wins, key=lambda x: sum([i.cost for i in x]))
print(sum([i.cost for i in m]))

print(max(loses, key=lambda x: sum([i.cost for i in x])))
m = max(loses, key=lambda x: sum([i.cost for i in x]))
print(sum([i.cost for i in m]))
