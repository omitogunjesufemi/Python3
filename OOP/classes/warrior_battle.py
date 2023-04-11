import random
import math

class Warrior:
    def __init__(self, name, health, attack_max=0, block_max=0):
        self.name = name
        self.health = health
        self.attack_max = attack_max
        self.block_max = block_max


    def attack(self):
        attack_amt = self.attack_max * (random.random() + .5)
        return attack_amt


    def block(self):
        block_amt = self.block_max * (random.random() + .5)
        return block_amt


class Battle:
    def start_fight(self, warrior_1, warrior_2):
        while True:
            if self.get_attack_result(warrior_1, warrior_2) == "Game Over":
                print("Game Over")
                break

            if self.get_attack_result(warrior_2, warrior_1) == "Game Over":
                print("Game Over")
                break


    @staticmethod
    def get_attack_result(warrior_a, warrior_b):

        attack_amt_warrior_a = warrior_a.attack()
        block_amt_warrior_b = warrior_b.block()
        damage_to_warrior_b = math.ceil(attack_amt_warrior_a
                                        - block_amt_warrior_b)
        warrior_b.health = warrior_b.health - damage_to_warrior_b
        print("{} attacks {} and deals {} damage"
              .format(warrior_a.name, warrior_b.name, damage_to_warrior_b))
        print("{} is down to {} health"
              .format(warrior_b.name, warrior_b.health))

        if warrior_b.health <= 0:
            print("{} has died and {} is victorious"
                  .format(warrior_b.name, warrior_a.name))
            return "Game Over"
        else:
            return "Fight Again"


def main():
    maximus = Warrior("Maximus", 50, 20, 10)
    galaxon = Warrior("Galaxon", 50, 20, 10)

    battle = Battle()
    battle.start_fight(maximus, galaxon)

main()
