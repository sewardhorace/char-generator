#should contain all data for character generation

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

class armor:
    def __init__(self,name,ac,weight=0,special=None):
        self.name = name
        self.ac = ac
        self.weight = weight
        self.special = special

PADDED = armor('padded armor',1)
LEATHER = armor('leather armor',1)
STUDDED = armor('studded leather',2)
HIDE = armor('hide armor',2,1) #medium armor weight = 1
CHAINSHIRT = armor('chain shirt',3,1)
SCALEMAIL = armor('scale mail',4,1)
BREASTPLATE = armor('breastplate',4,1)
HALFPLATE = armor('half plate',5,1)
RINGMAIL = armor('ring mail',4,2) #heavy armor weight = 2
CHAINMAIL = armor('chain mail',6,2)
SPLINT = armor('splint mail',7,2)
PLATE = armor('full plate',8,2)
SHIELD = armor('shield',2,2)
LIGHT = armor('light armor',0)# proficiencies
MEDIUM = armor('medium armor',0)
HEAVY = armor('heavy armor',0)
SHIELDS = armor('shields',0)
UNARMOREDBARB = armor('unarmored defense (barbarian)',0,0,'Barbarian')#special
UNARMOREDMONK = armor('unarmored defense (monk)',0,0,'Monk')

ARMOR = [
    PADDED,     #0
    LEATHER,    #1
    STUDDED,  #2
    HIDE,       #3
    CHAINSHIRT,      #4
    SCALEMAIL,       #5
    BREASTPLATE,      #6
    HALFPLATE,       #7
    RINGMAIL,        #8
    CHAINMAIL,       #9
    SPLINT,      #10
    PLATE,      #11
    SHIELD,           #12
    LIGHT,            #13
    MEDIUM,           #14
    HEAVY,            #15            
    SHIELDS,           #16
    UNARMOREDBARB,      #17
    UNARMOREDMONK       #18
    ]

class weapon:
    def __init__(self,name,damage,ranged=False,finesse=False,twohanded=False,number=1):
        self.name = name
        self.damage = damage
        self.ranged = ranged
        self.finesse = finesse
        self.twohanded = twohanded
        self.number = number
        
CLUB = weapon('club','1d4')
DAGGER = weapon('dagger','1d4',finesse=True)
GREATCLUB = weapon('greatclub','1d8',twohanded=True)
HANDAXE = weapon('handaxe','1d6')
JAVELIN = weapon('javelin','1d6')
LIGHTHAMMER = weapon('light hammer','1d4')
MACE = weapon('mace','1d6')
QUARTERSTAFF = weapon('quarterstaff','1d6')
SICKLE = weapon('sickle','1d4')
SPEAR = weapon('spear','1d6')
UNARMEDSTRIKE = weapon('unarmed strike','1')
LIGHTCROSSBOW = weapon('light crossbow','1d8',ranged=True)
DART = weapon('dart','1d4',finesse=True)
SHORTBOW = weapon('shortbow','1d6',ranged=True)
SLING = weapon('sling','1d4',ranged=True)
BATTLEAXE = weapon('battleaxe','1d8')
FLAIL = weapon('flail','1d8')
GLAIVE = weapon('glaive','1d10',twohanded=True)
GREATAXE = weapon('greataxe','1d12',twohanded=True)
GREATSWORD = weapon('greatsword','2d6',twohanded=True)
HALBERD = weapon('halberd','1d10',twohanded=True)
LANCE = weapon('lance','1d12')
LONGSWORD = weapon('longsword','1d8')
MAUL = weapon('maul','2d6',twohanded=True)
MORNINGSTAR = weapon('morningstar','1d8')
PIKE = weapon('pike','1d10',twohanded=True)
RAPIER = weapon('rapier','1d8',finesse=True)
SCIMITAR = weapon('scimitar','1d6',finesse=True)
SHORTSWORD = weapon('shortsword','1d6',finesse=True)
TRIDENT = weapon('trident','1d6')
WARPICK = weapon('war pick','1d8')
WARHAMMER = weapon('warhammer','1d8')
WHIP = weapon('whip','1d4',finesse=True)
BLOWGUN = weapon('blowgun','1',ranged=True)
HANDCROSSBOW = weapon('hand crossbow','1d6',ranged=True)
HEAVYCROSSBOW = weapon('heavy crossbow','1d10',ranged=True)
LONGBOW = weapon('longbow','1d8',ranged=True)
NET = weapon('net','-',ranged=True)
SIMPLE = weapon('simple weapons','')
MARTIAL = weapon('martial weapons','')

WEAPONS = [
    CLUB,             #0 Simple Weapons
    DAGGER,           #1
    GREATCLUB,        #2
    HANDAXE,          #3
    JAVELIN,          #4
    LIGHTHAMMER,     #5
    MACE,             #6
    QUARTERSTAFF,     #7
    SICKLE,           #8
    SPEAR,            #9
    UNARMEDSTRIKE,    #10
    LIGHTCROSSBOW,       #11 Simple Ranged
    DART,             #12
    SHORTBOW,         #13
    SLING,            #14
    BATTLEAXE,        #15 Martial Weapons
    FLAIL,            #16
    GLAIVE,           #17
    GREATAXE,         #18
    GREATSWORD,       #19
    HALBERD,          #20
    LANCE,            #21
    LONGSWORD,        #22
    MAUL,             #23
    MORNINGSTAR,      #24
    PIKE,             #25
    RAPIER,           #26
    SCIMITAR,         #27
    SHORTSWORD,       #28
    TRIDENT,          #29
    WARPICK,            #30
    WARHAMMER,          #31
    WHIP,               #32
    BLOWGUN,            #33 Martial Ranged
    HANDCROSSBOW,       #34
    HEAVYCROSSBOW,      #35
    LONGBOW,            #36
    NET,                #37
    SIMPLE,             #38 Categories
    MARTIAL,            #39
    ]

def finesse(strMod,dexMod):
    if strMod>dexMod:
        return strMod
    else:
        return dexMod

class Background:
    def __init__(self,
                 name = '',
                 skills = [[]],
                 otherProficiencies = [[]],
                 languages = [[]],
                 equipment = [[]],
                 features = [[]]
                 ):
        self.name=name
        self.skills=skills
        self.otherProficiencies = otherProficiencies
        self.languages = languages
        self.equipment = equipment
        self.features=features

ACOLYTE = Background(
    'Acolyte',
    [[SKILLSOPT[8],SKILLSOPT[10]]],
    languages = [LANGOPT,2],
    equipment = [['a holy symbol', 'a prayer book or prayer wheel',
                 '5 sticks of incense', 'vestements', 'a set of common clothes',
                 'a belt pouch containing 15gp']],
    features = [['Shelter of the Faithful']]
    )

class Races:
    def __init__(self,
                 name = '',
                 adjust=[0,0,0,0,0,0],
                 size='',
                 speed=0,
                 features=[[]],
                 languages=[[]],
                 physical=(0,0,0,0,0,0),
                 subs=[],
                 skills=[[]],
                 weaponProficiencies=[[]],
                 armorProficiencies=[[]],
                 otherProficiencies=[[]],
                 hp=0,
                 cantrips=[[]]
                 ):
        self.name=name
        self.adjust=adjust
        self.size=size
        self.speed=speed
        self.features=features
        self.languages=languages
        self.physical=physical
        self.subs=subs
        self.skills=skills
        self.weaponProficiencies=weaponProficiencies
        self.armorProficiencies=armorProficiencies
        self.otherProficiencies=otherProficiencies
        self.hp=hp
        self.cantrips=cantrips

HILLDWARF = Races(
    'Hill ',
    [0,0,0,0,1,0],
    features=[['Dwarven Toughness']],
    physical=(44,(2,4),115,(2,6),40,(3,14)),
    hp=1 #double check
    )
MOUNTAINDWARF = Races(
    'Mountain ',
    [2,0,0,0,0,0],
    features=[['Dwarven Armor Training']],
    physical=(48,(2,4),130,(2,6),40,(3,14)),
    armorProficiencies=[[LIGHT,MEDIUM]]
    )
DWARF = Races(
    'Dwarf',
    [0,0,2,0,0,0],
    'Medium',
    25,
    [['Darkvision','Dwarven Resilience','Dwarven Combat Training','Stonecunning'],None],
    [[LANGOPT[0],LANGOPT[1]]],
    subs=[HILLDWARF,MOUNTAINDWARF],
    weaponProficiencies=[[BATTLEAXE,HANDAXE,LIGHTHAMMER,WARHAMMER]],
    otherProficiencies=[[TOOLS[1],TOOLS[13],TOOLS[10]],1]
    )

class Classes:
    def __init__(self,
                 name='',
                 primary=(),
                 hp=0,
                 armorProficiencies=[[]],
                 weaponProficiencies=[[]],
                 otherProficiencies=[[]],
                 saves=[0,0,0,0,0,0],
                 saveNames = '',
                 skills = [[]],
                 equipment = [[]],
                 weapons = [],
                 armor = [],
                 features = [[]],
                 cantrips = [[]],
                 spells = [[]],
                 spellSlots = 0,
                 languages = [[]]
                 ):
        self.name = name
        self.primary = primary
        self.hp = hp
        self.weaponProficiencies = weaponProficiencies
        self.armorProficiencies = armorProficiencies
        self.otherProficiencies = otherProficiencies
        self.saves = saves
        self.saveNames = saveNames
        self.skills = skills
        self.equipment = equipment
        self.weapons = weapons
        self.armor = armor
        self.features = features
        self.cantrips = cantrips
        self.spells = spells
        self.spellSlots = spellSlots
        self.languages = languages

BARBARIAN = Classes(
    'Barbarian',
    (0,2),
    12,
    [[LIGHT,MEDIUM,SHIELDS]],
    [[SIMPLE,MARTIAL]],
    saves = [2,0,2,0,0,0],
    saveNames = 'Str, Con',
    skills = [[SKILLSOPT[0],SKILLSOPT[9],SKILLSOPT[7],SKILLSOPT[12],SKILLSOPT[13],
               SKILLSOPT[15]],2],
    equipment = [['an explorer\'s pack']],
    weapons = [JAVELIN],
    armor = [UNARMOREDBARB],
    features = [['Rage 2/day','Unarmored Defense']]
    )
options = [GREATAXE,WEAPONS[r.randint(15,32)]]
BARBARIAN.weapons.append(options[r.randint(0,len(options)-1)])
options = [HANDAXE,WEAPONS[r.randint(0,9)]]
BARBARIAN.weapons.append(options[r.randint(0,len(options)-1)])

BACKGROUNDLIST = [
    ACOLYTE
    ]

RACELIST = [
    DWARF
    ]

CLASSLIST = [
    BARBARIAN
    ]
