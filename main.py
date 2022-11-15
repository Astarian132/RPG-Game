from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random

print("\n\n")

#Create Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 12, 120, "black")

#Create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")
curaga = Spell("Curaga", 25, 500, "white")

# Create some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restore HP/MP of one party member", 9999)
megaelixer = Item("MegaElixer", "elixer", "Fully restore HP/MP of all party members", 9999)
grenade = Item("Grenade", "atack", "Deals 500 damage", 500)

player_magic = [fire, thunder, blizzard, meteor, cure, cura]
enemy_magic = [fire, meteor, curaga]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5} ,
                {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 5} ,
                {"item": megaelixer, "quantity": 2}, {"item": grenade, "quantity": 5}]

# Instantiate People
player1 = Person("Valos", 420, 65, 60, 34, player_magic, player_items)         # self jest używane jako obecne wystąpienie w danej klasie, dlatego przez self raz przypisujemy do zmiennej player wartości w klasie Person
player2 = Person("Nick ", 340, 65, 60, 34, player_magic, player_items)
player3 = Person("Robot", 380, 65, 60, 34, player_magic, player_items)

enemy1 = Person ("Imp  ", 150, 65, 50, 25, enemy_magic, [])
enemy2 = Person ("Magus", 2500, 65, 45, 25, enemy_magic, [])        # a raz tym samym sposobem przypisujemy do zmiennej enemy
enemy3 = Person ("Imp  ", 150, 65, 50, 25, enemy_magic, [])


players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]


running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATACKS!" + bcolors.ENDC)

while running:
        # print("==================")
        # print("\n")
        print("NAME                  HP                                    MP")
        for player in players:
                player.get_stats()
        print("\n")

        for enemy in enemies:
                enemy.get_enemy_stats()

        for player in players:
                player.choose_action()
                choice = input("    Choose action: ")
                index = int(choice) - 1
        #        print("You chose", index)
                if index == 0:
                        dmg = player.generate_damage()

                        enemy = player.choose_target(enemies)
                        enemies[enemy].take_damage(dmg)
                        print(player.name + " atacked " + enemies[enemy].name + " for ", dmg, " points of damage.")
                        if enemies[enemy].get_hp() == 0:
                                print(enemies[enemy].name.replace(" ", "") + " has died")
                                del enemies[enemy]

                        if len(enemies) == 0:
                                print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
                                running = False

                        elif len(players) == 0:
                                print(bcolors.FAIL + "Your enemy has defeated You" + bcolors.ENDC)
                                running = False
                elif index == 1:
                        player.choose_magic()
                        magic_choice = int(input("    Choose magic: ")) -1
                        if magic_choice == -1:
                                continue

                        spell = player.magic[magic_choice]
                        magic_dmg = spell.generate_damage()

                        current_mp = player.get_mp()

                        if spell.cost > current_mp:
                                print(bcolors.FAIL + "\nNot enough MP" + bcolors.ENDC)
                                continue

                        player.reduce_mp(spell.cost)

                        if spell.type == "white":
                                player.heal(magic_dmg)
                                print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + bcolors.ENDC)
                        elif spell.type == "black":
                                enemy = player.choose_target(enemies)
                                enemies[enemy].take_damage(magic_dmg)

                                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage"
                                + " to " + enemies[enemy].name.replace(" ", "") + bcolors.ENDC)

                        if enemies[enemy].get_hp() == 0:
                                print(enemies[enemy].name.replace(" ", "") + " has died")
                                del enemies[enemy]

                        if len(enemies) == 0:
                                print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
                                break


                elif index == 2:
                        player.choose_item()
                        item_choice = int(input("    Choose item: ")) - 1

                        if item_choice == -1:
                                continue

                        item = player.items[item_choice]["item"]
                        if player.items[item_choice]["quantity"] == 0:
                                print(bcolors.FAIL + "\n" + "None left..." + bcolors.ENDC)
                                continue

                        player.items[item_choice]["quantity"] -= 1

                        if item.type == "potion":
                                player.heal(item.prop)
                                print(bcolors.OKGREEN + "\n" + item.name + " heals for ", str(item.prop), "HP" + bcolors.ENDC)

                        elif item.type == "elixer":
                                if item.name == "MegaElixer":
                                        for i in players:
                                                i.hp = i.maxhp
                                                i = i.maxmp
                                else:
                                        player.hp = player.maxhp
                                        player.mp = player.maxmp
                                print(bcolors.OKGREEN + "\n" + item.name + " Fully restores HP/MP" + bcolors.ENDC)

                        elif item.type == "atack":
                                enemy = player.choose_target(enemies)
                                enemies[enemy].take_damage(item.prop)
                                print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage to "
                                + enemies[enemy].name.replace(" ", "") + bcolors.ENDC)

                        if enemies[enemy].get_hp() == 0:
                                print(enemies[enemy].name.replace(" ", "") + " has died")
                                del enemies[enemy]

                        if len(enemies) == 0:
                                print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
                                running = False
                                break

        for enemy in enemies:
                if enemy.get_hp():
                        enemy_choice = random.randrange(0, 2)
                        #enemy_choice = 1
                        if enemy_choice == 0:
                                enemy_target = random.randrange(0, len(players))
                                enemy_dmg = enemy.generate_damage()
                                players[enemy_target].take_damage(enemy_dmg)
                                print(enemy.name.replace(" ", "") + " atacks "
                                      + players[enemy_target].name.replace(" ", "") + " for ", enemy_dmg, "points of damage")

                                if players[enemy_target].get_hp() == 0:
                                        print(players[enemy_target].name.replace(" ", "") + " has died")
                                        del players[enemy_target]

                                if len(players) == 0:
                                        print(bcolors.FAIL + "Your enemy has defeated You" + bcolors.ENDC)
                                        running = False

                        elif enemy_choice == 1:
                                spell, magic_dmg = enemy.choose_enemy_spell()
                                print("Enemy chose", spell, " dealing ", magic_dmg)
                                if spell.type == "white":
                                        enemy.heal(magic_dmg)
                                        print(bcolors.OKBLUE + "\n" + spell.name + " heals " + enemy.name +
                                              " for ", str(magic_dmg), "HP." + bcolors.ENDC)
                                elif spell.type == "black":
                                        enemy_target = random.randrange(0, len(players))
                                        players[enemy_target].take_damage(magic_dmg)

                                        print(bcolors.OKBLUE + "\n"+ enemy.name.replace(" ", "") + "'s " + spell.name
                                              + " deals", str(magic_dmg), " points of damage"
                                              + " to " + players[enemy_target].name.replace(" ", "") + bcolors.ENDC)

                                        if players[enemy_target].get_hp() == 0:
                                                print(players[enemy_target].name.replace(" ", "") + " has died")
                                                del players[enemy_target]

                                        if len(players) == 0:
                                                print(bcolors.FAIL + "Your enemy has defeated You" + bcolors.ENDC)
                                                running = False



        print("------------------------------------------------")


