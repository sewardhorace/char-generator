import random as r
#to fix - number of weapons granted by classes (multiples of same weapon
# bard instrument proficiencies don't match instrument equipment gives

#random selections should be made as late as possible

#Huge index of items/other 'selectable' options
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

TRINKETS = [
    'a mummified goblin hand',
    'a piece of crystal that faintly glows in the moonlight',
    'a gold coin minted in an unknown land',
    'a diary written in a language you don\'t know',
    'a brass ring that never tarnishes',
    'an old chess piece made from glass',
    'a pair of knucklebone dice, each with a skull symbol on the side that would normally show six pips',
    'a small idol depicting a nightmarish creature that gives you unsettling dreams when you sleep near it',
    'a rope necklace from which dangle four mummified elf fingers',
    'the deed for a parcel of land in a realm unknown to you',
    'a 1-ounce block made from an unknown material',
    'a small cloth doll skewered with needles',
    'a tooth from an unknown beast',
    'an enormous scale, perhaps from a dragon',
    'a bright green feather',
    'an old divination card bearing your likeness',
    'a glass orb filled with moving smoke',
    'a 1-pound egg with a bright red shell',
    'a pipe that blows bubbles',
    'a glass jar containing a weird bit of flesh floating in pickling fluid',
    'a tiny gnome-crafted music box that plays a song you dimly remember from your childhood',
    'a small wooden statuette of a smug halfling',
    'a brass orb etched with strange runes',
    'a multicolored stone disk',
    'a tiny silver icon of a raven',
    'a bag containing forty-seven humanoid teeth, one of which is rotten',
    'a shard of obsidian that always feels warm to the touch',
    'a dragon\'s bony talon hanging from a plain leather necklace',
    'a pair of old socks',
    'a blank book whose pages refuse to hold ink, chalk, graphite, or any other substance or marking',
    'a silver badge in the shape of a five-pointed star',
    'a knife that belonged to a relative',
    'a glass vial filled with nail clippings',
    'a rectangular metal device with two tiny metal cups on one end that throws sparks when wet',
    'a white, sequined glove sized for a human',
    'a vest with one hundred tiny pockets',
    'a small, weightless stone block',
    'a tiny sketch portrait of a goblin',
    'an empty glass vial that smells of perfume when opened',
    'a gemstone that looks like a lump of coal when examined by anyone but you',
    'a scrap of cloth from an old banner',
    'a rank insignia from a lost legionnaire',
    'a tiny silver bell without a clapper',
    'a mechanical canary inside a gnomish lamp',
    'a tiny chest carved to look like it has numerous feet on the bottom',
    'a dead sprite inside a clear glass bottle',
    'a metal can that has no opening but sounds as if it is filled with liquid, sand, spiders, or broken glass (your choice)',
    'a glass orb filled with water, in which swims a clockwork goldfish',
    'a silver spoon with an M engraved on the handle',
    'a whistle made from gold-colored wood',
    'a dead scarab beetle the size of your hand',
    'two toy soldiers, one with a missing head',
    'a small box filled with different-sized buttons',
    'a candle that can\'t be lit',
    'a tiny cage with no door',
    'an old key',
    'an indecipherable treasure map',
    'a hilt from a broken sword',
    'a rabbit\'s foot',
    'a glass eye',
    'a cameo carved in the likeness of a hideous person',
    'a silver skull the size of a coin',
    'an alabaster mask',
    'a pyramid of sticky black incense that smells very bad',
    'a nightcap that, when worn, gives you pleasant dreams',
    'a single caltrop made from bone',
    'a gold monocle frame without the lens',
    'a 1-inch cube, each side painted a different color',
    'a crystal knob from a door',
    'a small packet filled with pink dust',
    'a fragment of a beautiful song, written as musical notes on two pieces of parchment',
    'a silver teardrop earring made from a real teardrop',
    'the shell of an egg painted with scenes of human misery in disturbing detail',
    'a fan that, when unfolded, shows a sleeping cat',
    'a set of bone pipes',
    'a four-leaf clover pressed inside a book discussing manners and etiquette',
    'a sheet of parchment upon which is drawn a complex mechanical contraption',
    'an ornate scabbard that fits no blade you have found so far',
    'an invitation to a party where a murder happened',
    'a bronze pentacle with an etching of a rat\'s head in its center',
    'a purple handkerchief embroidered with the name of a powerful archmage',
    'half of a floorplan for a temple, castle, or some other structure',
    'a bit of folded cloth that, when unfolded, turns into a stylish cap',
    'a receipt of deposit at a bank in a far-flung city',
    'a diary with seven missing pages',
    'an empty silver snuffbox bearing an inscription on the surface that says "dreams"',
    'an iron holy symbol devoted to an unknown god',
    'a book that tells the story of a legendary hero\'s rise and fall, with the last chapter missing',
    'a vial of dragon blood',
    'an ancient arrow of elven design',
    'a needle that never bends',
    'an ornate brooch of dwarven design',
    'an empty wine bottle bearing a pretty label that says, "The Wizard of Wines Winery, Red Dragon Crush, 331422-W"',
    'a mosaic tile with a multicolored, glazed surface',
    'a petrified mouse',
    'a black pirate flag adorned with a dragon\'s skull and crossbones',
    'a tiny mechanical crab or spider that moves about when it is not being observed',
    'a glass jar containing lard with a label that reads, "Griffon Grease"',
    'a wooden box with a ceramic bottom that holds a living worm with a head on each end of its body',
    'a metal urn containing the ashes of a hero'
    ]

#class spell lists
BAR = {
    0:[
        'Blade Ward',
        'Dancing Lights',
        'Friends',
        'Light',
        'Mage Hand',
        'Mending',
        'Message',
        'Minor Illusion',
        'Prestidigitation',
        'True Strike',
        'Vicious Mockery'
        ],
    1:[
        'Animal Friendship',
        'Bane',
        'Charm Person',
        'Comprehend Languages',
        'Cure Wounds',
        'Detect Magic',
        'Disguise Self',
        'Dissonant Whispers',
        'Faerie Fire',
        'Feather Fall',
        'Healing Word',
        'Heroism',
        'Identify',
        'Illusory Script',
        'Longstrider',
        'Silent Image',
        'Sleep',
        'Speak with Animals',
        'Tasha\'s Hideous Laughter',
        'Thunderwave',
        'Unseen Servant'
        ]
    }
CLER = {
    0:[
        'Guidance',         #0
        'Light',            #1
        'Mending',          #2
        'Resistance',       #3
        'Sacred Flame',     #4
        'Spare the Dying',  #5
        'Thaumaturgy',      #6
        ],
    1:[
        'Bane',                             
        'Bless',                            
        'Command',                          
        'Create or Destroy Water',
        'Cure Wounds',
        'Detect Evil and Good',
        'Detect Magic',
        'Detect Poison and Disease',
        'Guiding Bolt',
        'Healing Word',
        'Inflict Wounds',
        'Protection from Good and Evil',
        'Purify Food and Drink',
        'Sanctuary',
        'Shield of Faith'
        ]
    }
DRU = {
    0:[
        'Druidcraft',
        'Guidance',
        'Mending',
        'Poison Spray',
        'Produce Flame',
        'Resistance',
        'Shillelagh',
        'Thorn Whip',
       ],
    1:[
        'Animal Friendship',
        'Charm Person',
        'Create or Destroy Water',
        'Cure Wounds',
        'Detect Magic',
        'Detect Poison and Disease',
        'Entangle',
        'Faerie Fire',
        'Fog Cloud',
        'Goodberry',
        'Healing Word',
        'Jump',
        'Longstrider',
        'Purify Food and Drink',
        'Speak with Animals',
        'Thunderwave',
        ]
    }
PAL = {
    1:[
        ]
    }
RANG = {
    1:[
        ]
    }
SOR = {
    0:[
        'Acid Splash',
        'Blade Ward',
        'Chill Touch',
        'Dancing Lights',
        'Fire Bolt',
        'Friends',
        'Light',
        'Mage Hand',
        'Mending',
        'Message',
        'Minor Illusion',
        'Poison Spray',
        'Prestidigitation',
        'Ray of Frost',
        'Shocking Grasp',
        'True Strike'
        ],
    1:[
        'Burning Hands',
        'Charm Person',
        'Chromatic Orb',
        'Color Spray',
        'Comprehend Languages',
        'Detect Magic',
        'Disguise Self',
        'Expeditious Retreat',
        'False Life',
        'Feather Fall',
        'Fog Cloud',
        'Jump',
        'Mage Armor',
        'Magic Missile',
        'Ray of Sickness',
        'Shield',
        'Silent Image',
        'Sleep',
        'Thunderwave',
        'Witch Bolt'       
        ]
    }
WAR = {
    0:[
        'Blade Ward',
        'Chill Touch',
        'Eldritch Blast',
        'Friends',
        'Mage Hand',
        'Minor Illusion',
        'Poison Spray',
        'Prestidigitation',
        'True Strike'
        ],
    1:[
        'Armor of Agathys',
        'Arms of Hadar',
        'Charm Person',
        'Comprehend Languages',
        'Expeditious Retreat',
        'Hellish Rebuke',
        'Hex',
        'Illusory Script',
        'Protection from Good and Evil',
        'Unseen Servant',
        'Witch Bolt'
        ]
    }
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

def rollX(numberOfDice=1, numberOfSides=6):
    #roll xd(whatever), return the result
    total = 0
    while numberOfDice > 0:
        i = r.randint(1,numberOfSides)
        total += i
        numberOfDice -= 1
    return total

def randAbility(numberOfScores, amtOfIncrease, preadjust=[0,0,0,0,0,0]):
    Abilities = preadjust
    while numberOfScores > 0:
        i = r.randint(0,5)
        if Abilities[i] == 0:
            Abilities[i]+=amtOfIncrease
            numberOfScores-=1
    return Abilities
        
def randSelect(options, amount, destinationSet): #convert this to make it useful
    #for current model, able to add items to a set one at a time
    #or a separate function to add one at a time

    #adds an amount of options chosen at random to a destination set
    #for spells, indicate spell level in options and destination
    #ex. (Wiz[0],amount,SpellList[0])
    i = len(destinationSet)
    while len(destinationSet)<i+amount:
        j = options[r.randint(0,len(options)-1)]
        if j not in destinationSet:
            destinationSet.add(j)

def randOption(options,amount=1): #how to return multiple values, unpacked?
    while amount > 0 and len(options) > 0:
        new = options.pop(r.randint(0,len(options)-1))
        amount -= 1
        return new
    #return new

def select(destinationSet,contentList,amount=None):
    i = len(destinationSet)
    if amount == None:
        amount = len(contentList)
    
    while len(destinationSet)<i+amount:
        if len(contentList)>0:
            destinationSet.add(contentList.pop(r.randint(0,len(contentList)-1)))
        else:
            amount-=1
            
def selectList(destinationSet,contentList,amount=None): #not even using??
    i = len(destinationSet)
    if amount == None:
        amount = len(contentList)
    while len(destinationSet)<i+amount:
        if len(contentList)>0:
            destinationSet.append(contentList.pop(r.randint(0,len(contentList)-1)))
        else:
            amount-=1

def inBoth(firstList,secondList,amount=1): #how to return multiple values, unpacked?
    firstSet = set(firstList)
    secondSet = set(secondList)
    both = list(firstSet.intersection(secondSet))
    while amount > 0 and len(both)>0:
        result = both.pop(r.randint(0,len(both)-1))
        amount-=1
        return result
    
#index data about backgrounds, races, and classes for method use later..
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

URCHIN = Background(
    'Urchin',
    [[SKILLSOPT[2],SKILLSOPT[3]]],
    [[TOOLS[22],TOOLS[25]]],
    equipment = [['a small knife','a map of the city you grew up in','a pet mouse',
                  'a token to remember your parents by','a set of common clothes','a belt pouch containing 10gp']],
    features = [['City Secrets']]
    )

SOLDIER = Background(
    'Soldier',
    [[SKILLSOPT[0],SKILLSOPT[15]]],
    [[TOOLS[27],randOption(TOOLS[17:21])]],
    equipment = [['an insignia of rank','a trophy taken from a fallen enemy: '+randOption(['a dagger','broken blade','piece of a banner']),
                  'a set of common clothes','a belt pouch containing 10gp']],
    features = [['Military Rank','Specialty: '+randOption(['Officer','Scout','Infantry','Cavalry',
                                                'Healer','Quartermaster','Standard bearer','Support staff (cook, blacksmith, or the like)'])]]
    )
if TOOLS[17] in SOLDIER.otherProficiencies[0]:
    SOLDIER.equipment[0].append('a set of bone dice')
else:
    SOLDIER.equipment[0].append('a deck of cards')


SAILOR = Background(
    skills = [[SKILLSOPT[0],SKILLSOPT[12]]],
    otherProficiencies = [[TOOLS[26],TOOLS[28]]],
    equipment = [['a belaying pin (club)','50 feet of silk rope',
                  'a lucky charm such as a rabbit foot or a small stone with a hole in the center (or random trinket)',
                  'a set of common clothes','a belt pouch containing 10gp']],
    features = [[]] #all classes without this share features assigne later for some reason...
    )
SAILOR.name = randOption(['Sailor','Variant Sailor: Pirate'])
if SAILOR.name == 'Sailor':
    SAILOR.features[0].append('Ship\'s Passage')
else:
    SAILOR.features[0].append(randOption(['Ship\'s Passage','Variant Feature: Bad Reputation']))

SAGE = Background(
    'Sage',
    [[SKILLSOPT[4],SKILLSOPT[5]]],
    languages = [LANGOPT,2],
    equipment = [['a bottle of black ink','a quill','a small knife',
                  'a letter from a dead colleague posing a question you have not yet been able to answer',
                  'a set of common clothes','a belt pouch containing 10gp']],
    features = [['Researcher','Specialty: '+randOption(['Alchemist','Astronomer','Discredited academic',
                                                        'Librarian','Professor','Researcher','Wizard\'s apprentice',
                                                        'Scribe'])]]
    )

OUTLANDER = Background(
    'Outlander',
    [[SKILLSOPT[0],SKILLSOPT[13]]],
    [[randOption(TOOLS[29:])]],
    [LANGOPT,1],
    [['a staff','a hunting trap','a trophy from an animal you killed',
      'a set of traveler\'s clothes','a belt pouch containing 10gp']],
    [['Wanderer','Origin: '+randOption(['Forester','Trapper','Homesteader','Guide',
                             'Exile or outcast','Bounty hunter','Pilgrim',
                             'Tribal nomad','Hunter-gatherer','Tribal marauder'])]]
    )

NOBLE = Background(
    skills = [[SKILLSOPT[5],SKILLSOPT[17]]],
    otherProficiencies = [[randOption(TOOLS[17:21])]],
    languages = [LANGOPT,1],
    equipment = [['a set of fine clothes','a signet ring','a scroll of pedigree','a purse containing 25gp']],
    features = [[]] #must be here, or else features mix...
    )
NOBLE.name = randOption(['Noble','Variant Noble: Knight'])
if NOBLE.name == 'Variant Noble: Knight':
    NOBLE.features[0].append('Variant Feature: Retainers')
    NOBLE.equipment[0].append('a banner or other token from a noble lord or lady to whom you have given your heart')
else:
    NOBLE.features[0].append(randOption(['Variant Feature: Retainers','Position of Privilege']))

HERMIT = Background(
    'Hermit',
    [[SKILLSOPT[11],SKILLSOPT[8]]],
    [[TOOLS[21]]],
    [LANGOPT,1],
    [['a scroll case stuffed full of notes from your studies or prayers',
      'a winter blanket','a set of common clothes','an herbalism kit','5gp']],
    [['Discovery','Life of Seclusion: '+randOption(['I was searching for spiritual enlightenment',
                              'I was partaking of communal living in accordance wit the dictates of a religious order',
                              'I was exiled for a crime I didn\'t commit',
                              'I retreated from society after a life-altering event',
                              'I needed a quiet place to work on my art, literature, music, or manifesto',
                              'I needed to commune with nature, far from civilization',
                              'I was the caretaker of an ancient rune or relic',
                              'I was a pilgrim in search of a perso, place, or relic of spiritual significance'])]]
    )

GUILDARTISAN = Background(
    'Guild Artisan',
    [[SKILLSOPT[10],SKILLSOPT[17]]],
    [[]],
    [LANGOPT,1],
    [['a letter of introduction from your guild','a set of traveler\'s clothes',
      'a belt pouch containing 15gp']],
    [[]] # must be here or features will mix...
    )
options = [('Alchemists and apothecaries',TOOLS[0]),
           ('Armorers, locksmiths, and finesmiths',TOOLS[13]),
           ('Brewers, distillers, and vintners',TOOLS[1]),
           ('Calligraphers, scribes, and scriveners',TOOLS[2]),
           ('Carpenters, roofers, and plasterers',TOOLS[3]),
           ('Cartographers, surveyors, and chart-makers',TOOLS[4]),
           ('Cobblers and shoemakers',TOOLS[5]),
           ('Cooks and bakers',TOOLS[6]),
           ('Glassblowers and glaziers',TOOLS[7]),
           ('Jewelers and gemcutters',TOOLS[8]),
           ('Leatherworkers, skinners, and tanners',TOOLS[9]),
           ('Masons and stonecutters',TOOLS[10]),
           ('Painters, limners, and sign-makers',TOOLS[11]),
           ('Potters and tile-makers',TOOLS[12]),
           ('Shipwrights and sailmakers',TOOLS[3]),
           ('Smiths and metal-forgers',TOOLS[13]),
           ('Tinkers, pewterers, and casters',TOOLS[14]),
           ('Wagon-makers and wheelwrights',TOOLS[3]),
           ('Weavers and dyers',TOOLS[15]),
           ('Woodcarvers, coopers, and bowyers',TOOLS[16])]
choice = randOption(options)
GUILDARTISAN.otherProficiencies[0].append(choice[1])
GUILDARTISAN.equipment[0].append(choice[1])
GUILDARTISAN.features[0].append('Guild Membership: '+choice[0])


FOLKHERO = Background(
    'Folk Hero',
    [[SKILLSOPT[9],SKILLSOPT[13]]],
    [['Vehicles (land)',randOption(TOOLS[:17])]],
    equipment = [['a shovel','an iron pot','a set of common clothes',
                  'a belt pouch containing 15gp']],
    features = [['Rustic Hospitality','Defining Event: '+randOption(
        ['I stood up to a tyrant\'s agents','I saved people during a natural disaster',
         'I stood alone against a terrible monster','I stole from a corrupt merchant to help the poor',
         'I led a militia to fight off an invading army','I broke into a tyrant\'s castle and stole weapons to arm the people',
         'I trained the peasantry to use farm implements as weapons against a tyrant\'s soldiers',
         'A lord rescinded an unpopular decree after I led a symbolic act of protest against it',
         'A celestial, fey, or similar creature gave me a blessing or revealed my secret origin',
         'Recruited to a lord\'s army, I rose to leadership and was commended for my heroism'])]]
    )
FOLKHERO.equipment[0].append(inBoth(FOLKHERO.otherProficiencies[0],TOOLS[:17]))

ENTERTAINER = Background(
    'Entertainer',
    [[SKILLSOPT[1],SKILLSOPT[16]]],
    [[TOOLS[22],randOption(TOOLS[29:])]],
    equipment = [['a costume','a belt pouch containing 15gp','the favor of an admirer: '+randOption(
                      ['love letter', 'lock of hair', 'trinket'])]],
    features = [['By Popular Demand','Routine: '+randOption(['Actor',
            'Dancer','Fire-eater','Jester','Juggler','Instrumentalist',
           'Poet','Singer','Storyteller','Tumbler'])]] #fix so there are 3 routines
    )
ENTERTAINER.equipment[0].append(inBoth(ENTERTAINER.otherProficiencies[0],TOOLS[29:]))

ACOLYTE = Background(
    'Acolyte',
    [[SKILLSOPT[8],SKILLSOPT[10]]],
    languages = [LANGOPT,2],
    equipment = [['a holy symbol', 'a prayer book or prayer wheel',
                 '5 sticks of incense', 'vestements', 'a set of common clothes',
                 'a belt pouch containing 15gp']],
    features = [['Shelter of the Faithful']]
    )

CHARLATAN = Background(
    'Charlatan',
    [[SKILLSOPT[2],SKILLSOPT[14]]],
    [[TOOLS[22],TOOLS[23]]],
    equipment = [['a set of fine clothes', 'disguise kit',
                  'a belt pouch containing 15gp']],
    features =[['False Identity']]
    )
options = ['ten stoppered bottles filled with colored liquid',
           'a set of weighted dice', 'a deck of marked cards',
           'a signet ring of an imaginary duke']
CHARLATAN.equipment[0].append(options[r.randint(0,len(options)-1)])

CRIMINAL = Background(
    'Criminal',
    [[SKILLSOPT[3],SKILLSOPT[14]]],
    [[TOOLS[25],TOOLS[r.randint(17,20)]]],
    equipment = [['a crowbar',
                   'a set of dark common clothes including a hood',
                   'a belt pouch containing 15gp']],
    features = [['Criminal Contact']]
    )

BACKGROUNDLIST = [
    ACOLYTE,
    CHARLATAN,
    CRIMINAL,
    ENTERTAINER,
    FOLKHERO,
    GUILDARTISAN,
    HERMIT,
    NOBLE,
    OUTLANDER,
    SAGE,
    SAILOR,
    SOLDIER,
    URCHIN
    ]

#which features are part of all races?  which are for subraces only? both?
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

NOSUB = Races()

HILLDWARF = Races(
    'Hill ',
    [0,0,0,0,1,0],
    features=[['Dwarven Toughness']],
    physical=(44,rollX(2,4),115,rollX(2,6),40,rollX(3,14)),#make a tuple?
    hp=1
    )
MOUNTAINDWARF = Races(
    'Mountain ',
    [2,0,0,0,0,0],
    features=[['Dwarven Armor Training']],
    physical=(48,rollX(2,4),130,rollX(2,6),40,rollX(3,14)),
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

HIGHELF = Races(
    'High ',
    [0,0,0,1,0,0],
    features=[['Darkvision','Elf Weapon Training','Cantrip']],
    languages=[LANGOPT,1],
    physical=[54,rollX(2,10),90, rollX(1,4),110,rollX(4,15)],
    weaponProficiencies=[[LONGSWORD,SHORTSWORD,SHORTBOW,LONGBOW]],
    cantrips=[WIZ[0],1]
    )
WOODELF = Races(
    'Wood ',
    [0,0,0,0,1,0],
    speed=5,
    features=[['Darkvision','Elf Weapon Training','Fleet of Foot',
               'Mask of the Wild']],
    physical=[54,rollX(2,10),100, rollX(1,4),110,rollX(4,15)],
    weaponProficiencies=[[LONGSWORD,SHORTSWORD,SHORTBOW,LONGBOW]]
    )
DARKELF = Races(
    'Dark ',
    [0,0,0,0,0,1],
    features=[['Superior Darkvision','Sunlight Sensitivity','Drow Magic']],
    physical=[53,rollX(2,6),75, rollX(1,6),110,rollX(4,15)],
    weaponProficiencies=[[RAPIER,SHORTSWORD,HANDCROSSBOW]],
    cantrips=[[WIZ[0][3]]]
    )
ELF = Races(
    'Elf',
    [0,2,0,0,0,0],
    'Medium',
    30,
    [['Keen Senses','Fey Ancestry','Trance']],
    [[LANGOPT[0],LANGOPT[2]]],
    skills=[[SKILLSOPT[12]]],
    subs=[HIGHELF,WOODELF,DARKELF]
    )
    
LIGHTFOOTHALFLING = Races(
    'Lightfoot ',
    [0,0,0,0,0,1],
    features=[['Naturally Stealthy']]
    )
STOUTHALFLING = Races(
    'Stout ',
    [0,0,1,0,0,0],
    features=[['Stout Resilience']]
    )
HALFLING = Races(
    'Halfling',
    [0,2,0,0,0,0],
    'Small',
    25,
    [['Lucky','Brave','Halfling Nimbleness']],
    [[LANGOPT[0],LANGOPT[6]]],
    [31, rollX(2,4), 35, 1, 20, rollX(2,12)],#double check physical for subs
    [LIGHTFOOTHALFLING,STOUTHALFLING],#how to do these...?
    )

STANDARDHUMAN = Races(
    adjust=[1,1,1,1,1,1],
    languages = [[LANGOPT[0],randOption(LANGOPT[1:])]],
    )
VARIANTHUMAN = Races(
    'Variant ',
    randAbility(2,1),
    features=[['Choose 1 Feat'],None],
    skills=[SKILLSOPT,1]
    )
HUMAN = Races(
    'Human',
    size='Medium',
    speed=25,
    physical=(56, rollX(2,10), 110, rollX(2,4), 15, rollX(1,12)),
    subs=[STANDARDHUMAN,VARIANTHUMAN]
    )

DRAGONBORN = Races(
    'Dragonborn',
    [2,0,0,0,0,1],
    'Medium',
    30,
    [[]],
    [[LANGOPT[0],LANGOPT[10]]],
    (66,rollX(2,8),175,rollX(2,6),14,rollX(2,5))
    )
options = [('Black','Acid'),
            ('Blue','Lightning'),
            ('Brass','Fire'),
            ('Bronze','Lightning'),
            ('Copper','Acid'),
            ('Gold','Fire'),
            ('Green','Poison'),
            ('Red','Fire'),
            ('Silver','Cold'),
            ('White','Cold')]
i = r.randint(0,len(options)-1)
DRAGONBORN.features[0].append('Draconic Ancestry: '+options[i][0])
DRAGONBORN.features[0].append('Damage Resistance: '+options[i][1])
if i < 5:
    DRAGONBORN.features[0].append('Breath Weapon: '+options[i][1]+' 5x30ft. line (Dex save)')
else:
    DRAGONBORN.features[0].append('Breath Weapon: '+options[i][1]+' 15ft. cone (Con save)')
    
FORESTGNOME = Races(
    'Forest ',
    [0,1,0,0,0,0],
    features = [['Natural Illusionist','Speak with Small Beasts']],
    cantrips = [[WIZ[0][10]]]
    )
ROCKGNOME = Races(
    'Rock ',
    [0,0,1,0,0,0],
    features = [['Artificer\'s Lore','Tinker']],
    otherProficiencies = [[TOOLS[14]]]
    )
GNOME = Races(
    'Gnome',
    [0,0,0,2,0,0],
    'Small',
    25,
    [['Darkvision','Gnome Cunning']],
    [[LANGOPT[0],LANGOPT[4]]],
    (35,rollX(2,4),35,1,40,rollX(4,13)),
    subs = [FORESTGNOME,ROCKGNOME]
    )

HALFELF = Races(
    'Half Elf',
    randAbility(2,1,[0,0,0,0,0,2]),
    'Medium',
    30,
    [['Darkvision','Fey Ancestry','Skill Versatility']],
    [[LANGOPT[0],LANGOPT[2]]],
    (57,rollX(2,8),110,rollX(2,4),20,rollX(1,18)),
    skills=[SKILLSOPT,2],
    )
options = LANGOPT[3:]
options.append(LANGOPT[1])
HALFELF.languages[0].append(options[r.randint(0,len(options)-1)])

HALFORC = Races(
    'Half Orc',
    [2,1,0,0,0,0],
    'Medium',
    30,
    [['Darkvision','Menacing','Relentless Endurance','Savage Attacks']],
    [[LANGOPT[0],LANGOPT[7]]],
    (58,rollX(2,10),140,rollX(2,6),14,rollX(1,12)),
    skills = [[SKILLSOPT[15]]]
    )

TIEFLING = Races(
    'Tiefling',
    [0,0,0,1,0,2],
    'Medium',
    30,
    [['Darkvision','Hellish Resistance','Infernal Legacy']],
    [[LANGOPT[0],LANGOPT[12]]],
    (57,rollX(2,8),110,rollX(2,4),15,rollX(1,12)),
    cantrips=[[CLER[0][6]]]
    )

RACELIST = [
            DWARF,
            ELF,
            HALFLING,
            HUMAN,
            DRAGONBORN,
            GNOME,
            HALFELF,
            HALFORC,
            TIEFLING    
            ]

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

CLERIC = Classes(
    'Cleric',
    (4,2),
    8,
    [[LIGHT,MEDIUM,SHIELDS]],
    [[SIMPLE]],
    saves = [0,0,0,0,2,2],
    saveNames = 'Wis, Cha',
    skills = [[SKILLSOPT[5],SKILLSOPT[10],SKILLSOPT[11],SKILLSOPT[17],SKILLSOPT[8]],2],
    equipment = [['a shield','a holy symbol',randOption(['a priest\'s pack','an explorer\'s pack'])]],
    weapons = [],
    armor = [],
    features = [['Spellcasting','Ritual Casting']]
    )

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

BARD = Classes(
    'Bard',
    (5,1),
    hp=8,
    weaponProficiencies=[[WEAPONS[38],WEAPONS[34],WEAPONS[22],WEAPONS[26],
                          WEAPONS[28]]],
    armorProficiencies=[[LIGHT]],
    otherProficiencies=[TOOLS[29:],2],#how to get proficiencies and equipment matched?
    saves=[0,2,0,0,0,2],
    saveNames='Dex, Cha',
    skills=[SKILLSOPT,3],
    equipment=[[randOption(['diplomat\'s pack','entertainer\'s pack'])]],
    weapons=[WEAPONS[1]],
    armor=[ARMOR[1]],
    features=[['Spellcasting (Ritual Casting)', 'Bardic Inspiration (1d6)']],
    cantrips=[BAR[0],2],
    spells=[BAR[1],4]
    )
options = [WEAPONS[22],WEAPONS[26],WEAPONS[r.randint(0,14)]]
BARD.weapons.append(options[r.randint(0,len(options)-1)])
option = randOption(TOOLS[29:])
BARD.otherProficiencies[0].append(option)
BARD.equipment[0].append(option)
#need two more instrument proficiencies

CLASSLIST = [
    BARBARIAN,
    BARD
    ]

def rollFour():
    #roll 4d6, remove the lowest roll(uniquely for ability scores)
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
    Abilities = []
    for i in range(6):
        Abilities.append(rollFour())
    return Abilities

def getMods(Abilities):
    Mods = []
    for i in range(6):
        Mods.append((Abilities[i]//2)-5)
    return Mods

def randPhys(baseHeightInches, heightMod, baseWeight, weightMod, baseAge, ageMod):
    #random height and weight and starting age
    #(use rollX(x,y) for mods in race object definitions)
    height = baseHeightInches+heightMod
    height = str(height//12)+'\''+str(height%12)+'\"'
    weight = baseWeight+(weightMod*heightMod)
    age = baseAge+ageMod
    physical = [height,str(weight)+' lbs.',str(age)+' years']
    return physical

def choose(group):
    choice = group[r.randint(0,len(group)-1)]
    return choice

def optimize(abilities,primary):
    abilities.sort()
    temp = [0,0,0,0,0,0]
    temp[primary[0]] = abilities.pop()
    temp[primary[1]] = abilities.pop()
    for i in range(6):
        if temp[i] == 0:
            temp[i]+=abilities.pop(r.randint(0,len(abilities)-1))
    return temp
    
def printAll(Abilities, Background, Race, Class):
    if len(Race.subs)>0:
        Sub = Race.subs[r.randint(0,len(Race.subs)-1)]
        Race.name = Sub.name+Race.name
    else:Sub = NOSUB
    Abilities = optimize(Abilities,Class.primary)
    for i in range(6):
        Abilities[i]+=Race.adjust[i]+Sub.adjust[i]
    features = set()
    select(features,*Background.features)
    select(features,*Race.features)
    select(features,*Sub.features)
    select(features,*Class.features)
    languages = set()
    select(languages,*Race.languages)
    select(languages,*Sub.languages)
    select(languages,*Background.languages)
    select(languages,*Class.languages)
    physical = randPhys(*Race.physical)
    if physical == ['0\'0"', '0 lbs.', '0 years']:
            physical = randPhys(*Sub.physical)
    skills = set()
    select(skills,*Background.skills)
    select(skills,*Race.skills)
    select(skills,*Sub.skills)
    select(skills,*Class.skills)
    weaponProficiencies = set()
    select(weaponProficiencies,*Race.weaponProficiencies)
    select(weaponProficiencies,*Sub.weaponProficiencies)
    select(weaponProficiencies,*Class.weaponProficiencies)
    armorProficiencies = set()
    select(armorProficiencies,*Race.armorProficiencies)
    select(armorProficiencies,*Sub.armorProficiencies)
    select(armorProficiencies,*Class.armorProficiencies)
    otherProficiencies = set()
    select(otherProficiencies,*Race.otherProficiencies)
    select(otherProficiencies,*Sub.otherProficiencies)
    select(otherProficiencies,*Background.otherProficiencies)
    select(otherProficiencies,*Class.otherProficiencies)
    equipment = set()
    select(equipment,*Background.equipment)
    select(equipment,*Class.equipment)
    spellList = {0:set(),1:set()}
    select(spellList[0],*Race.cantrips)
    select(spellList[0],*Sub.cantrips)
    select(spellList[0],*Class.cantrips)
    select(spellList[1],*Class.spells)
    mods = getMods(Abilities)
    hp = Race.hp + Sub.hp + Class.hp + mods[2]
    saves = Class.saves
    for i in range(6):
        Class.saves[i]+=mods[i]
    ac = 10
    if Class.armor == []:
        ac+=mods[1]
    else:
        for i in Class.armor:
            acbonus = mods[1]
            if i.weight == 0:
                ac+=i.ac+acbonus
            elif i.weight == 1:
                if acbonus>2:
                    acbonus=2
                ac+=i.ac+acbonus
            elif i.weight == 2:
                ac+=i.ac
            if i.special == 'Barbarian':
                ac+=mods[2]
            elif i.special == 'Monk':
                ac+=mods[4]
    print('%s %s (%s)' % (Race.name,Class.name,Background.name))
    print('HP = %d AC = %d' % (hp,ac))
    print('Abilities (Mod) - Save')
    for i in range(6):
        abName = ['Str','Dex','Con','Int','Wis','Cha']
        print('%s= %d (%d) - %d' % (abName[i],Abilities[i],mods[i], saves[i]))
    print('Saves= '+Class.saveNames)
    print('Attack= ')
    for i in Class.weapons:
        if i.ranged:
            j=mods[1]
        elif i.finesse:
            j=finesse(mods[0],mods[1])
        else:
            j=mods[0]
        k = i.damage+'+'+str(j)
        print('   %s +%d atk, %s dmg' % (i.name,j+2,k))
    print('Armor= ', end='')
    for i in Class.armor:
        print(i.name, end=', ')
    print('\nSize= %s, Speed= %d' % (Race.size,Race.speed+Sub.speed))
    print('Height= %s Weight= %s Age= %s' % (physical[0],physical[1],physical[2]))
    print('Features=', end=' ')
    for i in features:
        print(i, end=', ')
    print('\nSkills=', end=' ')
    for i in skills:
        print(i, end=', ')
    print('\nWeapon Proficiencies=', end=' ')
    for i in weaponProficiencies:
        print(i.name, end=', ')
    print('\nArmor Proficiencies=', end=' ')
    for i in armorProficiencies:
        print(i.name, end=', ')
    print('\nOther Proficiencies=', end=' ')
    for i in otherProficiencies:
        print(i, end=', ')
    print('\nLanguages=', end=' ')
    for i in languages:
        print(i, end=', ')
    print('\nEquipment=', end=' ')
    for i in equipment:
        print(i, end=', ')
    print('\nSpells:\nLevel 0=', end=' ')
    for i in spellList[0]:
        print(i, end=', ')
    print('\nLevel 1=', end=' ')
    for i in spellList[1]:
        print(i, end=', ')
                                        
printAll(rollStats(), choose(BACKGROUNDLIST), choose(RACELIST), choose(CLASSLIST))
