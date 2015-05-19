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

#index data about races and classes for method use later..

def rollX(numberOfDice, numberOfSides):
    #roll xd(whatever), return the result
    total = 0
    while numberOfDice > 0:
        i = r.randint(1,numberOfSides)
        total += i
        numberOfDice -= 1
    return total

class Races:
    def __init__(self):
        self.name = 'Race'
        self.adjust = [0,0,0,0,0,0]
        self.size = 'Size'
        self.speed = 'Speed'
        self.features = []
        self.languages = []
        self.subs = {}



HALFLING = {
    'name':'Halfling',
    'adjust':[0,2,0,0,0,0],
    'size':'Small',
    'speed':25,
    'features':['Lucky','Brave','Halfling Nimbleness'],
    'languages':[LANGOPT[0],LANGOPT[6]],
    'subs':[
        {
            'subname':'Lightfoot ',
            'adjust':[0,0,0,0,0,1],
            'features':['Naturally Stealthy'],
            'physical':[31, rollX(2,4), 35, 1, 20, rollX(2,12)]
            #[baseHeight,heightMod,baseWeight,weightMod,baseAge,ageMod]
            },
        {
            'subname':'Stout ',
            'adjust':[0,0,1,0,0,0],
            'features':['Stout Resilience'],
            'physical':[31, rollX(2,4), 35, 1, 20, rollX(2,12)]
            }
        ]
    }

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

def raceData(RACE):
    global Race
    global Subrace
    global Abilities
    global Age
    global Size
    global Height
    global Weight
    global Speed
    global Features
    global Languages

    Race = RACE['name']
    Size = RACE['size']
    Speed = RACE['speed']
    for i in RACE['adjust']:
        Abilities[i]+=i
    for i in RACE['features']:
        Features.add(i)
    for i in RACE['languages']:
        Languages.add(i)
    
        
    #for k,v in RACE[subs]:
    #Subrace = RACE[subs[r.randint(0,RACE[subs]-1)]]
    

##    HALFLING = {
##    name:'Halfling',
##    adjust:[0,2,0,0,0,0]
##    size:'Small',
##    speed:25,
##    features:['Lucky','Brave','Halfling Nimbleness'],
##    languages:[LANGOPT[0],LANGOPT[6]],
##    subs:{
##        'Lightfoot ':{
##            #or
##            #subname:'Lightfoot ',
##            adjust:[Abilities[5]+=1],
##            features:['Naturally Stealthy'],
##            physical:[31, rollX(2,4), 35, 1, 20, rollX(2,12)]
##            #[baseHeight,heightMod,baseWeight,weightMod,baseAge,ageMod]
##            }
##        'Stout ':{
##            adjust:[Abilities[2]+=1],
##            features:['Stout Resilience'],
##            physical:[31, rollX(2,4), 35, 1, 20, rollX(2,12)]
##            }
##        }
##    }



rollStats()
for i in range(6):
    print(Abilities[i])
Race = HALFLING
raceData(Race)
getMods()
print(Race)
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

