from typing import override
import random


class BattleError(Exception):
    pass

class Character:
    def __init__(self, name: str, health: float, attack_power: float):
        self._name = name
        self._health = health
        self._attack_power = attack_power
    
    def attack(self, other: Character):
        if not isinstance(other, Character):
            raise TypeError("Cannot attack a non-Character")

        print(f"⚔️  {self._name} attacks {other._name} for {self._attack_power} damage!")
        other.take_damage(self._attack_power)
        print(f"   {other._name} health: {other._health:.1f}")
    
    def take_damage(self, attack_power: float):
        if not self.is_alive():
            raise BattleError("Cannot attack a dead character")

        self._health -= attack_power
        print(f"💥 {self._name} takes {attack_power} damage!")

    def is_alive(self):
        return self._health > 0
    
    def __str__(self):
        return (f"{self._name}: Character Type: {self.__class__.__name__}, "
        f"Health = {self._health}, Attack Power = {self._attack_power}")


class Warrior(Character):
    def __init__(self, name: str, baseHealth: float, baseAttackPower: float, defense: float = 1.5):
        # Warrior modifiers: extra health and attack
        self.__WARRIOR_HEALTH_MODIFIER = 1.5
        self.__WARRIOR_ATTACK_MODIFIER = 1.2
        baseHealth *= self.__WARRIOR_HEALTH_MODIFIER
        baseAttackPower *= self.__WARRIOR_ATTACK_MODIFIER
        self._defense = defense
        super().__init__(name, baseHealth, baseAttackPower)

    @override
    def take_damage(self, attack_power: float):
        reduced_damage = attack_power / self._defense
        super().take_damage(reduced_damage)
        print(f"🛡️  {self._name}'s armor reduces damage by {attack_power - reduced_damage:.1f}!") # warriors take less damage - they have defense


class Mage(Character):
    def __init__(self, name: str, baseHealth: float, baseAttackPower: float, mana: int = 100, mana_cost: int = 50):
        # Mage modifiers: less health
        # Additionally, a mage has mana: if he has enough mana, he will cast a powerful spell attack,
        # otherwise his attack will be weaker
        self.__MAGE_HEALTH_MODIFIER = 0.8
        self.__MAGE_ATTACK_MODIFIER = 0.8
        baseHealth *= self.__MAGE_HEALTH_MODIFIER
        baseAttackPower *= self.__MAGE_ATTACK_MODIFIER
        self._mana = mana
        self._mana_cost = mana_cost
        super().__init__(name, baseHealth, baseAttackPower)

    @override
    def attack(self, other: Character):
        if not isinstance(other, Character):
            raise TypeError("Cannot attack a non-Character")

        if self._mana >= self._mana_cost:
            spell_attack = self._attack_power * (1.0 / self.__MAGE_ATTACK_MODIFIER) * 2 # 1.0 / 0.8 to counterbalance the 0.8 multiplier from baseAttackPower

            print(f"✨ {self._name} casts a powerful spell on {other._name} for {spell_attack} damage!")
            other.take_damage(spell_attack) 
            self._mana -= self._mana_cost
            print(f"   {self._name} mana: {self._mana:.1f}/{self._mana_cost}")
        else:
            print(f"💫 {self._name} casts a weak spell on {other._name} for {self._attack_power} damage!")
            other.take_damage(self._attack_power)
            print(f"   {self._name} mana: {self._mana:.1f}/{self._mana_cost} (not enough for powerful spell!)")

    def restore_mana(self, amount: int):
        self._mana += amount

    def get_mana(self):
        return self._mana


class Assassin(Character):
    def __init__(self, name: str, baseHealth: float, baseAttackPower: float, critChance: float = 25):
        # Assassin modifiers: less health
        self.__ASSASSIN_HEALTH_MODIFIER = 0.9
        baseHealth *= self.__ASSASSIN_HEALTH_MODIFIER
        self._critChance = critChance
        super().__init__(name, baseHealth, baseAttackPower)

    def get_crit_chance(self):
        return self._critChance

    def set_crit_chance(self, critChance: float):
        self._critChance = critChance

    @override
    def attack(self, other: Character):
        if not isinstance(other, Character):
            raise TypeError("Cannot attack a non-Character")
        
        if random.random() < self._critChance / 100.0:
            crit_damage = self._attack_power * 5
            print(f"🗡️  {self._name} lands a CRITICAL HIT on {other._name} for {crit_damage} damage!")
            other.take_damage(crit_damage)
            print(f"   {other._name} health: {other._health:.1f}")
        else:
            super().attack(other)

class Battle:
    def __init__(self, character1: Character, character2: Character):
        self.character1 = character1
        self.character2 = character2
    
    def start_battle(self):
        print("\n" + "="*60)
        print("⚔️  BATTLE BEGINS! ⚔️")
        print("="*60)
        print(f"\n{self.character1}")
        print(f"VS")
        print(f"{self.character2}\n")
        print("-"*60)
        
        round_count = 1
        while self.character1.is_alive() and self.character2.is_alive():
            print(f"\n🔥 ROUND {round_count} 🔥")
            print("-"*30)
            
            self.character1.attack(self.character2)
            if not self.character2.is_alive():
                print(f"\n💀 {self.character2._name} has been defeated!")
                print(f"🏆 {self.character1._name} wins the battle!")
                break
            
            print()  # Add spacing
            self.character2.attack(self.character1)
            if not self.character1.is_alive():
                print(f"\n💀 {self.character1._name} has been defeated!")
                print(f"🏆 {self.character2._name} wins the battle!")
                break
            
            round_count += 1
        
        print("\n" + "="*60)
        print("⚔️  BATTLE ENDED! ⚔️")
        print("="*60)

Markus = Character("Markus", 100, 20)
Malekith = Warrior("Malekith", 200, 50)
Gandalf = Mage("Gandalf", 100, 20)
Ezio = Assassin("Ezio", 100, 20)

battle = Battle(Markus, Malekith)
battle.start_battle()

battle2 = Battle(Gandalf, Ezio)
battle2.start_battle()

# Markus.attack(Malekith)
# Malekith.attack(Markus)
# Malekith.attack(Markus)
# try:
#     Malekith.attack("not good")
# except TypeError as e:
#     print(e)
# print(Markus.is_alive())
# print(Markus)
# print(Malekith)
# try:
#     Gandalf.attack(Markus)
# except BattleError as e:
#     print(e)
# Gandalf.attack(Malekith)
# Gandalf.attack(Malekith)
# Gandalf.attack(Malekith)
# print(Gandalf)
# print(Malekith)

# Ezio.attack(Malekith)
# Ezio.attack(Malekith)
# Ezio.attack(Malekith)
# print(Ezio)
# print(Malekith)