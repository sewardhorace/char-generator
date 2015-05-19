#Random Character Generator, options for background and description.

import random as r

#Lots of globals...
Abilities = []
for i in range(6):
    Abilities.append(0)
Mods = []
for i in range(6):
    Mods.append(0)
Race = None
Subrace = None
Cla = None #Class
Background = None
HP = 0
AC = 10
Initiative = 0
Speed = 0
Size = None

#all added to Proficiencies dictionary before printing (bottom)
Saves = []
for i in range(6):
    Saves.append(0)
Skills = set()
WeaponProficiencies = set()
ArmorProficiencies = set()
OtherProficiencies = set()
Languages = set()
Features = set()

#
Attacks = [] #four-part entries? [weapon, str/dex, attack, damage]
Equipment = set()

#Spells
SpellList = {0:set(), 1:set()}
SpellSlots = {} #each index is the spell level
Prepared = 0

Description = {} #dictionary, move to the end after entries are assigned
#Description below here
Age = 0
Height = 0
Weight = 0
Traits = set()
Ideals = set()
Bonds = set()
Flaws = set()

#Huge index of items
ARMOR = [
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
WEAPONS = [
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
GEAR = [
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
TOOLS = [
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
LANGOPT = [
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
SKILLSOPT = [
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
WIZ = {
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

def rollStats():
    #assign rolls to six ability stats
    global Abilities
    for i in range(6):
        Abilities[i]+=rollFour()

def getMods():
    global Abilities
    global Mods
    for i in range(6):
        Mods[i]+=((Abilities[i]//2)-5)
    
def randSelect(options, amount, destinationSet):
    #adds an amount of options chosen at random to a destination set
    #for spells, indicate spell level in options and destination
    #ex. (Wiz[0],amount,SpellList[0])
    i = len(destinationSet)
    while len(destinationSet)<i+amount:
        j = options[r.randint(0,len(options)-1)]
        if j not in destinationSet:
            destinationSet.add(j)

def randPhys(baseHeightInches, HeightMod, BaseWeight, WeightMod, BaseAge, AgeMod):
    #random height and weight and starting age
    #use rollX(x,y) for mods
    global Height
    global Weight
    global Age
    Height = baseHeightInches+HeightMod
    Height = str(Height//12)+'\''+str(Height%12)+'\"'
    Weight = BaseWeight+(WeightMod*HeightMod)
    Age = BaseAge+AgeMod

def race():
    #assigns a base race
    global Race
    races = ['Dwarf', 'Elf', 'Halfling', 'Human'
             #, 'Dragonborn', 'Gnome', 'Half-Elf', 'Half-Orc', 'Tiefling']
             ]
    Race = races[r.randint(0, len(races)-1)]

def cla():
    #assigns a class to the global Cla
    global Cla
    classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk',
               'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']
    Cla = classes[r.randint(0, len(classes)-1)]

def raceStats():
    #sets subrace, description, djusts ability scores based on race and subrace
    global Race
    global Subrace
    global Abilities
    global Age
    global Size
    global Height
    global Weight
    global HP
    global Speed
    global Features
    global WeaponProficiencies
    global OtherProficiencies
    global Skills
    global Languages
    global LANGOPT
    global ARMOR
    global WEAPONS
    global GEAR
    global TOOLS
    global SpellList
    global WIZ
    Race = 'Elf'
    if Race == 'Dwarf':
        Abilities[2]+=2
        Size = 'Medium'
        Speed = 25
        Features.add('Darkvision')
        Features.add('Dwarven Resilience')
        Features.add('Dwarven Combat Training')
        WeaponProficiencies.add(WEAPONS[15])
        WeaponProficiencies.add(WEAPONS[3])
        WeaponProficiencies.add(WEAPONS[5])
        WeaponProficiencies.add(WEAPONS[31])
        randSelect([TOOLS[1],TOOLS[13],TOOLS[10]],1,OtherProficiencies)
        Features.add('Stonecunning')
        Languages.add(LANGOPT[0])
        Languages.add(LANGOPT[1])
        subs = ['Hill ', 'Mountain ']
        Subrace = subs.pop(r.randint(0, len(subs)-1))
        if Subrace == 'Hill ':
            Abilities[4]+=1
            Features.add('Dwarven Toughness')
            HP += 1
            hmod = rollX(2,4)
            Height = 44+hmod
            Height = str(Height//12)+'\''+str(Height%12)+'\"'
            wmod = rollX(2,6)
            Weight = 115+(wmod*hmod)
        else:
            Abilities[0]+=2
            Features.add('Dwarven Armor Training')
            ArmorProficiencies.add(ARMOR[13])
            ArmorProficiencies.add(ARMOR[14])
            randPhys(48,rollX(2,4),130,rollX(2,6),40,rollX(3,14))
            
    elif Race == 'Elf':
        Abilities[1]+=2
        Size = 'Medium'
        Speed = 30
        Features.add('Darkvision')
        Features.add('Keen Senses')
        Skills.add('Perception')
        Features.add('Fey Ancestry')
        Features.add('Trance')
        Languages.add(LANGOPT[0])
        Languages.add(LANGOPT[2])
        subs = ['High ', 'Wood ', 'Dark ']
        Subrace = subs.pop(r.randint(0, len(subs)-1))
        Subrace = 'High '
        if Subrace == 'High ':
            Abilities[3]+=1
            Features.add('Elf Weapon Training')
            WeaponProficiencies.add(WEAPONS[22])
            WeaponProficiencies.add(WEAPONS[28])
            WeaponProficiencies.add(WEAPONS[13])
            WeaponProficiencies.add(WEAPONS[36])
            Features.add('Cantrip')
            randSelect(WIZ[0],1,SpellList[0])
            randSelect(LANGOPT,2,Languages)
            randPhys(54,rollX(2,10),90, rollX(1,4),110,rollX(4,15))
        elif Subrace == 'Wood ':
            Abilities[4]+=1
            Features.add('Elf Weapon Training')
            WeaponProficiencies.add(WEAPONS[22])
            WeaponProficiencies.add(WEAPONS[28])
            WeaponProficiencies.add(WEAPONS[13])
            WeaponProficiencies.add(WEAPONS[36])
            Features.add('Fleet of Foot')
            Speed = 35
            Features.add('Mask of the Wild')
            randPhys(54,rollX(2,10),100, rollX(1,4),110,rollX(4,15))
        else:
            Abilities[5]+=1
            Features.remove('Darkvision')
            Features.add('Superior Darkvision')
            Features.add('Sunlight Sensitivity')
            Features.add('Drow Magic')
            SpellList[0].add(WIZ[0][3])
            WeaponProficiencies.add(WEAPONS[26])
            WeaponProficiencies.add(WEAPONS[28])
            WeaponProficiencies.add(WEAPONS[34])
            randPhys(53,rollX(2,6),75, rollX(1,6),110,rollX(4,15))
            
    elif Race == 'Halfling':
        Abilities[1]+=2
        Age = 20
        Size = 'Small'
        Speed = 25
        Features.add('Lucky')
        Features.add('Brave')
        Features.add('Halfling Nimbleness')
        Languages.add(LANGOPT[0])
        Languages.add(LANGOPT[6])
        subs = ['Lightfoot ', 'Stout ']
        Subrace = subs.pop(r.randint(0, len(subs)-1))
        if Subrace == 'Lightfoot ':
            Abilities[5]+=1
            Features.add('Naturally Stealthy')
            randPhys(31, rollX(2,4), 35, 1, 20, rollX(2,12))
        else:
            Abilities[2]+=1
            Features.add('Stout Resilience')
            randPhys(31, rollX(2,4), 35, 1, 20, rollX(2,12))
            
    elif Race == 'Human':
        Age = 18
        Size = 'Medium'
        Speed = 30
        Languages.add(LANGOPT[0])
        randSelect(LANGOPT, 2, Languages)
        subs = ['', 'Variant ']
        Subrace = subs.pop(r.randint(0, len(subs)-1))
        if Subrace == '':
            for i in range(6):
                Abilities[i]+=1
            randPhys(56, rollX(2,10), 110, rollX(2,4), 15, rollX(1,12))
        else:
            i = r.randint(0,5)
            j = r.randint(0,5)
            while i == j:
                j = r.randint(0,5)
            Abilities[i]+=1
            Abilities[j]+=1
            randSelect(SKILLSOPT,1,Skills)
            Features.add('Choose 1 Feat')
            randPhys(56, rollX(2,10), 110, rollX(2,4), 15, rollX(1,12))
            
    elif Race == 'Dragonborn':
        randPhys(60,rollX(2,8),175,rollX(2,6),14,rollX(2,5))
    elif Race == 'Gnome':
        randPhys(35,rollX(2,4),35,1,40,rollX(4,13))
    elif Race == 'Half-Elf':
        randPhys(57,rollX(2,8),110,rollX(2,4),20,rollX(1,18))
    elif Race == 'Half-Orc':
        randPhys(58,rollX(2,10),140,rollX(2,6),14,rollX(1,12))
    elif Race == 'Tiefling':
        randPhys(57,rollX(2,8),110,rollX(2,4),15,rollX(1,12))
        
def claStats():
    #adjusts stats for class
    global Features
    global WeaponProficiencies
    global OtherProficiencies
    global Skills
    global SKILLSOPT
    global Languages
    global LANGOPT
    global ARMOR
    global WEAPONS
    global GEAR
    global TOOLS
    global SpellList
    global WIZ

#    if Cla == 'Barbarian':

rollStats()
race()
cla()
#back()
raceStats()
#backStats()
#claStats()

getMods()

print(Subrace+Race+' '+Cla)
for i in range(6):
    AbName=['Str','Dex','Con','Int','Wis','Cha']
    print('%s= %d (%d)' % (AbName[i], Abilities[i], Mods[i]))
print('HP= '+str(HP))
print('Age = %d years, Height = %s, Weight = %d lbs.' % (Age,Height,Weight))
Proficiencies = {'Saves: ':Saves, 'Skills: ':Skills,
                 'Weapon Proficiencies: ':WeaponProficiencies,
                 'Armor Proficiencies: ':ArmorProficiencies,
                 'Other Proficiencies: ':OtherProficiencies,
                 'Features: ':Features,
                 'Spell List: ':SpellList,
                 'Languages: ':Languages}
for i,j in Proficiencies.items():
    print(i,j)
