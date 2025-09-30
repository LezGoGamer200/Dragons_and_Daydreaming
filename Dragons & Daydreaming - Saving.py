import random
import os
import time
world_name="[Error]"
player_name_first="[Error]"
player_name_last="[Error]"
final_boss="[Error]"
health=100
choice="[Error]"
location="Starting Field"
day=1
enemies_killed=0
health_potions=0
in_town=False
has_map=False
flee=False
attack=False
inventory=["hands"]
bosses=["Drakon","Avos","Davilith","Belos","Daygon","Knightmare"]
cutscene_days=[1,3,6,8]
clear = lambda: os.system('cls')
clear()
locations=["starting field","star tree town","easton town","weston town","northston town","southston town","farover hill","halted river cave","ice field","dark peak mountain","yes","no","nm"]
starting_field_items=["sword","dagger"]
star_tree_town_items=["sword","dagger","war axe"]
easton_town_items=["sword","dagger","war axe","mace"]
weston_town_items=["sword","dagger","war axe","mace"]
southston_town_items=["sword","dagger","war axe","mace"]
northston_town_items=["sword","dagger","war axe","mace"]
farover_hill_items=["sword","dagger","mace"]
halted_river_cave_items=["sword","dagger","war axe","mace"]
ice_field_items=["sword","dagger","mace"]
dark_peak_items=["sword","dagger","war axe","mace","the dream cleaver"]
starting_field_monsters=["Big Rat","Wolf","Boar"]
star_tree_town_monsters=["Big Rat","Rabid Dog"]
easton_town_monsters=["Big Rat","Rabid Dog"]
weston_town_monsters=["Big Rat","Rabid Dog"]
southston_town_monsters=["Big Rat","Rabid Dog"]
northston_town_monsters=["Big Rat","Rabid Dog"]
farover_hill_monsters=["Big Rat","Wolf","Bear","Wild Dog"]
halted_river_cave_monsters=["Big Rat","Wolf","Bear","Wild Dog"]
ice_field_monsters=["Big Rat","Wolf","boar"]
dark_peak_monsters=["Bear","Wild Dog","Young Rock Drake"]
star_tree_npcs=["Vikky","Shirlee","Oakleigh","Aline","Ashlie"]
npc_name_star_tree=random.choice(star_tree_npcs)
has_met_star_npc=False
easton_npcs=["Brayden","Hadley","Harold","Ralphie","Nevil"]
npc_name_easton=random.choice(easton_npcs)
has_met_easton_npc=False
weston_npcs=["Brandon","Norm","Marlyn","Jep","Charlton"]
npc_name_weston=random.choice(weston_npcs)
has_met_weston_npc=False
northston_npcs=["Miles","Denton","Malakai","Cash","Darius"]
npc_name_northston=random.choice(northston_npcs)
has_met_northston_npc=False
southston_npcs=["Becky","Lianne","Alexina","Janele","Candace"]
npc_name_southston=random.choice(southston_npcs)
has_met_southston_npc=False
has_met_ethan=True
def typewrite(text, modifier=0,delay=0.06):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(delay+modifier)
    print()
base_path = os.path.join(os.path.dirname(__file__))
full_path = ""
def load_file(filename):
    global base_path
    # Construct full path to the file
    full_path = os.path.join(base_path, filename)
    return full_path
save_file_1=load_file("save_1.txt")
save_file_2=load_file("save_2.txt")
save_file_3=load_file("save_3.txt")
def save_game(save_file):
    global has_map, world_name, player_name_first, player_name_last, starting_field_items, star_tree_town_items, easton_town_items, weston_town_items, southston_town_items, northston_town_items, farover_hill_items, halted_river_cave_items, ice_field_items, dark_peak_items, location, npc_name_star_tree, has_met_star_npc, npc_name_easton, has_met_easton_npc, npc_name_weston, has_met_weston_npc, npc_name_northston, has_met_northston_npc, npc_name_southston, has_met_northston_npc, has_met_ethan, day, health, in_town, inventory, enemies_killed, health_potions
    file = open(save_file, "w")
    file.write(f"{player_name_first}\n") # Line 0
    file.write(f"{player_name_last}\n") # Line 1
    file.write(f"{world_name}\n") # Line 2
    file.write(f"{has_map}\n") # Line 3
    file.write(f"{location}\n") # Line 4
    file.write(f"{str(day)}\n") # Line 5
    file.write(f"{str(health)}\n") # Line 6
    file.write(f"{in_town}\n") # Line 7
    file.write(f"{str(day)}\n") # Line 8
    file.write(f"{str(enemies_killed)}\n") # Line 9
    file.write(f"{str(health_potions)}\n") # Line 10
    file.write(f"{str(inventory)}\n") # Line 11
    file.write(f"{str(starting_field_items)}\n") # Line 12
    file.write(f"{str(star_tree_town_items)}\n") # Line 13
    file.write(f"{str(easton_town_items)}\n") # Line 14
    file.write(f"{str(weston_town_items)}\n") # Line 15
    file.write(f"{str(southston_town_items)}\n") # Line 16
    file.write(f"{str(northston_town_items)}\n") # Line 17
    file.write(f"{str(farover_hill_items)}\n") # Line 18
    file.write(f"{str(halted_river_cave_items)}\n") # Line 19
    file.write(f"{str(ice_field_items)}\n") # Line 20
    file.write(f"{str(dark_peak_items)}\n") # Line 21
    file.write(f"{npc_name_star_tree}\n") # Line 22
    file.write(f"{has_met_star_npc}\n") # Line 23
    file.write(f"{npc_name_easton}\n") # Line 24
    file.write(f"{has_met_easton_npc}\n") # Line 25
    file.write(f"{npc_name_weston}\n") # Line 26
    file.write(f"{has_met_weston_npc}\n") # Line 27
    file.write(f"{npc_name_southston}\n") # Line 28
    file.write(f"{has_met_southston_npc}\n") # Line 29
    file.write(f"{npc_name_northston}\n") # Line 30
    file.write(f"{has_met_northston_npc}\n") # Line 31
    file.write(f"{has_met_ethan}") # Line 32
    file.close()
    typewrite("Saving Game.")
    typewrite("*************************", .94)
    typewrite("Game Saved.")
def read_save(save_file):
    global has_map, world_name, player_name_first, player_name_last, starting_field_items, star_tree_town_items, easton_town_items, weston_town_items, southston_town_items, northston_town_items, farover_hill_items, halted_river_cave_items, ice_field_items, dark_peak_items, location, npc_name_star_tree, has_met_star_npc, npc_name_easton, has_met_easton_npc, npc_name_weston, has_met_weston_npc, npc_name_northston, has_met_northston_npc, npc_name_southston, has_met_northston_npc, has_met_ethan, day, health, in_town, inventory, enemies_killed, health_potions
    file = open(save_file, "r")
    read = file.readlines()
    player_name_first_check = read[0]
    player_name_first = player_name_first_check.replace("\n", "")
    player_name_last_check = read[1]
    player_name_last = player_name_last_check.replace("\n", "")
    world_name_check = read[2]
    world_name = world_name_check.replace("\n", "")
    has_map = bool(read[3])
    location_check = read[4]
    location = location_check.replace("\n", "")
    day = int(read[5])
    health = int(read[6])
    in_town = bool(read[7])
    day = int(read[8])
    enemies_killed = int(read[9])
    health_potions = int(read[10])
    inventory_load = read[11]
    starting_field_items_load = read[12]
    star_tree_town_items_load = read[13]
    easton_town_items_load = read[14]
    weston_town_items_load = read[15]
    southston_town_items_load = read[16]
    northston_town_items_load = read[17]
    farover_hill_items_load = read[18]
    halted_river_cave_items_load = read[19]
    ice_field_items_load = read[20]
    dark_peak_items_load = read[21]
    npc_name_star_tree_check = read[22]
    npc_name_star_tree = npc_name_star_tree_check.replace("\n", "")
    has_met_star_npc = bool(read[23])
    npc_name_easton_check = read[24]
    npc_name_easton = npc_name_easton_check.replace("\n", "")
    has_met_easton_npc = bool(read[25])
    npc_name_weston_check = read[26]
    npc_name_weston = npc_name_weston_check.replace("\n", "")
    has_met_weston_npc = bool(read[27])
    npc_name_southston_check = read[28]
    npc_name_southston = npc_name_southston_check.replace("\n", "")
    has_met_southston_npc = bool(read[29])
    npc_name_northston_check = read[30]
    npc_name_northston = npc_name_northston_check.replace("\n", "")
    has_met_northston_npc = bool(read[31])
    has_met_ethan = bool(read[32])
    file.close()
    if "dagger" in inventory_load:
        inventory.append("dagger")
    if "sword" in inventory_load:
        inventory.append("sword")
    if "war axe" in inventory_load:
        inventory.append("war axe")
    if "mace" in inventory_load:
        inventory.append("mace")
    if "the dream cleaver" in inventory_load:
        inventory.append("the dream cleaver")
    i=0
    while i <= health_potions:
        inventory.append("health potion")
        i+=1
    starting_field_items=[]
    star_tree_town_items=[]
    easton_town_items=[]
    weston_town_items=[]
    southston_town_items=[]
    northston_town_items=[]
    farover_hill_items=[]
    halted_river_cave_items=[]
    ice_field_items=[]
    dark_peak_items=[]
    if "sword" in dark_peak_items_load:
        starting_field_items.append("sword")
        star_tree_town_items.append("sword")
        easton_town_items.append("sword")
        weston_town_items.append("sword")
        southston_town_items.append("sword")
        northston_town_items.append("sword")
        farover_hill_items.append("sword")
        halted_river_cave_items.append("sword")
        ice_field_items.append("sword")
        dark_peak_items.append("sword")
    if "dagger" in dark_peak_items_load:
        starting_field_items.append("dagger")
        star_tree_town_items.append("dagger")
        easton_town_items.append("dagger")
        weston_town_items.append("dagger")
        southston_town_items.append("dagger")
        northston_town_items.append("dagger")
        farover_hill_items.append("dagger")
        halted_river_cave_items.append("dagger")
        ice_field_items.append("dagger")
        dark_peak_items.append("dagger")
    if "war axe" in dark_peak_items_load:
        star_tree_town_items.append("war axe")
        easton_town_items.append("war axe")
        weston_town_items.append("war axe")
        southston_town_items.append("war axe")
        northston_town_items.append("war axe")
        halted_river_cave_items.append("war axe")
        ice_field_items.append("war axe")
        dark_peak_items.append("war axe")
    if "mace" in dark_peak_items_load:
        easton_town_items.append("mace")
        weston_town_items.append("mace")
        southston_town_items.append("mace")
        northston_town_items.append("mace")
        farover_hill_items.append("mace")
        halted_river_cave_items.append("mace")
        ice_field_items.append("mace")
        dark_peak_items.append("mace")
    if "the dream cleaver" in dark_peak_items_load:
        dark_peak_items.append("the dream cleaver")
    typewrite("Loading file.")
    typewrite("*************************", .94)
    typewrite("File loaded.")
    console_clear()
    return has_map, world_name, player_name_first, player_name_last, starting_field_items, star_tree_town_items, easton_town_items, weston_town_items, southston_town_items, northston_town_items, farover_hill_items, halted_river_cave_items, ice_field_items, dark_peak_items, location, npc_name_star_tree, has_met_star_npc, npc_name_easton, has_met_easton_npc, npc_name_weston, has_met_weston_npc, npc_name_northston, has_met_northston_npc, npc_name_southston, has_met_northston_npc, has_met_ethan, day, health, in_town, inventory, enemies_killed, health_potions
def start():
    global world_name, player_name_first, player_name_last
    typewrite("Welcome to this land.          ",0.04)
    typewrite("Do you know who you are?          ",0.04)
    typewrite("Do you know where you are?          ",0.04)
    typewrite("Do you know why you are here?          ",0.04)
    typewrite("Do you know how you got here?          ",0.04)
    typewrite("I know the answers to all these questions but one. Who are you? What is your name?")
    player_name_first=input("[Please enter your first name]\n")
    player_name_last=input("[Please enter your last name]\n")
    if player_name_first=="":
        player_name_first="Bob"
    if player_name_last=="":
        player_name_last="Brody"
    typewrite(f"Ah yes, hello {player_name_first}.")
    typewrite("I shall tell you the rest of what I know later, if you don't figure it out for yourself.")
    typewrite(f"But I shall tell you one last thing before you go, this place is called {world_name}. Feel free to explore, but be careful, there is danger lurking about. Now,")
    typewrite("[???]'Hello? Hello! Wake up! Finally! Are you okay? I found you passed out in the middle of this field, & wanted to see if you were okay.'")
    typewrite(f"[{player_name_first} {player_name_last}]'Thank you, my name's {player_name_first}. What's yours?'")
    typewrite(f"[Ethan Dean]'You're welcome {player_name_first}. Also, my name is Ethan, Ethan Dean. And if you ever need a break from stressful things, you can find me in any of the towns around this place. If you can find me, I'll play a little game with you. Take care {player_name_first}!'")
    return player_name_first, player_name_last
def world():
    global world_name
    world_name_bank = ["Etheria","Anmestity","Pythagarea","Pythonaria","The Crystal Isles","Crystopia","Amgulmem","Gibbergh","Great Cooa","North Lingel","Neincreek","Buckcamsham","Conna","Merthallskaford","Moose Rathgowwral","Datenwood","Red Kerwkesster","Park Restval","Hillentain","Port Rdenwe","North Chaoak","North Fermoses","Middrntwood","Blaisevilnes","Tencavedon","Quoisasglen","End Ferry","South Hawkfea","Rostohill","Scrap Mechanica"]
    world_name=random.choice(world_name_bank)
    return world_name
def decision():
    global choice
    typewrite("What do you want to do? [Enter help to get a list of commands.]")
    choice=input()
    return choice
def greet_npc():
    global player_name_first, player_name_last, npc_name_star_tree, in_town, npc_name_easton, npc_name_northston, npc_name_southston, npc_name_weston, has_met_easton_npc, has_met_northston_npc, has_met_southston_npc, has_met_star_npc, has_met_weston_npc
    if in_town==True:
        if location=="Star Tree town":
            if has_met_star_npc==False:
                typewrite(f"[{player_name_first} {player_name_last}]'Hello there! My name is {player_name_first}. What's yours?'")
                typewrite(f"[{npc_name_star_tree}]'Hello! My name is {npc_name_star_tree}. Do you need anything?'")
                typewrite(f"[{player_name_first} {player_name_last}]'I'm trying to find out how I got here. Do you know of any place I can find some information about that? I can't seem to remember how I got here.'")
                typewrite(f"[{npc_name_star_tree}]'Um, I'm not sure. I do have some advice though. I find that some sleep tends to clear my mind. And perhaps someone from another town could help you.'")
                typewrite(f"[{player_name_first} {player_name_last}]'Thanks! See you!'")
            if has_met_star_npc==True:
                typewrite(f"[{player_name_first} {player_name_last}]'Hi {npc_name_star_tree}! Could you tell me what you said last time please?'")
                typewrite(f"[{npc_name_star_tree}]'It's okay {player_name_first}. I'm pretty sure you're having some memory problem. But to just to remind you, I advised you to try resting.' [Use the command 'rest']")
                typewrite(f"[{player_name_first} {player_name_last}]'Thanks! See you!'")
        if location=="Easton town":
            if has_met_easton_npc==False:
                typewrite(f"[{player_name_first} {player_name_last}]'Hello there! My name is {player_name_first}. What's yours?'")
                typewrite(f"[{npc_name_easton}]'Hello! My name is {npc_name_easton}. Do you need anything?'")
                typewrite(f"[{player_name_first} {player_name_last}]'I'm trying to find out how I got here. Do you know of any place I can find some information about that? I can't seem to remember how I got here.'")
                typewrite(f"[{npc_name_easton}]'Um, I'm not sure. But some sleep might help you remember. Perhaps some other person could help more.'")
                typewrite(f"[{player_name_first} {player_name_last}]'Thanks! See you!'")
            if has_met_easton_npc==True:
                typewrite(f"[{player_name_first} {player_name_last}]'Hi {npc_name_easton}! Could you tell me what you said last time please?'")
                typewrite(f"[{npc_name_easton}]'It's okay {player_name_first}. I'm pretty sure  you're having some memory problem. But to just to remind you, some sleep might help you.' [Use the command 'rest']")
                typewrite(f"[{player_name_first} {player_name_last}]'Thanks! See you!'")
        if location=="Weston town":
            if has_met_weston_npc==False:
                typewrite(f"[{player_name_first} {player_name_last}]'Hello there! My name is {player_name_first}. What's yours?'")
                typewrite(f"[{npc_name_weston}]'Hello! My name is {npc_name_weston}. Do you need anything?'")
                typewrite(f"[{player_name_first} {player_name_last}]'I'm trying to find out how I got here. Do you know of any place I can find some information about that? I can't seem to remember how I got here.'")
                typewrite(f"[{npc_name_weston}]'Um, perhaps some sleep might do you good. Though I heard some rummors about a great big monster at the top of Dark Peak Mountain. Though you shouldn't go up there without perparing first.")
                typewrite(f"[{player_name_first} {player_name_last}]'Thanks! See you!'")
            if has_met_weston_npc==True:
                typewrite(f"[{player_name_first} {player_name_last}]'Hi {npc_name_weston}! Could you tell me what you said last time please?'")
                typewrite(f"[{npc_name_weston}]'It's okay {player_name_first}. I'm pretty sure you're having some memory problem. But to just to remind you, I recommended sleep. [Use the command 'rest'] And I told you about the existance of the monster of Dark Peak.'")
                typewrite(f"[{player_name_first} {player_name_last}]'Thanks! See you!'")
        if location=="Northston town":
            if has_met_northston_npc==False:
                typewrite(f"[{player_name_first} {player_name_last}]'Hello there! My name is {player_name_first}. What's yours?'")
                typewrite(f"[{npc_name_northston}]'Hello! My name is {npc_name_northston}. Do you need anything?'")
                typewrite(f"[{player_name_first} {player_name_last}]'I'm trying to find out how I got here. Do you know of any place I can find some information about that? I can't seem to remember how I got here.'")
                typewrite(f"[{npc_name_northston}]'Um, perhaps you should sleep. I find that does some good at times. Also, beware the monster of Dark Peak. do not go looking for them unprepared.'")
                typewrite(f"[{player_name_first} {player_name_last}]'Thanks! See you!'")
            if has_met_northston_npc==True:
                typewrite(f"[{player_name_first} {player_name_last}]'Hi {npc_name_northston}! Could you tell me what you said last time please?'")
                typewrite(f"[{npc_name_northston}]'It's okay {player_name_first}. I'm pretty sure you're having some memory problem. But to just to remind you, I told you to get some sleep. [Use the command 'rest'] I also told you to be careful about the monster of Dark Peak. Don't aproach unprepared.'")
                typewrite(f"[{player_name_first} {player_name_last}]'Thanks! See you!'")
        if location=="Southston town":
            if has_met_southston_npc==False:
                typewrite(f"[{player_name_first} {player_name_last}]'Hello there! My name is {player_name_first}. What's yours?'")
                typewrite(f"[{npc_name_southston}]'Hello! My name is {npc_name_southston}. Do you need anything?'")
                typewrite(f"[{player_name_first} {player_name_last}]'I'm trying to find out how I got here. Do you know of any place I can find some information about that? I can't seem to remember how I got here.'")
                typewrite(f"[{npc_name_southston}]'Lets see, here, you look like you could use some sleep. There are great places to sleep all over this land. Even on Dark Peak. But beware the monster that lives there. It's dangerous up there.'")
                typewrite(f"[{player_name_first} {player_name_last}]'Thanks! See you!'")
            if has_met_southston_npc==True:
                typewrite(f"[{player_name_first} {player_name_last}]'Hi {npc_name_southston}! Could you tell me what you said last time please?'")
                typewrite(f"[{npc_name_southston}]'It's okay {player_name_first}. I'm pretty sure you're having some memory problems. But to just to remind you, I told you to get some sleep. [Use the command 'rest'] Even Dark Peak has nice places to sleep. But be careful up there, the monster up there is very dangerous.'")
                typewrite(f"[{player_name_first} {player_name_last}]'Thanks! See you!'")
    elif in_town==False:
        typewrite("You can't see anyone to talk to!")
    return has_met_star_npc, has_met_easton_npc, has_met_weston_npc, has_met_northston_npc, has_met_southston_npc
def get_map():
    global has_map
    typewrite("You got a map! Now you can look at it at anytime!")
    has_map=True
    inventory.append("map")
    return has_map
def map():
    global location
    typewrite("You check your map")
    typewrite("------------------------------------------------------------------------------------------------",-.06)
    typewrite("|cff                                   fff          whhhhhw                             ..^^^^^|",-.06)
    typewrite("|fAf___   hhhhh                        cIf___________h.G.hw                             ..^^D^^|",-.06)
    typewrite("|fff   \__h.B.h__________              fff          whhhhhw                             ..^^c^^|",-.06)
    typewrite("|         hhhhh          \              |           www|www                             ....|..|",-.06)
    typewrite("|                         \____________/_\____________/_\___________________                /  |",-.06)
    typewrite("|                               |                      |                    \______________/   |",-.06)
    typewrite("|          .....                |                      |              ccc   /       www|www    |",-.06)
    typewrite("|          .^^^.              hhhhh                  hhhhh            cJc__/        whhhhhw    |",-.06)
    typewrite("|          .^F________________h.E.h                  h.H.h            ccc           wh.C.hw    |",-.06)
    typewrite("|          .^^^.              hhhhh                  hhhhh                          whhhhhw    |",-.06)
    typewrite("------------------------------------------------------------------------------------------------",-.06)
    typewrite("-Location Key-")
    typewrite("\tA-Starting Field\t B-Star Tree-Town\t C-Weston-Town\t D-Dark Peak-Mountain\t E-Easton-Town\n\t F-Farover Hill\t G-Northston-Town\t H-Southston-Town\t I-Ice field\t J-Halted River Cave\n\t",-.06)
    typewrite("\n-Symbol & Lowercase letter Key-",-.06)
    typewrite("\th-town/building/house\t f-field\t w-wall\t c-cave\t ^-elevation up\t _/\|-road",-.06)
    typewrite(f"-Current Location-\n\t {location}",-.06)
def check_inventory():
    typewrite("You have decided to check your inventory. Here is what you have:")
    if "dagger" in inventory:
        typewrite("Dagger")
    if "sword" in inventory:
        typewrite("Sword")
    if "war axe" in inventory:
        typewrite("War Axe")
    if "mace" in inventory:
        typewrite("Mace")
    if "the dream cleaver" in inventory:
        typewrite("The Dream Cleaver")
    if "health potion" in inventory:
        typewrite(f"Health Potion(s) ({health_potions})")
def star_tree_description():
    typewrite("Star Tree town is a very small but beautiful town. You like it here. The houses are beautiful works of architecture. The people out here seem to be very happy to be so far from Dark Peak Mountain, & it's monsters. You can see Dark Peak Mountain stretching up far into the sky even from all the way over here. That mountain is Huge.")
def easton_description():
    typewrite("Easton town is a very beautiful place. You can see a big hill off in the distance. Perhaps you could go there later? The people here are glad they can live so far from Dark Peak. They say everyone but Weston town fears it.")
def weston_description():
    typewrite("Weston town is surrounded by high walls, about 12 feet tall, & looks very intimidating, likely due to the fact that it's so close to Dark Peak Mountain. But inside those walls is a very beautiful town, though you can tell it has needed repairs more than once. It's main function is to mine useful resources from the nearby Halted River cave.")
def northston_description():
    typewrite("Northston town is surrounded by walls about 7 feet high, & it seems slightly intimidating, though you know it needs the walls, as it's the secound closest town to Dark Peak Mountain. It's needs it's protection to make the villagers feel safe. The town itself is a very bright & cheerful place, & you can see the walls do their job well.")
def southston_description():
    typewrite("Southston town is a nice place, it rarly is attack by monsters coming from dark peak, so even though it's the 3rd closest town to Dark Peak, it has no walls. You can see that southston is a nice, very happy place, as you can see it in the eyes & on the faces of the villagers that live here.")
def starting_field_description():
    typewrite("Starting field is the place you woke up, it's a very beautiful field, far removed from the troubles of Dark Peak. The only danger here is the wild animals. You can see the remenants of a battle fought here long ago, thought vegetation has grown back over the marred landscape. It's hard to see the battlefield anymore, but you can still see the weapons & armour of fallen soldiers.")
def farover_hill_description():
    typewrite("Farover hill is a big hill just outside of Easton town. You could see the hill when you approached the town, & it now seems a little bigger up close than you orignally thought when you first saw it.")
def ice_field_description():
    typewrite("Ice field is a large field near Northston town where the farmers of Northston do their farming. They're not very friendly to people they don't know, & refuse to talk to people. They do their farming this far from the town so that the crops don't get destoryed during the attacks on Northston by Dark Peak's monsters.")
def halted_river_cave_description():
    typewrite("Halted River cave is a dark cave only lit up by the occasional gap in the rock forming it's ceiling, or the torches lining it's walls,put there by the inhabitants of Weston town, as this is where they mine. Though there are some dangerous creatures living in the cave.")
def dark_peak_mountain_description():
    global world_name
    typewrite(f"Dark Peak Mountain is a very dangerous place. The monsters that live here are constanly attacking Weston town, & sometimes Northston town. There is said to be a big monster that lives near the top of this mountain that never leaves it, & only shows itself to those it deems worthy, & by that it means it will only show to kill those that disrupts the chaos it loves to create in the land of {world_name}. The monsters that live here will hunt you if you try to find the legendary Dream Cleaver, as it is the one weapon that can easily kill their master. Good Luck.")
def travel():
    global location, in_town
    travel_answer="[Error]"
    if location=="Starting Field":
        typewrite("You can go to Star Tree town. Do you wish to go there?")
        travel_answer=input("[Yes or No]\n")
        if travel_answer.lower()=="yes":
            typewrite("You travel to Star Tree town.")
            location="Star Tree town"
            in_town=True
            star_tree_description()
            return location
        if travel_answer.lower()=="no":
            typewrite("Okay, you stay where you are.")
    elif location=="Star Tree town":
        typewrite("You can go to, Starting Field, Easton town, Ice Field, Northston town, Southston town, Halted River Cave, Weston town, or Dark Peak mountain.[Enter nm to stop]")
        travel_answer=input("Where do you want to go?\n")
        if travel_answer.lower()=="starting field":
            typewrite("You traveled to the Starting Field.")
            location="Starting Field"
            starting_field_description()
            in_town=False
        if travel_answer.lower()=="easton town":
            typewrite("You traveled to Easton town.")
            location="Easton town"
            easton_description()
            in_town=True
        if travel_answer.lower()=="ice field":
            typewrite("You traveld to Ice Field.")
            location="Ice Field"
            ice_field_description()
            in_town=False
        if travel_answer.lower()=="northston town":
            typewrite("You traveled to Northston town.")
            location="Northston town"
            northston_description()
            in_town=True
        if travel_answer.lower()=="southston town":
            typewrite("You traveled to Southston town.")
            location="Southston town"
            southston_description()
            in_town=True
        if travel_answer.lower()=="halted river cave":
            typewrite("You traveld to Halted River Cave.")
            location="Halted River Cave"
            halted_river_cave_description()
            in_town=False
        if travel_answer.lower()=="weston town":
            typewrite("You traveled to Weston town.")
            location="Weston town"
            weston_description()
            in_town=True
        if travel_answer.lower()=="dark peak mountain":
            typewrite("You traveled to the dark & dangerous Dark Peak.")
            location="Dark Peak"
            dark_peak_mountain_description()
            in_town=False
        if travel_answer.lower()=="nm":
            typewrite("Ok, you stay where you are.")
        return location
    elif location=="Easton town":
        typewrite("You can go to, Star Tree town, Farover Hill, Ice Field, Northston town, Southston town, Halted River Cave, Weston town, or Dark Peak mountain.[Enter nm to stop]")
        travel_answer=input("Where do you want to go?\n")
        if travel_answer.lower()=="star tree town":
            typewrite("You traveled to Star Tree town.")
            location="Star Tree town"
            star_tree_description()
            in_town=True
        if travel_answer.lower()=="farover hill":
            typewrite("You traveled to Farover hill.")
            location="Farover hill"
            farover_hill_description()
            in_town=False
        if travel_answer.lower()=="ice field":
            typewrite("You traveld to Ice Field.")
            location="Ice Field"
            ice_field_description()
            in_town=False
        if travel_answer.lower()=="northston town":
            typewrite("You traveled to Northston town.")
            location="Northston town"
            northston_description()
            in_town=True
        if travel_answer.lower()=="southston town":
            typewrite("You traveled to Southston town.")
            location="Southston town"
            southston_description()
            in_town=True
        if travel_answer.lower()=="halted river cave":
            typewrite("You traveld to Halted River Cave.")
            location="Halted River Cave"
            halted_river_cave_description()
            in_town=False
        if travel_answer.lower()=="weston town":
            typewrite("You traveled to Weston town.")
            location="Weston town"
            weston_description()
            in_town=True
        if travel_answer.lower()=="dark peak mountain":
            typewrite("You traveled to the dark & dangerous Dark Peak.")
            location="Dark Peak"
            dark_peak_mountain_description()
            in_town=False
        if travel_answer.lower()=="nm":
            typewrite("Ok, you stay where you are.")
        return location
    elif location=="Farover hill":
        typewrite("You can go to Easton town. Do you wish to go there?")
        travel_answer=input("[Yes or No]\n")
        if travel_answer.lower()=="yes":
            typewrite("You travel to Easton town.")
            location="Easton town"
            easton_description()
            in_town=True
            return location
        if travel_answer.lower()=="no":
            typewrite("Okay, you stay where you are.")
    elif location=="Weston town":
        typewrite("You can go to, Star Tree town, Easton town, Ice Field, Northston town, Southston town, Halted River Cave, or Dark Peak mountain.[Enter nm to stop]")
        travel_answer=input("Where do you want to go?\n")
        if travel_answer.lower()=="star tree town":
            typewrite("You traveled to Star Tree town.")
            location="Star Tree town"
            star_tree_description()
            in_town=True
        if travel_answer.lower()=="ice field":
            typewrite("You traveld to Ice Field.")
            location="Ice Field"
            ice_field_description()
            in_town=False
        if travel_answer.lower()=="northston town":
            typewrite("You traveled to Northston town.")
            location="Northston town"
            northston_description()
            in_town=True
        if travel_answer.lower()=="southston town":
            typewrite("You traveled to Southston town.")
            location="Southston town"
            southston_description()
            in_town=True
        if travel_answer.lower()=="halted river cave":
            typewrite("You traveld to Halted River Cave.")
            location="Halted River Cave"
            halted_river_cave_description()
            in_town=False
        if travel_answer.lower()=="dark peak mountain":
            typewrite("You traveled to the dark & dangerous Dark Peak.")
            location="Dark Peak"
            dark_peak_mountain_description()
            in_town=False
        if travel_answer.lower()=="nm":
            typewrite("Ok, you stay where you are.")
        return location
    elif location=="Ice Field":
        typewrite("You can go to, Star Tree town, Easton town, Weston town, Northston town, Southston town, Halted River Cave, or Dark Peak mountain.[Enter nm to stop]")
        travel_answer=input("Where do you want to go?\n")
        if travel_answer.lower()=="star tree town":
            typewrite("You traveled to Star Tree town.")
            location="Star Tree town"
            star_tree_description()
            in_town=True
        if travel_answer.lower()=="easton town":
            typewrite("You traveled to Easton town.")
            location="Easton town"
            easton_description()
            in_town=True
        if travel_answer.lower()=="weston town":
            typewrite("You traveled to Weston town.")
            location="Weston town"
            weston_description()
            in_town=True
        if travel_answer.lower()=="northston town":
            typewrite("You traveled to Northston town.")
            location="Northston town"
            northston_description()
            in_town=True
        if travel_answer.lower()=="southston town":
            typewrite("You traveled to Southston town.")
            location="Southston town"
            southston_description()
            in_town=True
        if travel_answer.lower()=="halted river cave":
            typewrite("You traveld to Halted River Cave.")
            location="Halted River Cave"
            halted_river_cave_description()
            in_town=False
        if travel_answer.lower()=="dark peak mountain":
            typewrite("You traveled to the dark & dangerous Dark Peak.")
            location="Dark Peak"
            dark_peak_mountain_description()
            in_town=False
        if travel_answer.lower()=="nm":
            typewrite("Ok, you stay where you are.")
        return location
    elif location=="Northston town":
        typewrite("You can go to, Star Tree town, Easton town, Weston town, Ice Field, Southston town, Halted River Cave, or Dark Peak mountain.[Enter nm to stop]")
        travel_answer=input("Where do you want to go?\n")
        if travel_answer.lower()=="star tree town":
            typewrite("You traveled to Star Tree town.")
            location="Star Tree town"
            star_tree_description()
            in_town=True
        if travel_answer.lower()=="easton town":
            typewrite("You traveled to Easton town.")
            location="Easton town"
            easton_description()
            in_town=True
        if travel_answer.lower()=="weston town":
            typewrite("You traveled to Weston town.")
            location="Weston town"
            weston_description()
            in_town=True
        if travel_answer.lower()=="ice field":
            typewrite("You traveld to Ice Field.")
            location="Ice Field"
            ice_field_description()
            in_town=False
        if travel_answer.lower()=="southston town":
            typewrite("You traveled to Southston town.")
            location="Southston town"
            southston_description()
            in_town=True
        if travel_answer.lower()=="halted river cave":
            typewrite("You traveld to Halted River Cave.")
            location="Halted River Cave"
            halted_river_cave_description()
            in_town=False
        if travel_answer.lower()=="dark peak mountain":
            typewrite("You traveled to the dark & dangerous Dark Peak.")
            location="Dark Peak"
            dark_peak_mountain_description()
            in_town=False
        if travel_answer.lower()=="nm":
            typewrite("Ok, you stay where you are.")
        return location
    elif location=="Southston town":
        typewrite("You can go to, Star Tree town, Easton town, Weston town, Ice Field, Northston town, Halted River Cave, or Dark Peak mountain.[Enter nm to stop]")
        travel_answer=input("Where do you want to go?\n")
        if travel_answer.lower()=="star tree town":
            typewrite("You traveled to Star Tree town.")
            location="Star Tree town"
            star_tree_description()
            in_town=True
        if travel_answer.lower()=="easton town":
            typewrite("You traveled to Easton town.")
            location="Easton town"
            easton_description()
            in_town=True
        if travel_answer.lower()=="weston town":
            typewrite("You traveled to Weston town.")
            location="Weston town"
            weston_description()
            in_town=True
        if travel_answer.lower()=="ice field":
            typewrite("You traveld to Ice Field.")
            location="Ice Field"
            ice_field_description()
            in_town=False
        if travel_answer.lower()=="northston town":
            typewrite("You traveled to Northston town.")
            location="Northston town"
            northston_description()
            in_town=True
        if travel_answer.lower()=="halted river cave":
            typewrite("You traveld to Halted River Cave.")
            location="Halted River Cave"
            halted_river_cave_description()
            in_town=False
        if travel_answer.lower()=="dark peak mountain":
            typewrite("You traveled to the dark & dangerous Dark Peak.")
            location="Dark Peak"
            dark_peak_mountain_description()
            in_town=False
        if travel_answer.lower()=="nm":
            typewrite("Ok, you stay where you are.")
        return location
    elif location=="Halted River Cave":
        typewrite("You can go to, Star Tree town, Easton town, Weston town, Ice Field, Northston town, Southston town, or Dark Peak mountain.[Enter nm to stop]")
        travel_answer=input("Where do you want to go?\n")
        if travel_answer.lower()=="star tree town":
            typewrite("You traveled to Star Tree town.")
            location="Star Tree town"
            star_tree_description()
            in_town=True
        if travel_answer.lower()=="easton town":
            typewrite("You traveled to Easton town.")
            location="Easton town"
            easton_description()
            in_town=True
        if travel_answer.lower()=="weston town":
            typewrite("You traveled to Weston town.")
            location="Weston town"
            weston_description()
            in_town=True
        if travel_answer.lower()=="ice field":
            typewrite("You traveld to Ice Field.")
            location="Ice Field"
            ice_field_description
            in_town=False
        if travel_answer.lower()=="northston town":
            typewrite("You traveled to Northston town.")
            location="Northston town"
            northston_description()
            in_town=True
        if travel_answer.lower()=="southston town":
            typewrite("You traveld to Southston town.")
            location="Southston town"
            southston_description
            in_town=True
        if travel_answer.lower()=="dark peak mountain":
            typewrite("You traveled to the dark & dangerous Dark Peak.")
            location="Dark Peak"
            dark_peak_mountain_description()
            in_town=False
        if travel_answer.lower()=="nm":
            typewrite("Ok, you stay where you are.")
        return location
    elif location=="Dark Peak":
        typewrite("You can go to, Star Tree town, Easton town, Weston town, Ice Field, Northston town, Southston town, or Dark Peak mountain.[Enter nm to stop]")
        travel_answer=input("Where do you want to go?\n")
        if travel_answer.lower()=="star tree town":
            typewrite("You traveled to Star Tree town.")
            location="Star Tree town"
            star_tree_description()
            in_town=True
        if travel_answer.lower()=="easton town":
            typewrite("You traveled to Easton town.")
            location="Easton town"
            easton_description()
            in_town=True
        if travel_answer.lower()=="weston town":
            typewrite("You traveled to Weston town.")
            location="Weston town"
            weston_description()
            in_town=True
        if travel_answer.lower()=="ice field":
            typewrite("You traveld to Ice Field.")
            location="Ice Field"
            ice_field_description()
            in_town=False
        if travel_answer.lower()=="northston town":
            typewrite("You traveled to Northston town.")
            location="Northston town"
            northston_description()
            in_town=True
        if travel_answer.lower()=="southston town":
            typewrite("You traveld to Southston town.")
            location="Southston town"
            southston_description()
            in_town=True
        if travel_answer.lower()=="halted river cave":
            typewrite("You traveled to Halted River Cave.")
            location="Halted River Cave"
            halted_river_cave_description()
            in_town=False
        if travel_answer.lower()=="nm":
            typewrite("Ok, you stay where you are.")
        return location
    elif travel_answer.lower() not in locations:
        typewrite("You can't go there! You either can't reach it from here or it doesn't exist.")
        typewrite("[Or there's a typo in your spelling.]")
def search():
    global location, health, inventory, items
    typewrite("You search the area.")
    if location=="Starting Field":
        item_chance=random.randint(1,3)
        if item_chance==2:
            if starting_field_items != []:
                item=random.choice(starting_field_items)
                inventory.append(item)
                typewrite(f"You got a {item}.")
                if item in starting_field_items:
                    starting_field_items.remove(item)
                if item in star_tree_town_items:
                    star_tree_town_items.remove(item)
                if item in easton_town_items:
                    easton_town_items.remove(item)
                if item in farover_hill_items:
                    farover_hill_items.remove(item)
                if item in halted_river_cave_items:
                    halted_river_cave_items.remove(item)
                if item in ice_field_items:
                    ice_field_items.remove(item)
                if item in dark_peak_items:
                   dark_peak_items.remove(item)
                if item in northston_town_items:
                    northston_town_items.remove(item)
                if item in southston_town_items:
                    southston_town_items.remove(item)
                if item in weston_town_items:
                    weston_town_items.remove(item)
            else:
                typewrite("There is nothing left here.")
        enemy_chance=random.randint(1,3)
        if enemy_chance==2:
            enemy=random.choice(starting_field_monsters)
            if enemy=="Big Rat":
                big_rat()
            elif enemy=="Wolf":
                wolf()
            elif enemy=="Boar":
                boar()
        health_potion_chance=random.randint(1,3)
        if health_potion_chance==2:
            health_potion_get()
        if item_chance!=2 and enemy_chance!=2 and health_potion_chance!=2:
            typewrite("You find nothing")
    elif location=="Star Tree town":
        item_chance=random.randint(1,3)
        if item_chance==2:
            if star_tree_town_items != []:
                item=random.choice(star_tree_town_items)
                inventory.append(item)
                typewrite(f"You got a {item}.")
                if item in starting_field_items:
                    starting_field_items.remove(item)
                if item in star_tree_town_items:
                    star_tree_town_items.remove(item)
                if item in easton_town_items:
                    easton_town_items.remove(item)
                if item in farover_hill_items:
                    farover_hill_items.remove(item)
                if item in halted_river_cave_items:
                    halted_river_cave_items.remove(item)
                if item in ice_field_items:
                    ice_field_items.remove(item)
                if item in dark_peak_items:
                   dark_peak_items.remove(item)
                if item in northston_town_items:
                    northston_town_items.remove(item)
                if item in southston_town_items:
                    southston_town_items.remove(item)
                if item in weston_town_items:
                    weston_town_items.remove(item)
            else:
                typewrite("There is nothing left here.")
        enemy_chance=random.randint(1,3)
        if enemy_chance==2:
            enemy=random.choice(star_tree_town_monsters)
            if enemy=="Big Rat":
                big_rat()
            if enemy=="Rabid Dog":
                rabid_dog()
        health_potion_chance=random.randint(1,3)
        if health_potion_chance==2:
            health_potion_get()
        if item_chance!=2 and enemy_chance!=2 and health_potion_chance!=2:
            typewrite("You find nothing")
    elif location=="Easton town":
        item_chance=random.randint(1,3)
        if item_chance==2:
            if easton_town_items != []:
                item=random.choice(easton_town_items)
                inventory.append(item)
                typewrite(f"You got a {item}.")
                if item in starting_field_items:
                    starting_field_items.remove(item)
                if item in star_tree_town_items:
                    star_tree_town_items.remove(item)
                if item in easton_town_items:
                    easton_town_items.remove(item)
                if item in farover_hill_items:
                    farover_hill_items.remove(item)
                if item in halted_river_cave_items:
                    halted_river_cave_items.remove(item)
                if item in ice_field_items:
                    ice_field_items.remove(item)
                if item in dark_peak_items:
                   dark_peak_items.remove(item)
                if item in northston_town_items:
                    northston_town_items.remove(item)
                if item in southston_town_items:
                    southston_town_items.remove(item)
                if item in weston_town_items:
                    weston_town_items.remove(item)
            else:
                typewrite("There is nothing left here.")
        enemy_chance=random.randint(1,3)
        if enemy_chance==2:
            enemy=random.choice(easton_town_monsters)
            if enemy=="Big Rat":
                big_rat()
            if enemy=="Rabid Dog":
                rabid_dog()
        health_potion_chance=random.randint(1,3)
        if health_potion_chance==2:
            health_potion_get()
        if item_chance!=2 and enemy_chance!=2 and health_potion_chance!=2:
            typewrite("You find nothing")
    elif location=="Northston town":
        item_chance=random.randint(1,3)
        if item_chance==2:
            if northston_town_items != []:
                item=random.choice(northston_town_items)
                inventory.append(item)
                typewrite(f"You got a {item}.")
                if item in starting_field_items:
                    starting_field_items.remove(item)
                if item in star_tree_town_items:
                    star_tree_town_items.remove(item)
                if item in easton_town_items:
                    easton_town_items.remove(item)
                if item in farover_hill_items:
                    farover_hill_items.remove(item)
                if item in halted_river_cave_items:
                    halted_river_cave_items.remove(item)
                if item in ice_field_items:
                    ice_field_items.remove(item)
                if item in dark_peak_items:
                   dark_peak_items.remove(item)
                if item in northston_town_items:
                    northston_town_items.remove(item)
                if item in southston_town_items:
                    southston_town_items.remove(item)
                if item in weston_town_items:
                    weston_town_items.remove(item)
            else:
                typewrite("There is nothing left here.")
        enemy_chance=random.randint(1,3)
        if enemy_chance==2:
            enemy=random.choice(northston_town_monsters)
            if enemy=="Big Rat":
                big_rat()
            if enemy=="Rabid Dog":
                rabid_dog()
        health_potion_chance=random.randint(1,3)
        if health_potion_chance==2:
            health_potion_get()
        if item_chance!=2 and enemy_chance!=2 and health_potion_chance!=2:
            typewrite("You find nothing")
    elif location=="Southston town":
        item_chance=random.randint(1,3)
        if item_chance==2:
            if southston_town_items != []:
                item=random.choice(southston_town_items)
                inventory.append(item)
                typewrite(f"You got a {item}.")
                if item in starting_field_items:
                    starting_field_items.remove(item)
                if item in star_tree_town_items:
                    star_tree_town_items.remove(item)
                if item in easton_town_items:
                    easton_town_items.remove(item)
                if item in farover_hill_items:
                    farover_hill_items.remove(item)
                if item in halted_river_cave_items:
                    halted_river_cave_items.remove(item)
                if item in ice_field_items:
                    ice_field_items.remove(item)
                if item in dark_peak_items:
                   dark_peak_items.remove(item)
                if item in northston_town_items:
                    northston_town_items.remove(item)
                if item in southston_town_items:
                    southston_town_items.remove(item)
                if item in weston_town_items:
                    weston_town_items.remove(item)
            else:
                typewrite("There is nothing left here.")
        enemy_chance=random.randint(1,3)
        if enemy_chance==2:
            enemy=random.choice(southston_town_monsters)
            if enemy=="Big Rat":
                big_rat()
            if enemy=="Rabid Dog":
                rabid_dog()
        health_potion_chance=random.randint(1,3)
        if health_potion_chance==2:
            health_potion_get()
        if item_chance!=2 and enemy_chance!=2 and health_potion_chance!=2:
            typewrite("You find nothing")
    elif location=="Ice Field":
        item_chance=random.randint(1,3)
        if item_chance==2:
            if ice_field_items != []:
                item=random.choice(ice_field_items)
                inventory.append(item)
                typewrite(f"You got a {item}.")
                if item in starting_field_items:
                    starting_field_items.remove(item)
                if item in star_tree_town_items:
                    star_tree_town_items.remove(item)
                if item in easton_town_items:
                    easton_town_items.remove(item)
                if item in farover_hill_items:
                    farover_hill_items.remove(item)
                if item in halted_river_cave_items:
                    halted_river_cave_items.remove(item)
                if item in ice_field_items:
                    ice_field_items.remove(item)
                if item in dark_peak_items:
                   dark_peak_items.remove(item)
                if item in northston_town_items:
                    northston_town_items.remove(item)
                if item in southston_town_items:
                    southston_town_items.remove(item)
                if item in weston_town_items:
                    weston_town_items.remove(item)
            else:
                typewrite("There is nothing left here.")
        enemy_chance=random.randint(1,3)
        if enemy_chance==2:
            enemy=random.choice(ice_field_monsters)
            if enemy=="Big Rat":
                big_rat()
            elif enemy=="Wolf":
                wolf()
            elif enemy=="Boar":
                boar()
        health_potion_chance=random.randint(1,3)
        if health_potion_chance==2:
            health_potion_get()
        if item_chance!=2 and enemy_chance!=2 and health_potion_chance!=2:
            typewrite("You find nothing")
    elif location=="Farover hill":
        item_chance=random.randint(1,3)
        if item_chance==2:
            if farover_hill_items != []:
                item=random.choice(farover_hill_items)
                inventory.append(item)
                typewrite(f"You got a {item}.")
                if item in starting_field_items:
                    starting_field_items.remove(item)
                if item in star_tree_town_items:
                    star_tree_town_items.remove(item)
                if item in easton_town_items:
                    easton_town_items.remove(item)
                if item in farover_hill_items:
                    farover_hill_items.remove(item)
                if item in halted_river_cave_items:
                    halted_river_cave_items.remove(item)
                if item in ice_field_items:
                    ice_field_items.remove(item)
                if item in dark_peak_items:
                   dark_peak_items.remove(item)
                if item in northston_town_items:
                    northston_town_items.remove(item)
                if item in southston_town_items:
                    southston_town_items.remove(item)
                if item in weston_town_items:
                    weston_town_items.remove(item)
            else:
                typewrite("There is nothing left here.")
        enemy_chance=random.randint(1,3)
        if enemy_chance==2:
            enemy=random.choice(farover_hill_monsters)
            if enemy=="Big Rat":
                big_rat()
            elif enemy=="Wolf":
                wolf()
            elif enemy=="Bear":
                bear()
            elif enemy=="Wild Dog":
                wild_dog()
        health_potion_chance=random.randint(1,3)    
        if health_potion_chance==2:
            health_potion_get()
        if item_chance!=2 and enemy_chance!=2 and health_potion_chance!=2:
            typewrite("You find nothing")
    elif location=="Halted River Cave":
        item_chance=random.randint(1,3)
        if item_chance==2:
            if halted_river_cave_items != []:
                item=random.choice(halted_river_cave_items)
                inventory.append(item)
                typewrite(f"You got a {item}.")
                if item in starting_field_items:
                    starting_field_items.remove(item)
                if item in star_tree_town_items:
                    star_tree_town_items.remove(item)
                if item in easton_town_items:
                    easton_town_items.remove(item)
                if item in farover_hill_items:
                    farover_hill_items.remove(item)
                if item in halted_river_cave_items:
                    halted_river_cave_items.remove(item)
                if item in ice_field_items:
                    ice_field_items.remove(item)
                if item in dark_peak_items:
                   dark_peak_items.remove(item)
                if item in northston_town_items:
                    northston_town_items.remove(item)
                if item in southston_town_items:
                    southston_town_items.remove(item)
                if item in weston_town_items:
                    weston_town_items.remove(item)
            else:
                typewrite("There is nothing left here.")
        enemy_chance=random.randint(1,3)
        if enemy_chance==2:
            enemy=random.choice(halted_river_cave_monsters)
            if enemy=="Big Rat":
                big_rat()
            elif enemy=="Wolf":
                wolf()
            elif enemy=="Bear":
                bear()
            elif enemy=="Wild Dog":
                wild_dog()
        health_potion_chance=random.randint(1,3)
        if health_potion_chance==2:
            health_potion_get()
        if item_chance!=2 and enemy_chance!=2 and health_potion_chance!=2:
            typewrite("You find nothing")
    elif location=="Dark Peak":
        item_chance=random.randint(1,4)
        if item_chance==2:
            if dark_peak_items != []:
                item=random.choice(dark_peak_items)
                inventory.append(item)
                if item !="the dream cleaver":
                    typewrite(f"You found a skeleton holding a {item}. Creepy. Let's go.")
                elif item=="the dream cleaver":
                    typewrite("You found the legendary Dream Cleaver! Good for you!")
                if item in starting_field_items:
                    starting_field_items.remove(item)
                if item in star_tree_town_items:
                    star_tree_town_items.remove(item)
                if item in easton_town_items:
                    easton_town_items.remove(item)
                if item in farover_hill_items:
                    farover_hill_items.remove(item)
                if item in halted_river_cave_items:
                    halted_river_cave_items.remove(item)
                if item in ice_field_items:
                    ice_field_items.remove(item)
                if item in dark_peak_items:
                   dark_peak_items.remove(item)
                if item in northston_town_items:
                    northston_town_items.remove(item)
                if item in southston_town_items:
                    southston_town_items.remove(item)
                if item in weston_town_items:
                    weston_town_items.remove(item)
            else:
                typewrite("There is nothing left here.")
        enemy_chance=random.randint(1,2)
        if enemy_chance==2:
            enemy=random.choice(dark_peak_monsters)
            if enemy=="Bear":
                bear()
            if enemy=="Wild Dog":
                wild_dog()
            if enemy=="Young Rock Drake":
                young_rock_drake()
        health_potion_chance=random.randint(1,3)
        if health_potion_chance==2:
            health_potion_get()
        if item_chance!=2 and enemy_chance!=2 and health_potion_chance!=2:
            typewrite("You find nothing")
    elif location=="Weston town":
        item_chance=random.randint(1,3)
        if item_chance==2:
            if weston_town_items != []:
                item=random.choice(weston_town_items)
                inventory.append(item)
                typewrite(f"You got a {item}.")
                if item in starting_field_items:
                    starting_field_items.remove(item)
                if item in star_tree_town_items:
                    star_tree_town_items.remove(item)
                if item in easton_town_items:
                    easton_town_items.remove(item)
                if item in farover_hill_items:
                    farover_hill_items.remove(item)
                if item in halted_river_cave_items:
                    halted_river_cave_items.remove(item)
                if item in ice_field_items:
                    ice_field_items.remove(item)
                if item in dark_peak_items:
                   dark_peak_items.remove(item)
                if item in northston_town_items:
                    northston_town_items.remove(item)
                if item in southston_town_items:
                    southston_town_items.remove(item)
                if item in weston_town_items:
                    weston_town_items.remove(item)
            else:
                typewrite("There is nothing left here.")
        enemy_chance=random.randint(1,3)
        if enemy_chance==2:
            enemy=random.choice(weston_town_monsters)
            if enemy=="Big Rat":
                big_rat()
            if enemy=="Rabid Dog":
                rabid_dog()
        health_potion_chance=random.randint(1,3)
        if health_potion_chance==2:
            health_potion_get()
        if item_chance!=2 and enemy_chance!=2 and health_potion_chance!=2:
            typewrite("You find nothing")
def death():
    global player_name_first, world_name
    typewrite("You're dying, you can feel it. As you're laying there, you notice the world fading. You think it's because you're dying, but then you hear weird noises. It sounds like, a heart monitor? But something's wrong, it's slowing. You can feel your heart beat slowing too.",0.04)
    typewrite("'Oh,' you say aloud. You've just remembered something. This place isn't real. That's why it's fading. The brain that created it can't hold onto the world any longer. You've been in a coma this whole time. But you were placed in this coma magically.",0.04)
    typewrite(f"If you die in this dream, you die in real life. Death is settling in. Your pain starts to subside, but you know it's because you're losing the feeling in your body. Your heart slows more. The noise grows louder & louder until, 'Goodbye {player_name_first}, I'll miss you, so, so much.' Your brother is devastated. You realize just before you die, his voice was the one that guided you during this adventure.",0.04)
    typewrite("You smile, your last smile. Even when he didn't know it, your brother still helped you when you needed his help most.",0.04)
    typewrite("..........",0.019)
    typewrite(f"You hear the monitor flatline as you lose all feeling. Goodbye {world_name}. Goodbye Earth. Goobye Life",0.04)
    typewrite("..........",0.44)
    typewrite("Hello Death.",0.44)
    typewrite("[Enter anything to end game. Thanks for playing!]")
    typewrite("************************************************************",.94)
    quit()
def help():
    typewrite("Here is a list of things you can do, & where you can do them.")
    typewrite("1. Travel [Allows you to travel between locations.]",-.06)
    typewrite("2. Search [You search the area you are located in. You can find items & monsters. Different locations have different items & monsters.]",-.06)
    typewrite("3. Get Map [You get a map. Can only be used in towns.]",-.06)
    typewrite("4. Map [Opens the map]",-.06)
    typewrite("5. Talk / Greet NPC [You talk to an Npc for information. Can only be used in a town.]",-.06)
    typewrite("6. Boss Fight [Starts the boss fight if at dark peak mountain.]",-.06)
    typewrite("7. Rest / Sleep [You go to sleep. Restores your health to 100. Fun things happen.]",-.06)
    typewrite("8. Quit [Quits the game. But be careful! You can't save.]",-.06)
    typewrite("9. Check Stats / Status Check [Prints the # of days played, # of enemies killed, & player & world names]",-.06)
    typewrite("10. Check Inventory [Shows you the stuff in your inventory.]",-.06)
    typewrite("11. Clear Console [Clears the screen/console of all text]",-.06)
    typewrite("12. Mini Game [Starts a mini game. There are 5 different mini games, 1 for each town.]",-.06)
    typewrite("13. Save [Saves the game so you can pick up later.]",-.06)
def list_check():
    print(starting_field_items)
    print(star_tree_town_items)
    print(easton_town_items)
    print(weston_town_items)
    print(northston_town_items)
    print(southston_town_items)
    print(farover_hill_items)
    print(halted_river_cave_items)
    print(ice_field_items)
    print(dark_peak_items)
attack_options=["fight","attack"]
flee_options=["flee","run","run away",""]
def fight_or_flight():
    global flee, attack
    flee=False
    attack=False
    fight="[Error]"
    while flee==False and attack==False:
        typewrite("What do you want to do! You can attack or flee")
        fight=input()
        if fight.lower() in attack_options:
            typewrite("You decide to fight!")
            attack=True
        elif fight.lower() in flee_options:
            flee=True
        else:
            typewrite("[Error. Decision not valid, please enter attack or flee]")
    return flee, attack, inventory
def fighting(enemy,enemy_hp,enemy_damage):
    global flee, attack, health, enemies_killed
    typewrite(f"'Ah! A {enemy}!'")
    fight_or_flight()
    enemy_health=enemy_hp
    if attack==True:
        while enemy_health>0:
            typewrite(f"What weapon do you use? Here's what you got:\nhands")
            if "sword"in inventory:
                typewrite("sword")
            if "dagger"in inventory:
                typewrite("dagger")
            if "war axe"in inventory:
                typewrite("war axe")
            if "mace"in inventory:
                typewrite("mace")
            if "the dream cleaver"in inventory:
                typewrite("the dream cleaver")
            if "health potion" in inventory:
                typewrite("health potion")
            print()
            weapon=input()
            if weapon.lower() in inventory:
                if weapon.lower()=="hands":
                    typewrite(f"You attack with your bare hands! The {enemy} takes 1 hp of damage.")
                    enemy_health=enemy_health-1
                    if enemy_health>0:
                        enemy_attack(enemy_damage,enemy)
                if weapon.lower()=="sword":
                    typewrite(f"You attack with your sword! The {enemy} takes 3 hp of damage.")
                    enemy_health=enemy_health-3
                    if enemy_health>0:
                        enemy_attack(enemy_damage,enemy)
                if weapon.lower()=="dagger":
                    typewrite(f"You attack with your dagger! The {enemy} takes 2 hp of damage.")
                    enemy_health=enemy_health-2
                    if enemy_health>0:
                        enemy_attack(enemy_damage,enemy)
                if weapon.lower()=="war axe":
                    typewrite(f"You attack with your war axe! The {enemy} takes 4 hp of damage.")
                    enemy_health=enemy_health-4
                    if enemy_health>0:
                        enemy_attack(enemy_damage,enemy)
                if weapon.lower()=="mace":
                    typewrite(f"You attack with your mace! The {enemy} takes 5 hp of damage.")
                    enemy_health=enemy_health-5
                    if enemy_health>0:
                        enemy_attack(enemy_damage,enemy)
                if weapon.lower()=="the dream cleaver":
                    typewrite(f"You attack with the dream cleaver! The {enemy} takes 7 hp of damage")
                    enemy_health=enemy_health-7
                    if enemy_health>0:
                        enemy_attack(enemy_damage,enemy)
                if weapon.lower()=="health potion":
                    health_potion()
                    if enemy_health>0:
                        enemy_attack(enemy_damage,enemy)
                typewrite(f"You have {health} hp points left!")
            elif weapon.lower() not in inventory:
                typewrite("You don't have one of those![Or a typo] Try something else.")
            if health<=0:
                typewrite("You have been defeated. Goodbye.",0.14)
                death()
            if enemy_health>0:
                typewrite(f"The {enemy} has {enemy_health} hp points left!")
        typewrite(f"You have defeated the {enemy}! Good job!")
        enemies_killed=enemies_killed+1
        return enemies_killed
    elif flee==True:
        typewrite(f"You got away! But you got hit in the process! You took {enemy_damage} hp damage")
        health=health-enemy_damage
    else:
        typewrite("[Error]")
def enemy_attack(enemy_damage,enemy):
    global health
    hit_chance=random.randint(1,2)
    if hit_chance==2:
        typewrite(f"You got hit! You take {enemy_damage} hp of damage.")
        health=health-enemy_damage
        if health<=0:
            typewrite("You have been defeated. Goodbye.",0.14)
            death()
    elif hit_chance==1:
        typewrite(f"The {enemy} missed! You are safe!")
def big_rat():
    fighting("Big Rat",5,2)
def wolf():
    fighting("Wolf",7,4)
def boar():
    fighting("Boar",8,4)
def rabid_dog():
    fighting("Rabid Dog",6,3)
def wild_dog():
    fighting("Wild Dog",7,4)
def bear():
    fighting("Bear",10,5)
def young_rock_drake():
    fighting("Young Rock Drake",12,6)
def sleep():
    global day, health
    typewrite("You decide to go to sleep. Sweet dreams!",0.015)
    health=100
    if day==1:
        cutscene_1()
    if day==3:
        cutscene_2()
    if day==6:
        cutscene_3()
    if day==8:
        cutscene_4()
    if day not in cutscene_days:
        if day>8:
            cutscene_review_decision="[Error]"
            while cutscene_review_decision.lower()!="no":
                typewrite("Would you like to review a cutscene? [Yes or No]")
                cutscene_review_decision=input()
                if cutscene_review_decision.lower()=="yes":
                    typewrite("What cutscene would you like to review? Cutscene 1, 2, 3, or 4?")
                    cutscene_number=int(input())
                    if cutscene_number==1:
                        typewrite("Okay! Here you go!")
                        cutscene_1()
                        cutscene_review_decision=="no"
                    if cutscene_number==2:
                        typewrite("Okay! Here you go!")
                        cutscene_2()
                        cutscene_review_decision=="no"
                    if cutscene_number==3:
                        typewrite("Okay! Here you go!")
                        cutscene_3()
                        cutscene_review_decision=="no"
                    if cutscene_number==4:
                        typewrite("Okay! Here you go!")
                        cutscene_4()
                        cutscene_review_decision=="no"
            if cutscene_review_decision.lower()=="no":
                typewrite("Okay.")
                no_dream()
        if day<8:
            no_dream()
    day=day+1
    typewrite(f"It has been {day} days since you awoke here.")
    typewrite("You feel refreshed. Your health has been replenished.")
    return day,health
def no_dream():
    typewrite("You have no dreams tonight. Peace.")
def cutscene_1():
    global player_name_first
    typewrite(f"'{player_name_first}!, please wake up! Wake up! Please.")
    typewrite("You wake up imediatly.")
    typewrite("'What was that?'")
    typewrite("...",0.14)
    typewrite("'Weird'")
def cutscene_2():
    typewrite(f"'I miss you {player_name_first}. Please wake up soon.'")
    typewrite("...")
    typewrite("'Stupid Witch.'")
    typewrite("You wake up in a cold sweat.")
    typewrite("'These are some weird dreams. I hope they stop soon.'")
def cutscene_3():
    typewrite(f"'I miss you so much {player_name_first}. I hate what that witch has done to you.")
    typewrite(".....")
    typewrite("'I have to find a way to fix this.'")
    typewrite("...")
    typewrite("'I'll talk to you later, okay?'")
    typewrite("'Gah!'")
    typewrite("These dreams keep getting werider & weirder. Why? Do they mean anything?")
    typewrite("I'll think more about this later, I have other things to do.")
def cutscene_4():
    typewrite(f"'Hey {player_name_first}. I'm so, so sorry. I couldn't find a way to wake you up.")
    typewrite("The witch said that you had to find a way to wake up yourself. That you had to fight something big. Whatever that means.")
    typewrite("But I won't give up. I will find a way to break that witch's curse. Just you wait.'")
    typewrite("You awake calmly, for the first time after you've had one of these dreams.")
    typewrite("'Who is this person? What were they talking about?'")
    typewrite("'What was this big thing I have to fight? Do they mean the monster of Dark Peak?'")
    typewrite("'If they do, does that means defeating the monster will help me figure out the rest of the questions?'")
    typewrite("'Well, there's only one way to find out. To Dark Peak!'")
def boss():
    global final_boss
    final_boss=random.choice(bosses)
    return final_boss
def the_end():
    global final_boss,player_name_first
    typewrite(f"You have defeated the monster of Dark Peak, {final_boss}.")
    typewrite(f"'Well done. You have defeated {final_boss}.'")
    typewrite("'And now,")
    typewrite("'It's time for you to",0.04)
    typewrite("Wake up.'",0.69)
    typewrite("'Wake, & live.'")
    typewrite("'And remember, don't trust shady people.'")
    typewrite("'Live your life to it's fullest.'")
    typewrite("'I will miss you. Now wake.'")
    typewrite("..........",0.44)
    typewrite("You awaken to see, White? There's so much white. you're in a hospital, you can tell.")
    typewrite("'Hello?' You say, hoping someone will hear. 'Where am I?'")
    typewrite(f"Someone comes in the room. '{player_name_first}! You're finaly awake! Oh I've missed you so much! Your brother gives you a big hug.")
    typewrite("You smile. You're awake. You're free. You're safe.")
    typewrite("You are home.",0.69)
    typewrite("The End")
    typewrite("Thanks for playing Dragons & Daydreaming! Hope you enjoed! Have a great day!")
    typewrite("[If you encoutered any issues, please contact Ethan Dean so he can fix them. Thank You!]")
    typewrite("************************************************************",.94)
    quit()
def boss_attack(boss_health,boss_damage):
    global health
    if boss_health>0:
        typewrite(f"{final_boss} attacks! Dark energy swirls around the room,")
        hit_chance=random.randint(1,2)
        if hit_chance==2:
            typewrite("you got hit!")
            typewrite(f"You take {boss_damage} hp of damage!")
            typewrite("Come on, keep going! You can do this!")
            health=health-boss_damage
            return health
        elif hit_chance==1:
               typewrite("They missed! Hurry! Retaliate!")
def boss_fight(boss_health,boss_damage):
    global location, inventory, player_name_first, player_name_last, final_boss, health
    if location=="Dark Peak":
        typewrite("You have gone searching for the monster of Dark Peak. Good Luck.")
        typewrite("[???]'Hello there little pest. You've been upsetting the fear I've placed over this land, and I don't like that.'")
        typewrite("[???]'You have 2 options. Leave this land, never to return, or Die.'")
        typewrite(f"[{player_name_first} {player_name_last}]'What makes you think I'll be choosing either of them? And who the heck are you?'")
        typewrite(f"[{final_boss}]'I am {final_boss}. And you will choose, or I will choose for you. And I don't think you'll like what I choose.'")
        typewrite(f"[{player_name_first} {player_name_last}]'I choose to fight.'")
        typewrite(f"[{final_boss}]'So you have chosen, death.")
        typewrite(f"[{final_boss}]'Now come and face the manefestion of your fears.")
        typewrite("Watch out!")
        while boss_health>0:
            if health<=0:
                typewrite(f"[{final_boss}]'Ha Ha Ha! You fool! Challenging me was the worst mistake you could have made!'")
                typewrite(f"You see {final_boss} start to fade.")
                typewrite(f"[{final_boss}]'What is happening to me!?'")
                typewrite(f"{final_boss} is gone faded out of existance. What happened? You don't know. All you know is that,")
                death()
            typewrite("What do you use to fight?")
            typewrite(f"Here's what you have:\nhands")
            if "sword"in inventory:
                typewrite("sword")
            if "dagger"in inventory:
                typewrite("dagger")
            if "war axe"in inventory:
                typewrite("war axe")
            if "mace"in inventory:
                typewrite("mace")
            if "the dream cleaver"in inventory:
                typewrite("the dream cleaver")
            if "health potion" in inventory:
                typewrite("health potion")
            print()
            weapon_choice=input()
            if weapon_choice.lower() in inventory:
                if weapon_choice.lower()=="hands":
                    typewrite(f"You attack with your bare hands! {final_boss} takes 1 hp of damage.")
                    boss_health=boss_health-1
                    if boss_health>0:
                        boss_attack(boss_health,boss_damage)
                if weapon_choice.lower()=="sword":
                    typewrite(f"You attack with your sword! {final_boss} takes 3 hp of damage.")
                    boss_health=boss_health-3
                    if boss_health>0:
                        boss_attack(boss_health,boss_damage)
                if weapon_choice.lower()=="dagger":
                    typewrite(f"You attack with your dagger! {final_boss} takes 2 hp of damage.")
                    boss_health=boss_health-2
                    if boss_health>0:
                        boss_attack(boss_health,boss_damage)
                if weapon_choice.lower()=="war axe":
                    typewrite(f"You attack with your war axe! {final_boss} takes 4 hp of damage.")
                    boss_health=boss_health-4
                    if boss_health>0:
                        boss_attack(boss_health,boss_damage)
                if weapon_choice.lower()=="mace":
                    typewrite(f"You attack with your mace! {final_boss} takes 5 hp of damage.")
                    boss_health=boss_health-5
                    if boss_health>0:
                        boss_attack(boss_health,boss_damage)
                if weapon_choice.lower()=="the dream cleaver":
                    typewrite(f"You attack with the dream cleaver! {final_boss} takes 7 hp of damage")
                    boss_health=boss_health-7
                    if boss_health>0:
                        boss_attack(boss_health,boss_damage)
                if weapon_choice.lower()=="health potion":
                    health_potion()
                    if boss_health>0:
                        boss_attack(boss_health,boss_damage)
                typewrite(f"You have {health} hp points left!")
                if boss_health>0:
                    typewrite(f"{final_boss} has {boss_health} hp points left!")
            if boss_health<=0:
                typewrite(f"[{final_boss}]'Noooooooooo!' You can't defeat me!'")
                typewrite(f"{final_boss} starts to fade.")
                typewrite(f"[{final_boss}]'I am your fear! I can not be killed! You can not get rid of me!")
                typewrite(f"{final_boss} fades more.")
                typewrite(f"[{player_name_first} {player_name_last}]'I can get rid of you. I have. I faced my fear & overcame it. You hold no power over me anymore.'")
                typewrite(f"[{player_name_first} {player_name_last}]'You fade with my fears. & I fear no more.'")
                typewrite(f"{final_boss} is gone. You are all alone.")
                typewrite("....................",0.69)
                typewrite(f"Hello {player_name_first}. Well done.")
                the_end()
    if location!="Dark Peak":
        typewrite("You are not in Dark Peak. You can not search for it's resident monster here.")
        typewrite("Go do something else.")
def profile():
    global day, enemies_killed, world_name, player_name_first, player_name_last
    typewrite("Here's your character profile:")
    typewrite(f"Day: {day}")
    typewrite(f"Enemies killed: {enemies_killed}")
    typewrite(f"First Name: {player_name_first}")
    typewrite(f"Last Name: {player_name_last}")
    typewrite(f"World Name: {world_name}")
def health_potion():
    global health, health_potions
    typewrite("You used a health potion! Your hp points have been restored!")
    typewrite("Keep up the fight!")
    health=100
    inventory.remove("health potion")
    health_potions=health_potions-1
    return health, health_potions
def health_potion_get():
    global inventory, health_potions
    typewrite("You got a health potion! You can only use it while fighting.")
    inventory.append("health potion")
    health_potions=health_potions+1
    return health_potions
def console_clear():
    global clear
    typewrite("Clearing console")
    typewrite("*************************",.94)
    clear()
    typewrite("Console Cleared.")
def play_mini_games():
    global location, in_town, has_met_ethan, player_name_first, player_name_last, health
    if in_town==True:
        if has_met_ethan==True:
            typewrite(f"[Ethan Dean]'Hello {player_name_first}! Would you like to play a game?")
        typewrite("Do you want to play a mini game? [Yes or No]")
        mini_decision=input()
        if mini_decision.lower()=="yes":
            if location=="Star Tree town":
                mini_game_1()
                health=100
            elif location=="Easton town":
                mini_game_2()
                health=100
            elif location=="Weston town":
                mini_game_3()
                health=100
            elif location=="Northston town":
                mini_game_4()
                health=100
            elif location=="Southston town":
                mini_game_5()
                health=100
            return health
        if mini_decision.lower()=="no":
            typewrite("'Okay! Come again soon!'")
    elif in_town==False:
        typewrite("There's no one around to play a game with. Perhaps someone in a nearby town will want to play?")
def mini_game_1():
    typewrite("[Ethan Dean]'Thanks! Lets play Rock Paper Scisors!")
    player_move=0
    while player_move != 4:
        typewrite("Enter the number of the move you want to play")
        player_move=int(input("Choose:\n1. Rock\n2. Paper\n3. Scissors\n4. Quit\n"))
        typewrite(f"You have chosen {player_move}")
        if player_move == 4:
            typewrite("Goodbye!")
        if player_move !=4:
            computer_move=random.randint(1,3)
            typewrite(f"[Ethan Dean]'I have chosen {computer_move}.'")
            if player_move == computer_move:
                typewrite("[Ethan Dean]'It's a tie!'")
            if player_move == 1 and computer_move == 2:
                typewrite("[Ethan Dean]'I win! Again?'")
            if player_move == 1 and computer_move == 3:
                typewrite("[Ethan Dean]'You win! Again?'")
            if player_move == 2 and computer_move == 3:
                typewrite("[Ethan Dean]'I win! Again?'")
            if player_move == 2 and computer_move == 1:
                typewrite("[Ethan Dean]'You win! Again?'")
            if player_move == 3 and computer_move == 1:
                typewrite("[Ethan Dean]'I win! Again?'")
            if player_move == 3 and computer_move == 2:
                typewrite("[Ethan Dean]'You win! Again?'")
def mini_game_2():
    global location
    typewrite("[Ethan Dean]'Thanks! Lets play a dice game!")
    dice=0
    while dice != 4:
        dice=int(input("How many dice would you like to roll? 1, 2, or 3? enter 4 to stop playing. "))
        if dice==4:
            typewrite("[Ethan Dean]'Goodbye!'")
        if dice!=4:
            typewrite(f"You have chosen to roll {dice} dice")
            if dice == 1:
                player_roll1=random.randint(1,6)
                typewrite(f"[Ethan Dean]'You rolled a {player_roll1}.'")
                computer_roll1=random.randint(1,6)
                typewrite(f"[Ethan Dean]'I rolled a {computer_roll1}.'")
                if player_roll1 > computer_roll1:
                    typewrite("[Ethan Dean]'You win! Again?'")
                elif player_roll1 < computer_roll1:
                    typewrite("[Ethan Dean]'I win! Again?'")
                elif player_roll1 == computer_roll1:
                    typewrite("[Ethan Dean]'It's a tie! Again?'")
            if dice == 2:
                player_roll1=random.randint(1,6)
                player_roll2=random.randint(1,6)
                typewrite(f"[Ethan Dean]'You rolled a {player_roll1} & {player_roll2}.'")
                computer_roll1=random.randint(1,6)
                computer_roll2=random.randint(1,6)
                typewrite(f"'I rolled a {computer_roll1} & {computer_roll2}.'")
                if player_roll1+player_roll2 > computer_roll1+computer_roll2:
                    typewrite("[Ethan Dean]'You win! Again?'")
                elif player_roll1+player_roll2 < computer_roll1+computer_roll2:
                    typewrite("[Ethan Dean]'I win! Again?'")
                elif player_roll1+player_roll2 == computer_roll1+computer_roll2:
                    typewrite("[Ethan Dean]'It's a tie! Again?'")
            if dice == 3:
                player_roll1=random.randint(1,6)
                player_roll2=random.randint(1,6)
                player_roll3=random.randint(1,6)
                typewrite(f"[Ethan Dean]'You rolled a {player_roll1} & {player_roll2} & {player_roll3}.'")
                computer_roll1=random.randint(1,6)
                computer_roll2=random.randint(1,6)
                computer_roll3=random.randint(1,6)
                typewrite(f"[Ethan Dean]'I rolled a {computer_roll1} & {computer_roll2} & {computer_roll3}.'")
                if player_roll1+player_roll2+player_roll3 > computer_roll1+computer_roll2+computer_roll3:
                    typewrite("[Ethan Dean]'You win! Again?'")
                elif player_roll1+player_roll2+player_roll3 < computer_roll1+computer_roll2+computer_roll3:
                    typewrite("[Ethan Dean]'I win! Again?'")
                elif player_roll1+player_roll2+player_roll3 == computer_roll1+computer_roll2+computer_roll3:
                    typewrite("[Ethan Dean]'It's a tie! Again?'")
stars=""
wrong_guesses=0
def mini_game_3():
    global stars, wrong_guesses
    typewrite("[Ethan Dean]'Thanks! Lets play Hangman!'")
    typewrite("Ethan pulls out a board & draws on it.")
    word_bank = ["apple", "spring", "supercalifragalistic", "tek rex", "computers", "balatro", "genocide, tyler gave me that idea", "aracnaphobia", "dogfight", "hanging tree", "hanging chad", "dark peak", "star tree town", "northston town", "southston town", "weston town", "easton town", "starting field", "ice field", "farover hill", "halted river cave"]
    word=random.choice(word_bank)
    stars=""
    for i in range(len(word)):
        stars = stars + "-"
    wrong_guesses=0
    past_guesses=[" ",","]
    def hang_main():
        while True:
            if wrong_guesses>=7:
                break
            if not "-" in stars:
                typewrite(f"[Ethan Dean]'Congratulations, you've won! The word was {word}'")
                break
            typewrite("Past guesses: ")
            for past_guess in past_guesses:
                print(past_guess, end=" ")
            print()
            typewrite("[Ethan Dean]'Guess any letter in the word'\n")
            typewrite(stars)
            guess = input("Please enter a letter:\n").lower()
            if guess not in past_guesses:
                hang(guess)
            elif guess in past_guesses:
                no()
    def no():
        typewrite("[Ethan Dean]'You've already guessed that letter! Guess another!'")
    def hang(guess):
        global stars, wrong_guesses
        new_stars=""
        past_guesses.append(guess)
        for letter in word:
            if letter == guess:
                new_stars=new_stars + letter
            elif letter in past_guesses:
                new_stars = new_stars + letter
            else:
                new_stars=new_stars + "-"
        if stars == new_stars:
            wrong_guesses = wrong_guesses+1
            typewrite("[Ethan Dean]'That guess was wrong, try again!'")
            hangman_image()
        stars=new_stars
    def hangman_image():
        match wrong_guesses:
            case 1:
                typewrite("[Ethan Dean]'Wrong guess, try again'")
                print("\n\n\n")
                typewrite("___|___")
                print()
            case 2:
                typewrite("[Ethan Dean]'Wrong guess, try again'")
                typewrite("   |")
                typewrite("   |")
                typewrite("   |")
                typewrite("   |")
                typewrite("   |")
                typewrite("   |")
                typewrite("   |")
                typewrite("___|___")
            case 3:
                typewrite("[Ethan Dean]'Wrong guess, try again'")
                typewrite("   ____________")
                typewrite("   |")
                typewrite("   |")
                typewrite("   |")
                typewrite("   |")
                typewrite("   |")
                typewrite("   |")
                typewrite("   | ")
                typewrite("___|___")
            case 4:
                typewrite("[Ethan Dean]'Wrong guess, try again'")
                typewrite("   ____________")
                typewrite("   |          _|_")
                typewrite("   |         /   \\")
                typewrite("   |        |     |")
                typewrite("   |         \\_ _/")
                typewrite("   |")
                typewrite("   |")
                typewrite("   |")
                typewrite("___|___")
            case 5:
                typewrite("[Ethan Dean]'Wrong guess, try again'")
                typewrite("   ____________")
                typewrite("   |          _|_")
                typewrite("   |         /   \\")
                typewrite("   |        |     |")
                typewrite("   |         \\_ _/")
                typewrite("   |           |")
                typewrite("   |           |")
                typewrite("   |")
                typewrite("___|___")
            case 6:
                typewrite("[Ethan Dean]'Wrong guess, try again'")
                typewrite("   ____________")
                typewrite("   |          _|_")
                typewrite("   |         /   \\")
                typewrite("   |        |     |")
                typewrite("   |         \\_ _/")
                typewrite("   |           |")
                typewrite("   |           |")
                typewrite("   |          / \\ ")
                typewrite("___|___      /   \\")
            case 7:
                typewrite("[Ethan Dean]'GAME OVER! You lost!'")
                typewrite("   ____________")
                typewrite("   |          _|_")
                typewrite("   |         /   \\")
                typewrite("   |        |     |")
                typewrite("   |         \\_ _/")
                typewrite("   |          _|_")
                typewrite("   |         / | \\")
                typewrite("   |          / \\ ")
                typewrite("___|___      /   \\")
                typewrite(f"[Ethan Dean]'The word was {word}.'")
    hang_main()
def mini_game_4():
    global location
    typewrite("[Ethan Dean]'Thanks! Lets play a number guessing game! Do you want to choose or guess a number?'")
    typewrite("[Enter Guess or Choose]")
    guess_or_choose=input()
    if guess_or_choose.lower()=="guess":
        typewrite("[Ethan Dean]'Alright! I'll choose a number between 1 & 10, & you have to guess it. Got it?'")
        ethan_choice=random.randint(1,10)
        typewrite("[Ethan Dean]'I got my number! Now guess!'")
        player_guess=int(input())
        if player_guess==ethan_choice:
            typewrite("[Ethan Dean]'You guessed my number! Good job!'")
            typewrite("[Ethan Dean]'Have fun on your quest! Bye!'")
        if player_guess!=ethan_choice:
            typewrite(f"[Ethan Dean]'That is not my number. My number was {ethan_choice}.'")
            typewrite("[Ethan Dean]'Have fun on your quest! Bye!'")
    elif guess_or_choose.lower()=="choose":
        typewrite("[Ethan Dean]'Alright! You choose a number between 1 & 10, & I'll try to guess it.'")
        player_choice=0
        ethan_guess=random.randint(1,10)
        while player_choice<1 or player_choice>10:
            typewrite("Choose a number between 1 & 10")
            player_choice=int(input())
            if player_choice<1 or player_choice>10:
                typewrite("You can't choose that number! It is not between 1 & 10.")
        typewrite(f"[Ethan Dean]'Got your number? Good. I guess the number {ethan_guess}.'")
        if ethan_guess==player_choice:
            typewrite(f"[{player_name_first} {player_name_last}]'That's my number! Good job!'")
            typewrite("[Ethan Dean]'Thanks. Thank you for playing, & have fun on your adventure! Bye!'")
        if ethan_guess!=player_choice:
            typewrite(f"[{player_name_first} {player_name_last}]'That is not my number. Good try!'")
            typewrite("[Ethan Dean]'Thanks. Thank you for playing, & have fun on your adventure! Bye!'")
    else:
        typewrite("[Error. Choice not allowed. Please try a valid option next time.]")
aces=["A ♠","A ♡","A ♣","A ♢"]
twos=["2 ♠","2 ♡","2 ♣","2 ♢"]
threes=["3 ♠","3 ♡","3 ♣","3 ♢"]
fours=["4 ♠","4 ♡","4 ♣","4 ♢"]
fives=["5 ♠","5 ♡","5 ♣","5 ♢"]
sixes=["6 ♠","6 ♡","6 ♣","6 ♢"]
sevens=["7 ♠","7 ♡","7 ♣","7 ♢"]
eights=["8 ♠","8 ♡","8 ♣","8 ♢"]
nines=["9 ♠","9 ♡","9 ♣","9 ♢"]
tens=["10 ♠","10 ♡","10 ♣","10 ♢"]
jacks=["J ♠","J ♡","J ♣","J ♢"]
queens=["Q ♠","Q ♡","Q ♣","Q ♢"]
kings=["K ♠","K ♡","K ♣","K ♢"]
ethan_score=0
player_score=0
hit_or_stand_dec="[Error]"
ethan_hit=False
play_again="[Error]"
def mini_game_5():
    global hit_or_stand_dec, ethan_hit, ethan_score, player_score, play_again
    typewrite("[Ethan Dean]'Thanks! Lets play Black Jack!'")
    play_again=True
    while play_again!=False:
        player_score=0
        ethan_score=0
        ethan_card_1="[Error]"
        ethan_card_2="[Error]"
        ethan_card_3="[Error]"
        ethan_card_4="[Error]"
        ethan_card_5="[Error]"
        player_card_1="[Error]"
        player_card_2="[Error]"
        player_card_3="[Error]"
        player_card_4="[Error]"
        player_card_5="[Error]"
        cards=["A ♠","2 ♠","3 ♠","4 ♠","5 ♠","6 ♠","7 ♠","8 ♠","9 ♠","10 ♠","J ♠","Q ♠","K ♠","A ♡","2 ♡","3 ♡","4 ♡","5 ♡","6 ♡","7 ♡","8 ♡","9 ♡","10 ♡","J ♡","Q ♡","K ♡","A ♣","2 ♣","3 ♣","4 ♣","5 ♣","6 ♣","7 ♣","8 ♣","9 ♣","10 ♣","J ♣","Q ♣","K ♣","A ♢","2 ♢","3 ♢","4 ♢","5 ♢","6 ♢","7 ♢","8 ♢","9 ♢","10 ♢","J ♢","Q ♢","K ♢"]
        typewrite("[Ethan Dean]'I'll deal the cards. You can go up to 5 cards. And aces are always 11 points.'")
        typewrite("[Ethan Dean]'Here:'")
        ethan_card_1=random.choice(cards)
        cards.remove(ethan_card_1)
        player_card_1=random.choice(cards)
        cards.remove(player_card_1)
        ethan_card_2=random.choice(cards)
        cards.remove(ethan_card_2)
        player_card_2=random.choice(cards)
        cards.remove(player_card_2)
        typewrite("Ethan's Cards:       Your Cards:")
        typewrite(f"{ethan_card_1}  ?                {player_card_1}  {player_card_2}")
        increase_player_score(player_card_1)
        increase_player_score(player_card_2)
        hit_or_stand()
        if hit_or_stand_dec=="stand":
            typewrite("[Ethan Dean] Okay! My turn! First I'll flip over my other card.")
            typewrite("Ethan's Cards:")
            typewrite(f"{ethan_card_1}  {ethan_card_2}")
            increase_ethan_score(ethan_card_1)
            increase_ethan_score(ethan_card_2)
            ethan_hit_or_stand()
            if ethan_hit==True:
                ethan_card_3==random.choice(cards)
                cards.remove(ethan_card_3)
                typewrite(f"[Ethan Dean]'I drew a {ethan_card_3}.'")
                increase_ethan_score(ethan_card_3)
                ethan_hit_or_stand()
                if ethan_hit==True:
                    ethan_card_4==random.choice(cards)
                    cards.remove(ethan_card_4)
                    typewrite(f"[Ethan Dean]'I drew a {ethan_card_4}.'")
                    increase_ethan_score(ethan_card_4)
                    ethan_hit_or_stand()
                    if ethan_hit==True:
                        ethan_card_5==random.choice(cards)
                        cards.remove(ethan_card_5)
                        typewrite(f"[Ethan Dean]'I drew a {ethan_card_5}.'")
                        increase_ethan_score(ethan_card_5)
                    elif ethan_hit==False:
                        typewrite("[Ethan Dean]'I choose not to hit. Too risky.'")
                        determine_winner()
                elif ethan_hit==False:
                    typewrite("[Ethan Dean]'I choose not to hit. Too risky.'")
                    determine_winner()
            elif ethan_hit==False:
                typewrite("[Ethan Dean]'I choose not to hit. Too risky.'")
                determine_winner()
        elif hit_or_stand_dec=="hit":
            typewrite("[Ethan Dean]'Okay! Here's your card.'")
            player_card_3=random.choice(cards)
            cards.remove(player_card_3)
            increase_player_score(player_card_3)
            typewrite(f"You drew a {player_card_3}.")
            if player_score>=21:
                determine_winner()
            elif player_score<21:
                hit_or_stand()
                if hit_or_stand_dec=="stand":
                    typewrite("[Ethan Dean] Okay! My turn! First I'll flip over my other card.")
                    typewrite("Ethan's Cards:")
                    typewrite(f"{ethan_card_1}  {ethan_card_2}")
                    increase_ethan_score(ethan_card_1)
                    increase_ethan_score(ethan_card_2)
                    ethan_hit_or_stand()
                    if ethan_hit==True:
                        ethan_card_3==random.choice(cards)
                        cards.remove(ethan_card_3)
                        typewrite(f"[Ethan Dean]'I drew a {ethan_card_3}.'")
                        increase_ethan_score(ethan_card_3)
                        ethan_hit_or_stand()
                        if ethan_hit==True:
                            ethan_card_4==random.choice(cards)
                            cards.remove(ethan_card_4)
                            typewrite(f"[Ethan Dean]'I drew a {ethan_card_4}.'")
                            increase_ethan_score(ethan_card_4)
                            ethan_hit_or_stand()
                            if ethan_hit==True:
                                ethan_card_5==random.choice(cards)
                                cards.remove(ethan_card_5)
                                typewrite(f"[Ethan Dean]'I drew a {ethan_card_5}.'")
                                increase_ethan_score(ethan_card_5)
                            elif ethan_hit==False:
                                typewrite("[Ethan Dean]'I choose not to hit. Too risky.'")
                                determine_winner()
                        elif ethan_hit==False:
                            typewrite("[Ethan Dean]'I choose not to hit. Too risky.'")
                            determine_winner()
                    elif ethan_hit==False:
                        typewrite("[Ethan Dean]'I choose not to hit. Too risky.'")
                        determine_winner()
                elif hit_or_stand_dec=="hit":
                    typewrite("[Ethan Dean]'Okay! Here's your card.'")
                    player_card_4=random.choice(cards)
                    cards.remove(player_card_4)
                    increase_player_score(player_card_4)
                    typewrite(f"You drew a {player_card_4}.")
                    if player_score>=21:
                        determine_winner()
                    elif player_score<21:
                        hit_or_stand()
                        if hit_or_stand_dec=="stand":
                            typewrite("[Ethan Dean] Okay! My turn! First I'll flip over my other card.")
                            typewrite("Ethan's Cards:")
                            typewrite(f"{ethan_card_1}  {ethan_card_2}")
                            increase_ethan_score(ethan_card_1)
                            increase_ethan_score(ethan_card_2)
                            ethan_hit_or_stand()
                            if ethan_hit==True:
                                ethan_card_3==random.choice(cards)
                                cards.remove(ethan_card_3)
                                typewrite(f"[Ethan Dean]'I drew a {ethan_card_3}.'")
                                increase_ethan_score(ethan_card_3)
                                ethan_hit_or_stand()
                                if ethan_hit==True:
                                    ethan_card_4==random.choice(cards)
                                    cards.remove(ethan_card_4)
                                    typewrite(f"[Ethan Dean]'I drew a {ethan_card_4}.'")
                                    increase_ethan_score(ethan_card_4)
                                    ethan_hit_or_stand()
                                    if ethan_hit==True:
                                        ethan_card_5==random.choice(cards)
                                        cards.remove(ethan_card_5)
                                        typewrite(f"[Ethan Dean]'I drew a {ethan_card_5}.'")
                                        increase_ethan_score(ethan_card_5)
                                    elif ethan_hit==False:
                                        typewrite("[Ethan Dean]'I choose not to hit. Too risky.'")
                                        determine_winner()
                                elif ethan_hit==False:
                                    typewrite("[Ethan Dean]'I choose not to hit. Too risky.'")
                                    determine_winner()
                            elif ethan_hit==False:
                                typewrite("[Ethan Dean]'I choose not to hit. Too risky.'")
                                determine_winner()
                        elif hit_or_stand_dec=="hit":
                            typewrite("[Ethan Dean]'Okay! Here's your card.'")
                            player_card_5=random.choice(cards)
                            cards.remove(player_card_5)
                            increase_player_score(player_card_5)
                            typewrite(f"You drew a {player_card_5}.")
                            typewrite("[Ethan Dean] Okay! My turn! First I'll flip over my other card.")
                            typewrite("Ethan's Cards:")
                            typewrite(f"{ethan_card_1}  {ethan_card_2}")
                            increase_ethan_score(ethan_card_1)
                            increase_ethan_score(ethan_card_2)
                            ethan_hit_or_stand()
                            if ethan_hit==True:
                                ethan_card_3==random.choice(cards)
                                cards.remove(ethan_card_3)
                                typewrite(f"[Ethan Dean]'I drew a {ethan_card_3}.'")
                                increase_ethan_score(ethan_card_3)
                                ethan_hit_or_stand()
                                if ethan_hit==True:
                                    ethan_card_4==random.choice(cards)
                                    cards.remove(ethan_card_4)
                                    typewrite(f"[Ethan Dean]'I drew a {ethan_card_4}.'")
                                    increase_ethan_score(ethan_card_4)
                                    ethan_hit_or_stand()
                                elif ethan_hit==False:
                                    typewrite("[Ethan Dean]'I choose not to hit. Too risky.'")
                                    if ethan_hit==True:
                                        ethan_card_5==random.choice(cards)
                                        cards.remove(ethan_card_5)
                                        typewrite(f"[Ethan Dean]'I drew a {ethan_card_5}.'")
                                        increase_ethan_score(ethan_card_5)
                                    elif ethan_hit==False:
                                        typewrite("[Ethan Dean]'I choose not to hit. Too risky.'")
                            elif ethan_hit==False:
                                typewrite("[Ethan Dean]'I choose not to hit. Too risky.'")
                            determine_winner()
def increase_player_score(player_card):
    global player_score, aces, twos, threes, fours, fives, sixes, sevens, eights, nines, tens, jacks, queens, kings
    if player_card in aces:
        player_score=player_score+11
    elif player_card in twos:
        player_score=player_score+2
    elif player_card in threes:
        player_score=player_score+3
    elif player_card in fours:
        player_score=player_score+4
    elif player_card in fives:
        player_score=player_score+5
    elif player_card in sixes:
        player_score=player_score+6
    elif player_card in sevens:
        player_score=player_score+7
    elif player_card in eights:
        player_score=player_score+8
    elif player_card in nines:
        player_score=player_score+9
    elif player_card in tens:
        player_score=player_score+10
    elif player_card in jacks:
        player_score=player_score+10
    elif player_card in queens:
        player_score=player_score+10
    elif player_card in kings:
        player_score=player_score+10
    return player_score
def increase_ethan_score(ethan_card):
    global ethan_score, aces, twos, threes, fours, fives, sixes, sevens, eights, nines, tens, jacks, queens, kings
    if ethan_card in aces:
        ethan_score=ethan_score+11
    elif ethan_card in twos:
        ethan_score=ethan_score+2
    elif ethan_card in threes:
        ethan_score=ethan_score+3
    elif ethan_card in fours:
        ethan_score=ethan_score+4
    elif ethan_card in fives:
        ethan_score=ethan_score+5
    elif ethan_card in sixes:
        ethan_score=ethan_score+6
    elif ethan_card in sevens:
        ethan_score=ethan_score+7
    elif ethan_card in eights:
        ethan_score=ethan_score+8
    elif ethan_card in nines:
        ethan_score=ethan_score+9
    elif ethan_card in tens:
        ethan_score=ethan_score+10
    elif ethan_card in jacks:
        ethan_score=ethan_score+10
    elif ethan_card in queens:
        ethan_score=ethan_score+10
    elif ethan_card in kings:
        ethan_score=ethan_score+10
    return ethan_score
def hit_or_stand():  
    global hit_or_stand_dec
    typewrite("[Ethan Dean]'Do you want to hit or stand?'\n[Input Hit or Stand.]")
    hit_or_stand_dec=input()
    return hit_or_stand_dec
def ethan_hit_or_stand():
    global ethan_score, player_score
    if player_score<21 and ethan_score<21:
        if ethan_score<18:
            ethan_hit=True
        elif ethan_score>18 and player_score>ethan_score:
            ethan_hit=True
        elif ethan_score>=18 and player_score<ethan_score:
            ethan_hit=False
        elif ethan_score>=21:
            ethan_hit=False
        return ethan_hit
def determine_winner():
    global player_score, ethan_score, play_again
    typewrite(f"Your Score: {player_score}")
    typewrite(f"Ethan's Score: {ethan_score}")
    if player_score==21:
        typewrite("[Ethan Dean]'Congrats, you win! Good game!'")
    elif ethan_score==21:
        typewrite("[Ethan Dean]'I won! Good game!'")
    elif player_score>21:
        typewrite("[Ethan_Dean]'You bust! I win! Good game!'")
    elif ethan_score>21:
        typewrite("[Ethan Dean]'I bust! You win! Good game!'")
    elif player_score>ethan_score:
        typewrite("[Ethan Dean]'Congrats! You won! Good game!'")
    elif ethan_score>player_score:
        typewrite("[Ethan Dean]'I win! Good game!'")
    typewrite("[Ethan Dean]'Do you want to play again?' [Yes or No]")
    play_again_dec=input()
    if play_again_dec.lower()=="yes":
        play_again=True
    if play_again_dec.lower()=="no":
        play_again=False
    return play_again
def main_game():
    global choice, has_map, health, enemies_killed, full_path
    load_dec=input("Do you want to load a save? [y or n]\n")
    save_file_options = [1, 2, 3]
    while load_dec != "y" and load_dec != "n":
        load_dec = input("Error. invalid option. Please enter a vaild option. [y or n]\n")
    if load_dec.lower() == "n":
        world()
        start()
    elif load_dec.lower() == "y":
        load_option = int(input("Which save file do you want to load? [1, 2, or 3]\n"))
        while load_option not in save_file_options:
            load_option = int(input("Error, invalid option. Please enter a vaild option. [1, 2, or 3]\n"))
        if load_option == 1:
            read_save(save_file_1)
        if load_option == 2:
            read_save(save_file_2)
        if load_option == 3:
            read_save(save_file_2)
    while health > 0:
        typewrite(f"You have {health} hp points.")
        decision()
        if choice.lower()=="map":
            if has_map==True:
                map()
            if has_map==False:
                typewrite("You don't have a map yet! You can't check one! Perhaps you could get one from a nearby town?")
        elif choice.lower()=="talk" or choice.lower()=="greet npc":
            greet_npc()
        elif choice.lower()=="get map":
            if in_town==True:
                get_map()
            if in_town==False:
                typewrite("You can't seem to find a map anywhere! Perhaps a nearby town has one, why don't you try 'travel'ing?")
        elif choice.lower()=="check inventory":
            check_inventory()
        elif choice.lower()=="travel":
            travel()
        elif choice.lower()=="search":
            search()
        elif choice.lower()=="help":
            help()
        elif choice.lower()=="quit":
            typewrite("Are you sure you want to quit? Your progress can not be saved.")
            typewrite("[Yes or No]")
            quit_decision=input()
            if quit_decision=="yes":
                typewrite("Alright then, goodbye.")
                death()
            if quit_decision=="no":
                typewrite("Okay then, continue on.")
        elif choice.lower()=="rest" or choice.lower()=="sleep":
            sleep()
        elif choice.lower()=="boss fight":
            if enemies_killed>=25:
                boss()
                if final_boss=="Drakon":
                    boss_fight(50,12)
                if final_boss=="Avos":
                    boss_fight(50,10)
                if final_boss=="Davilith":
                    boss_fight(50,11)
                if final_boss=="Belos":
                    boss_fight(50,9)
                if final_boss=="Daygon":
                    boss_fight(50,11)
                if final_boss=="Knightmare":
                    boss_fight(50,12)
            if enemies_killed<25:
                typewrite("You can not find the monster of dark peak. They do not see you as worth their time. Perhaps Defeating some of the monsters paluging this land will change their mind. [Defeat 25 enemies.]")
        elif choice.lower()=="status check" or choice.lower()=="check stats":
            profile()
        elif choice.lower()=="clear console":
            console_clear()
        elif choice.lower()=="list check":
            list_check()
        elif choice.lower()=="mini game":
            play_mini_games()
        elif choice.lower()=="save":
            save_dec = int(input("What save file do you want to save to? [1, 2, or 3]\n"))
            while save_dec not in save_file_options:
                save_dec = int(input("Error, invalid save_file. Please enter a vaild option. [1, 2, or 3]\n"))
            if save_dec == 1:
                save_game(save_file_1)
            if save_dec == 2:
                save_game(save_file_2)
            if save_dec == 3:
                save_game(save_file_3)
        else:
            typewrite("[Error command not recognized] Try checking your spelling or try asking for 'help'")
main_game()