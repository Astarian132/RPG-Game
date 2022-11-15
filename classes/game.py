import random
# from .magic import Spell
# import pprint



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, defence, magic, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atk_low = atk - 10
        self.atk_high = atk + 10
        self.defence = defence
        self.magic = magic
        self.items = items
        self.actions = ['Attack', 'Magic', 'Items']


    def generate_damage(self):
        return random.randrange(self.atk_low, self.atk_high)

    def take_damage(self, dmg):
        self.hp -= dmg              # to samo co self.hp = self.hp - dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp
    
    def get_max_mp(self):
        return self.maxmp
    
    def reduce_mp(self, cost):
        self.mp -= cost

    
    def choose_action(self):
        i = 1
        print("\n    " + bcolors.BOLD + self.name + bcolors.ENDC)
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "    ACTIONS" + bcolors.ENDC)
        for item in self.actions:
            print("        " + str(i) + ":", item)
            i += 1
            
    def choose_magic(self):
        i = 1

        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "    MAGIC" + bcolors.ENDC)
        for spell in self.magic:
            print("        " + str(i) + ":", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1

        print("\n" + bcolors.OKGREEN + bcolors.BOLD + "    ITEMS:" + bcolors.ENDC)
        for item in self.items:
            print("        " + str(i) + ".", item["item"].name, ":", item["item"].description, " (x" + str(item["quantity"]), ")")
            i += 1


    def choose_target(self, enemies):
        i = 0
        print("\n" + bcolors.FAIL + bcolors.BOLD + "    TARGET:" + bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp() > 0:
                print("        " + str(i+1) + "." + enemy.name)
                i += 1
        choice = int(input("    Choose target: ")) - 1
        return choice




    def get_enemy_stats(self):
        enemy_hp_bar = ""
        enemy_hp_ticks = (self.hp / self.maxhp) * 50        #(* 50 / 2)
        enemy_mp_bar = ""
        enemy_mp_ticks = (self.mp / self.maxmp) * 10
        while enemy_hp_ticks > 0:
            enemy_hp_bar +="█"
            enemy_hp_ticks -= 1



        while len(enemy_hp_bar) < 50:
            enemy_hp_bar += " "

        enemy_hp_space = ""

        if len(str(self.hp)) < len(str(self.maxhp)):
            enemy_hp_decreased = len(str(self.maxhp)) - len(str(self.hp))
            while enemy_hp_decreased > 0:
                enemy_hp_space += " "
                enemy_hp_decreased -= 1
        elif len(str(self.hp)) < 4:
            enemy_hp_decreased = 4 - len(str(self.hp))
            while enemy_hp_decreased > 0:
                enemy_hp_space += "  "
                enemy_hp_decreased -= 1

        while enemy_mp_ticks > 0:
            enemy_mp_bar += "█"
            enemy_mp_ticks -= 1

        while len(enemy_mp_bar) < 10:
            enemy_mp_bar += " "

        enemy_mp_space = ""
        if len(str(self.mp)) < len(str(self.maxmp)):
            enemy_mp_decreased = len(str(self.maxmp)) - len(str(self.mp))
            while enemy_mp_decreased > 0:
                enemy_mp_space += " "
                enemy_mp_decreased -= 1


        print("                     " + bcolors.BOLD + "__________________________________________________             __________" + bcolors.ENDC)
        print(bcolors.BOLD + bcolors.FAIL + self.name + "      " + enemy_hp_space + str(self.hp) + "/" + str(self.maxhp)
              + bcolors.ENDC + bcolors.BOLD + "|" + bcolors.OKGREEN + enemy_hp_bar + bcolors.ENDC + bcolors.BOLD +
              "|      " + enemy_mp_space + str(self.mp)+ "/" + str(self.maxmp) + "|" + bcolors.OKBLUE + enemy_mp_bar +
              bcolors.ENDC + bcolors.BOLD + "|" + bcolors.ENDC)


    def get_stats(self):
        hp_bar = ""
        hp_ticks = (self.hp / self.maxhp) * 25             #(* 100 / 4)

        mp_bar = ""
        mp_ticks = (self.mp / self.maxmp) * 10             #(* 100 / 10)

        while hp_ticks > 0:
            hp_bar +="█"
            hp_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        hp_space = ""

        if len(str(self.hp)) < len(str(self.maxhp)):
            hp_decreased = len(str(self.maxhp)) - len(str(self.hp))
            while hp_decreased > 0:
                hp_space += " "
                hp_decreased -= 1


        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        mp_space = ""
        if len(str(self.mp)) < len(str(self.maxmp)):
            mp_decreased = len(str(self.maxmp)) - len(str(self.mp))
            while mp_decreased > 0:
                mp_space += " "
                mp_decreased -= 1


        print("                   " + bcolors.BOLD + "_________________________             __________" + bcolors.ENDC)
        print(bcolors.BOLD + self.name + "      " + hp_space + str(self.hp) + "/" + str(self.maxhp) + "|" + bcolors.OKGREEN +
              hp_bar + bcolors.ENDC + bcolors.BOLD + "|      " + mp_space + str(self.mp)+ "/" + str(self.maxmp)
              + "|" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + bcolors.BOLD + "|" + bcolors.ENDC)



    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.generate_damage()
        pct = self.hp / self.maxhp * 100


        if self.mp < spell.cost or spell.type == "white" and pct > 50:
            self.choose_enemy_spell()
        else:
            return spell, magic_dmg
