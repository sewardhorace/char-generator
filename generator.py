#Random Character Generator, options for background and description.

import random as r

#Lots of globals...
class Character:
    def __init__(self):
        self.Abilities = []
        for i in range(6):
            self.Abilities.append(0)
        self.Mods = []
        for i in range(6):
            self.Mods.append(0)
        self.Race = ''
        self.Subrace = ''
        self.Size = ''
        self.Speed = 0
        self.Cla = '' #Class
        self.Back = ''
        self.HP = 0
        self.AC = 10
        self.Initiative = 0

    #all added to Proficiencies dictionary before printing (bottom)
        self.Saves = []
        for i in range(6):
            self.Saves.append(0)
        self.Skills = set()
        self.WeaponProficiencies = set()
        self.ArmorProficiencies = set()
        self.OtherProficiencies = set()
        self.Languages = set()
        self.Features = set()
    #
        self.Attacks = [] #four-part entries? [weapon, str/dex, attack, damage]
        self.Equipment = set()

    #Spells
        self.SpellList = {0:set(), 1:set()}
        self.SpellSlots = {} #each index is the spell level
        self.SpellPrep = 0

        self.Description = {} #dictionary, move to the end after entries are assigned
    #Description below here
        self.Age = 0
        self.Height = 0
        self.Weight = 0
        self.Traits = set()
        self.Ideals = set()
        self.Bonds = set()
        self.Flaws = set()

#Huge index of items
class DataBase:
    def __init__(self):
        self.ARMOR = [
            'Padded',           #0
            'Leather',          #1
            'Studded Leather',  #2
            'Hide',             #3
            'Chain Shirt',      #4
            'Scale Mail',       #5
            'Breastplate',      #6
            'Half Plate',       #7
            'Ring Mail',        #8
            'Chain Mail',       #9
            'Splint',           #10
            'Plate',            #11
            'Shield',           #12
            'light',            #13
            'medium',           #14
            'heavy',            #15            
            ]
        self.WEAPONS = [
            'club',             #0 Simple Weapons
            'dagger',           #1
            'greatclub',        #2
            'handaxe',          #3
            'javelin',          #4
            'light hammer',     #5
            'mace',             #6
            'quarterstaff',     #7
            'sickle',           #8
            'spear',            #9
            'unarmed strike',    #10
            'light crossbow',   #11 Simple Ranged
            'dart',             #12
            'shortbow',         #13
            'sling',            #14
            'battleaxe',        #15 Martial Weapons
            'flail',            #16
            'glaive',           #17
            'greataxe',         #18
            'greatsword',       #19
            'halberd',          #20
            'lance',            #21
            'longsword',        #22
            'maul',             #23
            'morningstar',      #24
            'pike',             #25
            'rapier',           #26
            'scimitar',         #27
            'shortsword',       #28
            'trident',          #29
            'war pick',         #30
            'warhammer',        #31
            'whip',             #32
            'blowgun',          #33 Martial Ranged
            'hand crossbow',    #34
            'heavy crossbow',   #35
            'longbow',          #36
            'net',              #37
            'simple weapons',   #38 Categories
            'martial weapons',  #39
            ]
        self.GEAR = [
            'Arrows (20)',
            'Blowgun Needles (50)',
            'Crossbow Bolts (20)',
            'Sling Bullets (20)',
            'Crystal (focus)',
            'Orb (focus)',
            'Rod (focus)',
            'Staff (focus)',
            'Wand (focus)',
            'Sprig of Mistletoe (focus)',
            'Totem (focus)',
            'Wooden Staff (focus)',
            'Yew Wand (focus)',
            'Amulet (holy symbol)',
            'Emblem (holy symbol)',
            'Reliquary (holy symbol)',
            ]
        self.TOOLS = [
            'Alchemist\'s supplies',    #0 artisan tools
            'Brewer\'s supplies',       #1
            'Calligrapher\'s supplies', #2
            'Carpenter\'s tools',       #3
            'Cartographer\'s tools',    #4
            'Cobbler\'s tools',         #5
            'Cook\'s utensils',         #6
            'Glassblower\'s tools',     #7
            'Jeweler\'s tools',         #8
            'Leatherworker\'s tools',   #9
            'Mason\'s tools',           #10
            'Painter\'s supplies',      #11
            'Potter\'s tools',          #12
            'Smith\'s tools',           #13
            'Tinker\'s tools',          #14
            'Weaver\'s tools',          #15
            'Woodcarver\'s tools',      #16
            'Dice set',                 #17 gaming sets
            'Dragonchess set',          #18
            'Playing card set',         #19
            'Three-Dragon Ante set',    #20
            'Herbalism kit',            #21 kits
            'Disguise kit',             #22
            'Forgery kit',              #23
            'Poisoner\'s tools',        #24
            'Theives\' tools',          #25
            'Navigator\'s tools',       #26 navigating/vehicles
            'Land vehicles',            #27
            'Water vehicles',           #28
            'Bagpipes',                 #29 instruments
            'Drum',                     #30
            'Dulcimer',                 #31
            'Flute',                    #32
            'Lute',                     #33
            'Lyre',                     #34
            'Horn',                     #35
            'Pan flute',                #36
            'Shawm',                    #37
            'Viol'                      #38
            ]
        self.LANGOPT = [
            'Common',       #0
            'Dwarvish',     #1
            'Elvish',       #2
            'Giant',        #3
            'Gnomish',      #4
            'Goblin',       #5
            'Halfling',     #6
            'Orc',          #7
            'Abyssal',      #8
            'Celestial',    #9
            'Draconic',     #10
            'Deep Speech',  #11
            'Infernal',     #12
            'Primordial',   #13
            'Sylvan',       #14
            'Undercommon'   #15
            ]
        self.SKILLSOPT = [
            'Athletics',        #0 Str
            'Acrobatics',       #1 Dex
            'Sleight of Hand',  #2
            'Stealth',          #3
            'Arcana',           #4 Int
            'History',          #5
            'Investigation',    #6
            'Nature',           #7
            'Religion',         #8
            'Animal Handling',  #9 Wis
            'Insight',          #10
            'Medicine',         #11
            'Perception',       #12
            'Survival',         #13
            'Deception',        #14 Cha
            'Intimidation',     #15
            'Performance',      #16
            'Persuasion',       #17
            ]
        #Class Spell Lists
        self.WIZ = {
            0:[
                'Acid Splash',      #0
                'Blade Ward',       #1
                'Chill Touch',      #2
                'Dancing Lights',   #3
                'Fire Bolt',        #4
                'Friends',          #5
                'Light',            #6
                'Mage Hand',        #7
                'Mending',          #8
                'Message',          #9
                'Minor Illusion',   #10
                'Poison Spray',     #11
                'Prestidigitation', #12
                'Ray of Frost',     #13
                'Shocking Grasp',   #14
                'True Strike'       #15
                ]
            }

def rollOne(number):
    #roll 1d(whatever), return the result
    return r.randint(1,number)

def rollX(numberOfDice, numberOfSides):
    #roll xd(whatever), return the result
    total = 0
    while numberOfDice > 0:
        i = rollOne(numberOfSides)
        total += i
        numberOfDice -= 1
    return total
    
def rollFour():
    #roll 4d6, remove the lowest roll, return the total
    rolls = []
    total = 0
    while len(rolls) < 4:
        i = rollX(1,6)
        rolls.append(i)
    rolls.sort()
    rolls.pop(0)
    for i in rolls:
        total += i
    return total

def rollAbilities(Abilities):
    #assign rolls to six ability stats
    for i in range(6):
        Abilities[i]+=rollFour()

##def getMod(Ability):
##    #returns ability modifier for given ability score
##    return (Ability//2)-5

def getAllMod(Mods,Abilities):
    #returns the ability modifiers for all ability scores
    for i in range(6):
        #Mods[i]+=getMod(Abilities[i])
        Mods[i]+=((Abilities[i]//2)-5)
    
def randSelect(options, amount, destinationSet):
    #adds an amount of options chosen at random to a destination set
    #for spells, indicate spell level in options and destination
    #ex. (D.WIZ[0],amount,C.SpellList[0])
    i = len(destinationSet)
    while len(destinationSet)<i+amount:
        j = options[r.randint(0,len(options)-1)]
        if j not in destinationSet:
            destinationSet.add(j)

def randPhys(baseHeightInches, HeightMod, BaseWeight, WeightMod, BaseAge, AgeMod):
    #random height and weight and starting age
    #use rollX(x,y) for mods
    Height = baseHeightInches+HeightMod
    C.Height = str(Height//12)+'\''+str(Height%12)+'\"'
    C.Weight = BaseWeight+(WeightMod*HeightMod)
    C.Age = BaseAge+AgeMod

def race(Race):
    #assigns a base race
    #note = revise this as a list CONSTANT, as above
    races = ['Dwarf', 'Elf', 'Halfling', 'Human'
             #, 'Dragonborn', 'Gnome', 'Half-Elf', 'Half-Orc', 'Tiefling']
             ]
    Race = races[r.randint(0, len(races)-1)]

def cla():
    #assigns a class to the global Cla
    # revise this as a list CONSTANT as above
    classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk',
               'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']
    C.Cla = classes[r.randint(0, len(classes)-1)]

def raceStats():
    #sets subrace, description, djusts ability scores based on race and subrace
    if C.Race == 'Dwarf':
        C.Abilities[2]+=2
        C.Size = 'Medium'
        C.Speed = 25
        C.Features.add('Darkvision')
        C.Features.add('Dwarven Resilience')
        C.Features.add('Dwarven Combat Training')
        C.WeaponProficiencies.add(D.WEAPONS[15])
        C.WeaponProficiencies.add(D.WEAPONS[3])
        C.WeaponProficiencies.add(D.WEAPONS[5])
        C.WeaponProficiencies.add(D.WEAPONS[31])
        randSelect([D.TOOLS[1],D.TOOLS[13],D.TOOLS[10]],1,C.OtherProficiencies)
        C.Features.add('Stonecunning')
        C.Languages.add(D.LANGOPT[0])
        C.Languages.add(D.LANGOPT[1])
        subs = ['Hill ', 'Mountain ']
        C.Subrace = subs.pop(r.randint(0, len(subs)-1))
        if C.Subrace == 'Hill ':
            C.Abilities[4]+=1
            C.Features.add('Dwarven Toughness')
            C.HP += 1
            randPhys(44,rollX(2,4),115,rollX(2,6),40,rollX(3,14))
        else:
            C.Abilities[0]+=2
            C.Features.add('Dwarven Armor Training')
            C.ArmorProficiencies.add(D.ARMOR[13])
            C.ArmorProficiencies.add(D.ARMOR[14])
            randPhys(48,rollX(2,4),130,rollX(2,6),40,rollX(3,14))
            
    elif C.Race == 'Elf':
        C.Abilities[1]+=2
        C.Size = 'Medium'
        C.Speed = 30
        C.Features.add('Darkvision')
        C.Features.add('Keen Senses')
        C.Skills.add('Perception')
        C.Features.add('Fey Ancestry')
        C.Features.add('Trance')
        C.Languages.add(D.LANGOPT[0])
        C.Languages.add(D.LANGOPT[2])
        subs = ['High ', 'Wood ', 'Dark ']
        C.Subrace = subs.pop(r.randint(0, len(subs)-1))
        if C.Subrace == 'High ':
            C.Abilities[3]+=1
            C.Features.add('Elf Weapon Training')
            C.WeaponProficiencies.add(D.WEAPONS[22])
            C.WeaponProficiencies.add(D.WEAPONS[28])
            C.WeaponProficiencies.add(D.WEAPONS[13])
            C.WeaponProficiencies.add(D.WEAPONS[36])
            C.Features.add('Cantrip')
            randSelect(D.WIZ[0],1,C.SpellList[0])
            randSelect(D.LANGOPT,1,C.Languages)
            randPhys(54,rollX(2,10),90, rollX(1,4),110,rollX(4,15))
        elif C.Subrace == 'Wood ':
            C.Abilities[4]+=1
            C.Features.add('Elf Weapon Training')
            C.WeaponProficiencies.add(D.WEAPONS[22])
            C.WeaponProficiencies.add(D.WEAPONS[28])
            C.WeaponProficiencies.add(D.WEAPONS[13])
            C.WeaponProficiencies.add(D.WEAPONS[36])
            C.Features.add('Fleet of Foot')
            C.Speed = 35
            C.Features.add('Mask of the Wild')
            randPhys(54,rollX(2,10),100, rollX(1,4),110,rollX(4,15))
        else:
            C.Abilities[5]+=1
            C.Features.remove('Darkvision')
            C.Features.add('Superior Darkvision')
            C.Features.add('Sunlight Sensitivity')
            C.Features.add('Drow Magic')
            C.SpellList[0].add(WIZ[0][3])
            C.WeaponProficiencies.add(D.WEAPONS[26])
            C.WeaponProficiencies.add(D.WEAPONS[28])
            C.WeaponProficiencies.add(D.WEAPONS[34])
            randPhys(53,rollX(2,6),75, rollX(1,6),110,rollX(4,15))
            
    elif C.Race == 'Halfling':
        C.Abilities[1]+=2
        C.Size = 'Small'
        C.Speed = 25
        C.Features.add('Lucky')
        C.Features.add('Brave')
        C.Features.add('Halfling Nimbleness')
        C.Languages.add(D.LANGOPT[0])
        C.Languages.add(D.LANGOPT[6])
        subs = ['Lightfoot ', 'Stout ']
        C.Subrace = subs.pop(r.randint(0, len(subs)-1))
        if C.Subrace == 'Lightfoot ':
            C.Abilities[5]+=1
            C.Features.add('Naturally Stealthy')
            randPhys(31, rollX(2,4), 35, 1, 20, rollX(2,12))
        else:
            C.Abilities[2]+=1
            C.Features.add('Stout Resilience')
            randPhys(31, rollX(2,4), 35, 1, 20, rollX(2,12))
            
    elif C.Race == 'Human':
        C.Size = 'Medium'
        C.Speed = 30
        C.Languages.add(D.LANGOPT[0])
        randSelect(D.LANGOPT, 1, C.Languages)
        subs = ['', 'Variant ']
        C.Subrace = subs.pop(r.randint(0, len(subs)-1))
        if C.Subrace == '':
            for i in range(6):
                C.Abilities[i]+=1
            randPhys(56, rollX(2,10), 110, rollX(2,4), 15, rollX(1,12))
        else:
            i = r.randint(0,5)
            j = r.randint(0,5)
            while i == j:
                j = r.randint(0,5)
            C.Abilities[i]+=1
            C.Abilities[j]+=1
            randSelect(D.SKILLSOPT,1,C.Skills)
            C.Features.add('Choose 1 Feat')
            randPhys(56, rollX(2,10), 110, rollX(2,4), 15, rollX(1,12))
            
##    elif C.Race == 'Dragonborn':
##        randPhys(60,rollX(2,8),175,rollX(2,6),14,rollX(2,5))
##    elif C.Race == 'Gnome':
##        randPhys(35,rollX(2,4),35,1,40,rollX(4,13))
##    elif C.Race == 'Half-Elf':
##        randPhys(57,rollX(2,8),110,rollX(2,4),20,rollX(1,18))
##    elif C.Race == 'Half-Orc':
##        randPhys(58,rollX(2,10),140,rollX(2,6),14,rollX(1,12))
##    elif C.Race == 'Tiefling':
##        randPhys(57,rollX(2,8),110,rollX(2,4),15,rollX(1,12))
##        
##def claStats():
##    #adjusts stats for class
##    global Features
##    global WeaponProficiencies
##    global OtherProficiencies
##    global Skills
##    global SKILLSOPT
##    global Languages
##    global LANGOPT
##    global ARMOR
##    global WEAPONS
##    global GEAR
##    global TOOLS
##    global SpellList
##    global WIZ

#    if Cla == 'Barbarian':


C = Character()
D = DataBase()
rollAbilities(C.Abilities)
race(C.Race)
cla()
#back()
raceStats()
#backStats()
#claStats()

getAllMod(C.Mods,C.Abilities)

print(str(C.Subrace)+str(C.Race)+' '+str(C.Cla))
for i in range(6):
    AbName=['Str','Dex','Con','Int','Wis','Cha']
    print('%s= %d (%d)' % (AbName[i], C.Abilities[i], C.Mods[i]))
print('HP= '+str(C.HP))
print('Age = %d years, Height = %s, Weight = %d lbs.' % (C.Age,C.Height,C.Weight))
Proficiencies = {'Saves: ':C.Saves, 'Skills: ':C.Skills,
                 'Weapon Proficiencies: ':C.WeaponProficiencies,
                 'Armor Proficiencies: ':C.ArmorProficiencies,
                 'Other Proficiencies: ':C.OtherProficiencies,
                 'Features: ':C.Features,
                 'Spell List: ':C.SpellList,
                 'Languages: ':C.Languages}
for i,j in Proficiencies.items():
    print(i,j)
