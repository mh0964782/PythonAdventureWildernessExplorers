#This is your starter file for the Final Project
#The lines that start with a # are comments and will not show up in your code
#You should utilize this feature to leave notes about what variables are for
#And what operations your code is performing

#Try to have your program be inutitive for the user to interact with
import random
import os
import copy
import time
import matplotlib.pyplot as plt

#creature class for both players and monsters
class Creature:
    def __init__(self, typ, name, HP, ATK, DEF, MAG, RES, SPE, LVL, base, actions):
        self.typ = typ
        self.name = name
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.MAG = MAG
        self.RES = RES
        self.SPE = SPE
        self.LVL = LVL
        # When creating monsters with the class, it levels up for every integer past 1 its LVL is at. (EX: levels up twice for a LVL of 3).
        if self.LVL > 1 and self.typ == 'monster':
            for i in range(self.LVL-1):
                self.LevelUp()
        self.base = base
        self.actions = actions
        
        self.WeaponBuff() #apply weapon buff
        
    def WeaponBuff(self): #functin to apply weapon buff
        if self.base.buff == 'ATK':
            self.ATK += 10
        elif self.base.buff == 'DEF':
            self.DEF += 10
        elif self.base.buff == 'MAG':
            self.MAG += 10
        elif self.base.buff == 'RES':
            self.RES += 10
        elif self.base.buff == 'SPE':
            self.SPE += 10
            
    def RemoveWeaponBuff(self, buff): #function to take away weapon buff when switched weapon
        if buff == 'ATK':
            self.ATK -= 10
        elif buff == 'DEF':
            self.DEF -= 10
        elif buff == 'MAG':
            self.MAG -= 10
        elif buff == 'RES':
            self.RES -= 10
        elif buff == 'SPE':
            self.SPE -= 10
        
    def LevelUp(self):
        self.Level('HP', self.HP)
        self.Level('ATK', self.ATK)
        self.Level('DEF', self.DEF)
        self.Level('MAG', self.MAG)
        self.Level('RES', self.RES)
        self.Level('SPE', self.SPE)
        if self.typ == 'player':
            for action in self.actions:
                action.amt = action.amtMax
            print('Actions Replenished!')
            input('enter to continue ')
        if self.typ == 'player':
            self.LVL += 1
        
    def Level(self, stat, statNum):
        temp = int(RandNum('low') * .2) #get temp number for stat increase
        if stat == 'ATK':
            self.ATK += temp
            if self.typ == 'player': #if its a player
                print(f'ATK: {statNum} + {temp}')
                time.sleep(0.1)
        elif stat == 'DEF':
            self.DEF += temp
            if self.typ == 'player': #if its a player
                print(f'DEF: {statNum} + {temp}')
                time.sleep(0.1)
        elif stat == 'MAG':
            self.MAG += temp
            if self.typ == 'player': #if its a player
                print(f'MAG: {statNum} + {temp}')
                time.sleep(0.1)
        elif stat == 'RES':
            self.RES += temp
            if self.typ == 'player': #if its a player
                print(f'RES: {statNum} + {temp}')
                time.sleep(0.1)
        elif stat == 'SPE':
            self.SPE += temp
            if self.typ == 'player': #if its a player
                print(f'SPE: {statNum} + {temp}')
                time.sleep(0.1)
        elif stat == 'HP':
            self.HP += temp
            if self.typ == 'player': #if its a player
                print(f'HP: {statNum} + {temp}')
                time.sleep(0.1)

#weapon class 
class Weapon:
    def __init__(self, name, bp, buff):
        self.name = name
        self.bp = bp
        self.buff = buff
        
    def Use(self, attacker, defender):
        damage = int((((((((2*attacker.LVL)/5)+2)*self.bp*attacker.ATK)/defender.DEF)/10)*round(random.uniform(0.8,1.2), 3)))
        defender.HP -= damage
        if defender.HP < 0:
            defender.HP = 0
        print(f'{attacker.name} used {self.name} and dealt {damage} damage to {defender.name}')
        print(f'{defender.name} has {defender.HP} health left')

#action class for all 20 actions
class Action: 
    def __init__ (self, name, amt, desc, mod = None, bp = None, bf1 = None, bf2 = None, dbf1 = None, dbf2 = None, stun = None, drain = None, heal = None):
        self.name = name #namne of action
        self.amt = amt #amount of moves per level
        self.amtMax = amt #max amount of moves
        self.desc = desc #description of move
        self.mod = mod #mod used for damage calc
        self.bp = bp #base power
        self.bf1 = bf1 #buff 1
        self.bf2 = bf2 #buff 2
        self.dbf1 = dbf1 #debuff 1
        self.dbf2 = dbf2 #debuff 2
        self.stun = stun #stun opponent next turn
        self.drain = drain #drain life
        self.heal = heal #heal yourself

    def Use(self, attacker, defender):
        self.amt -= 1
        if self.bp:
            #damage calc (use mod)
            if self.mod == 'ATK': #attack mod
                damage = int((((((((2*attacker.LVL)/5)+2)*self.bp*attacker.ATK)/defender.DEF)/10)*round(random.uniform(0.8,1.2), 3)))
                defender.HP -= damage #minus health
                if defender.HP < 0:
                    defender.HP = 0
                print(f'{attacker.name} used {self.name} and dealt {damage} damage to {defender.name}')
                time.sleep(0.5)
                print(f'{defender.name} has {defender.HP} health left')
                time.sleep(0.5)
            elif self.mod == 'MAG': #magic mod
                damage = int((((((((2*attacker.LVL)/5)+2)*self.bp*attacker.MAG)/defender.RES)/10)*round(random.uniform(0.8,1.2), 3)))
                defender.HP -= damage
                if defender.HP < 0:
                    defender.HP = 0
                print(f'{attacker.name} used {self.name} and dealt {damage} damage to {defender.name}')
                time.sleep(0.5)
                print(f'{defender.name} has {defender.HP} health left')
                time.sleep(0.5)
        if self.heal:
            healAmt = round(RandNum(self.heal) * 0.3)
            attacker.HP += healAmt
            print(f'{attacker.name} used {self.name} and healed by {healAmt} HP')
            print(f'{attacker.name} has {attacker.HP} HP')
            time.sleep(0.5)
        if self.drain:
            drainAmt = round(RandNum('low') * 0.5)
            defender.HP -= drainAmt
            if defender.HP < 0:
                defender.HP = 0
            attacker.HP += drainAmt
            print(f'{attacker.name} used {self.name} and drained {defender.name}\'s HP by {drainAmt} to heal')
            print(f'{attacker.name} has {attacker.HP} HP')
            print(f'{defender.name} has {defender.HP} HP left')
            time.sleep(0.5)
        if self.bf1:
            amntRaised = round(RandNum(self.bf1['amnt']) * 0.15)
            buffType = self.bf1['type']
            RaiseStat(attacker, buffType, amntRaised)
            print(f'{attacker.name} raised their {buffType} by {amntRaised}')
            time.sleep(0.5)
        if self.bf2:
            amntRaised = round(RandNum(self.bf2['amnt']) * 0.15)
            buffType = self.bf2['type']
            RaiseStat(attacker, buffType, amntRaised)
            print(f'{attacker.name} raised their {buffType} by {amntRaised}')
            time.sleep(0.5)
        if self.dbf1:
            amntLowered = round(RandNum(self.dbf1['amnt']) * 0.15)
            debuffType = self.dbf1['type']
            LowerStat(defender, debuffType, amntLowered)
            print(f'{attacker.name} lowered {defender.name}\'s {debuffType} by {amntLowered}')
            time.sleep(0.5)
        if self.dbf2:
            amntLowered = round(RandNum(self.dbf2['amnt']) * 0.15)
            debuffType = self.dbf2['type']
            LowerStat(defender, debuffType, amntLowered)
            print(f'{attacker.name} lowered {defender.name}\'s {debuffType} by {amntLowered}')
            time.sleep(0.5)
        if self.stun:
            print(f'{attacker.name} used {self.name} and stunned {defender.name}')
            time.sleep(0.5)
            print(f'{defender.name} turn is skipped.')
            time.sleep(0.5)
            return True
        return False
        
        
def RaiseStat(attacker, stat, amntRaised):
    if stat == 'ATK':
        attacker.ATK += amntRaised
    elif stat == 'DEF':
        attacker.DEF += amntRaised
    elif stat == 'MAG':
        attacker.MAG += amntRaised
    elif stat == 'RES':
        attacker.RES += amntRaised
    elif stat == 'SPE':
        attacker.SPE += amntRaised

def LowerStat(defender, stat, amntLowered):
    if stat == 'ATK':
        defender.ATK -= amntLowered
    elif stat == 'DEF':
        defender.DEF -= amntLowered
    elif stat == 'MAG':
        defender.MAG -= amntLowered
    elif stat == 'RES':
        defender.RES -= amntLowered
    elif stat == 'SPE':
        defender.SPE -= amntLowered

def RandNum(ranges): #function to make it easier to assign attributes within the ranges
    if ranges == 'low':
        return random.randint(25,40)
    elif ranges == 'med':
        return random.randint(40,60)
    elif ranges == 'high':
        return random.randint(60,75)
        
#create actions
#buffs and debuffs are stored as dictionaries because we need the stat affected and also the amount affected
#dictionary lets us store both but not quite sure how we will reguritate the info
sneakAttack = Action('sneak attack', 2, 'Sneak up on your opponent - deal high damage and stun your opponent for their next turn', mod = 'ATK', bp = 75, stun = True)
thunderbolt = Action('thunderbolt', 4, 'Cast a thunderbolt - deal medium damage and debuff your opponents RES', mod = 'MAG', bp = 50, dbf1 = {'type':'RES', 'amnt':'med'})
fireball = Action('fireball', 4, 'Cast a fireball - deal medium damage and buff your MAG', mod = 'MAG', bp = 50, bf1 = {'type':'MAG', 'amnt':'med'})
healingProwess = Action('healing prowess', 2, 'Use healing magic - heal yourself a high amount', mod = 'MAG', heal = 'high')
smokeBomb = Action('smoke bomb', 6, 'Throw a smokebomb - debuff your opponents DEF', mod = 'ATK', dbf1 = {'type':'DEF', 'amnt':'low'})
entangle = Action('entangle', 2, 'Summon vines to entange your opponent - deal low damage and debuff your opponents SPE', mod = 'MAG', bp = 25, dbf1 = {'type':'SPE', 'amnt':'high'})
frostNova = Action('frost nova', 4, 'Summon a blizzard - deal medium damage and debuff your opponents MAG', mod = 'MAG', bp = 50, dbf1 = {'type':'MAG', 'amnt':'med'})
whirlwindStrike = Action('whirlwind strike', 4, 'Make speedy strikes - buff your SPE and stun your opponent for their next turn', mod = 'ATK', bf1 = {'type':'SPE', 'amnt':'med'}, stun = True)
cripplingBlow = Action('crippling blow', 2, 'Make a heavy strike - deal high damage and debuff your opponents DEF', mod = 'ATK', bp = 75, dbf1 = {'type':'DEF', 'amnt':'med'})
shieldBash = Action('shield bash', 2, 'Surge with your shield - debuff your opponents ATK and DEF', mod = 'ATK', dbf1 = {'type':'ATK', 'amnt':'high'}, dbf2 = {'type':'DEF', 'amnt':'high'})
weaponFury = Action('weapon fury', 2, 'Slash a slurry of weapons - deal high damage and buff your SPE', mod = 'ATK', bp = 75, bf1 = {'type':'SPE', 'amnt':'med'})
healingHands = Action('healing hands', 6, 'Use healing magic - heal yourself a low amount', mod = 'MAG', heal = 'low')
safeguard = Action('safeguard', 2, 'Hunker down to safety - buff your ATK and DEF', mod = 'ATK', bf1 = {'type':'ATK', 'amnt':'high'}, bf2 = {'type':'DEF', 'amnt':'high'})
drain = Action('drain', 2, 'Drain your opponents life - steal their health and heal yourself', drain = True)
sharpen = Action('sharpen', 6, 'Take a turn to sharpen your weapon - buff your ATK', mod = 'ATK', bf1 = {'type':'ATK', 'amnt':'med'})
mysticSuppression = Action('mystic suppression', 4, 'Suppress your opponents magic - buff your MAG and debuff your opponents RES', mod = 'MAG', bf1 = {'type':'MAG', 'amnt':'high'}, dbf1 = {'type':'RES', 'amnt':'low'})
spellSurge = Action('spell surge', 6, 'Meditate for one turn - buff your MAG and RES', mod = 'MAG', bf1 = {'type':'MAG', 'amnt':'low'}, bf2 = {'type':'RES', 'amnt':'low'})
enchantmentBash = Action('enchantment bash', 4, 'Enchant your weapon - deal medium damage and buff your RES', mod = 'MAG', bp = 50, bf1 = {'type':'RES', 'amnt':'med'})
frenzy = Action('frenzy', 4, 'Go into a frezied state - buff your ATK and SPE', mod = 'ATK', bf1 = {'type':'ATK', 'amnt':'low'}, bf2 = {'type':'SPE', 'amnt':'high'})
rage = Action('rage', 2, 'Go into a raged state - deal high damage and buff your DEF', mod = 'ATK', bp = 75, bf1 = {'type':'DEF', 'amnt':'med'})

#array of all the actions
actions = [sneakAttack, thunderbolt, fireball, healingProwess, smokeBomb, entangle, frostNova, whirlwindStrike, cripplingBlow, shieldBash, weaponFury, healingHands, safeguard, drain, sharpen, mysticSuppression, spellSurge, enchantmentBash, frenzy, rage]

#create weapons
dagger = Weapon('dagger', 25, 'RES')
bigAxe = Weapon('big axe', 60, 'ATK')
bow = Weapon('bow', 50, 'DEF')
miniAxes = Weapon('mini axes', 25, 'SPE')
rock = Weapon('rock', 15, 'ATK')
spear = Weapon('spear', 40, 'RES')
club = Weapon('club', 60, 'MAG')
claw = Weapon('claw', 20, 'SPE')
sword = Weapon('sword', 50, 'MAG')

# array of all weapons
weapons = [dagger, bigAxe, bow, miniAxes, rock, spear, club, claw]

# Function to take the user's name and allow for them to choose a class. then, return the created object of the character.
def ChooseClass(name):
    # randomly collect two actions form the action list for the new character
    playerActions = random.sample(actions, 2)
    for playerAction in playerActions:
        playerAction = copy.deepcopy(playerAction)

    print('\nChoose your class to begin your adventure.')
    
    while(True):
        print('\n1. Druid\n2. Lumberjack\n3. Hunter\n4. Berserker\n')
        choice = input('Enter a number from the list of choices: ')
        if choice == '1':
            print(f'\nDruid\nHP: med\nATK: low\nDEF: med\nMAG: high\nRES: high\nSPE: med') #character stats
            print(f'\nWeapon: dagger\nBase Power: 25\nBuff: RES') #default weapon stats
            temp = input('\nPlay as a Druid? (Y/N): ').lower()
            if temp == 'y':
                return Creature('player', name, RandNum('med'), RandNum('low'), RandNum('med'), RandNum('high'), RandNum('high'), RandNum('med'), 1, dagger, playerActions)
            else:
                continue
        elif choice == '2':
            print(f'\nLumberjack\nHP: high\nATK: high\nDEF: med\nMAG: low\nRES: low\nSPE: low') #character stats
            print(f'\nWeapon: big axe\nBase Power: 60\nBuff: ATK') #default weapon stats
            temp = input('\nPlay as a Lumberjack? (Y/N): ').lower()
            if temp == 'y':
                return Creature('player', name, RandNum('high'), RandNum('high'), RandNum('med'), RandNum('low'), RandNum('low'), RandNum('low'), 1, bigAxe, playerActions)
            else:
                continue
        elif choice == '3':
            print(f'\nHunter\nHP: med\nATK: med\nDEF: med\nMAG: med\nRES: med\nSPE: med') #character stats
            print(f'\nWeapon: bow\nBase Power: 50\nBuff: DEF') #default weapon stats
            temp = input('\nPlay as a Hunter? (Y/N): ').lower()
            if temp == 'y':
                return Creature('player', name, RandNum('med'), RandNum('med'), RandNum('med'), RandNum('med'), RandNum('med'), RandNum('med'), 1, bow, playerActions)
            else:
                continue
        elif choice == '4':
            print(f'\nBerserker\nHP: med\nATK: low\nDEF: low\nMAG: med\nRES: med\nSPE: high') #character stats
            print(f'\nWeapon: Mini Axes\nBase Power: 25\nBuff: SPE') #default weapon stats
            temp = input('\nPlay as a Berserker? (Y/N): ').lower()
            if temp == 'y':
                return Creature('player', name, RandNum('med'), RandNum('low'), RandNum('low'), RandNum('med'), RandNum('med'), RandNum('high'), 1, miniAxes, playerActions)
            else:
                continue
        else:
            print('Invalid input. Please only enter a valid integer.\n')

# Function to create a new character for the user when they start a new game.
def StartGame():
    playerName = input('Enter your name: ')
    input('\nThis is a text based wilderness Rogue-Like. \nEach character starts with a default weapon and two random actions. \nActions are special moves that can be used a limited number of times per level. \nEach action is affected by either the player\'s ATK or MAG stat. \nDEF defends ATK \nRES resists MAG \n\nSlay The Forest Guardian in hopes to protect your world. (enter to continue)')
    player = ChooseClass(playerName)
    return player

# Main function of the game, controlling the loop for level status and completion.
def PlayGame(player, gameLvl=1, lvlMonstersLeft=1):
    stillPlaying = True
    monsterDefeated = False
    print('\nYou are wandering in the wilderness. What do you do?')
    # The stillPlaying loop runs untill the player saves and quits, dies, or beats the game.
    while stillPlaying:
        # At the start of every iteration, if the player as gotten to level 5, the final battle starts.
        if lvlMonstersLeft <= 0:
            print(f'\nYou completed level {gameLvl} and are now on level {gameLvl + 1}')
            player.LevelUp()
            gameLvl += 1
            lvlMonstersLeft = gameLvl
        if gameLvl == 5:
            stillPlaying, monsterDefeated = FinalBattle(player, gameLvl)
        # Otherwise, the player is reminded of their current status (game level, monsters left to next level, etc.).
        else:
            # The user chooses to either battle, search for treasure, view stats, or save and quit.
            print(f'\n1. Battle a Monster ({lvlMonstersLeft} monster(s) needed to defeat to advance to next level)\n2. Search for Treasure\n3. Check Current Stats\n! to Save & Quit')
            option = input('Enter here: ')
            if option == '1':
                stillPlaying, monsterDefeated = BattleMonster(player, gameLvl, gameLvl)
                if monsterDefeated:
                    monsterDefeated = False
                    lvlMonstersLeft -= 1
            elif option == '2':
                stillPlaying, monsterDefeated = TreasureSearch(player, gameLvl)
                if monsterDefeated:
                    monsterDefeated = False
                    lvlMonstersLeft -= 1
            elif option == '3':
                ViewPlayerStats(player)
            elif option == '!':
                SaveProgress(player, gameLvl, lvlMonstersLeft)
                stillPlaying = False
            else:
                print('Please only enter an option from the menu.')
    # print(player.name, player.HP, player.ATK, player.DEF, player.MAG, player.RES, player.LVL, player.base.name, player.actions[0].name, player.actions[1].name)

def CheckMonsterActions(playerActions):
    tempActions = random.sample(actions, 2) #get 2 random actions
    while True:
        for action in tempActions:
            if action in playerActions: #check if player has that aciton already
                tempActions = random.sample(actions, 2) #try again
            else:
                return tempActions #if not return the actions

def CreateMonster(monsterLvl, playerActions):

    monsterActions = CheckMonsterActions(playerActions) #2 random actions, different than the players for variety
    for monsterAction in monsterActions:
        monsterAction = copy.deepcopy(monsterAction)
    
    randNum = random.randint(1, 5) #random monster is created
    if randNum == 1:
        gnomes = Creature('monster', 'gnomes', int(RandNum('low') * .75), int(RandNum('med') * .75), int(RandNum('low') * .75), int(RandNum('med') * .75), int(RandNum('low') * .75), int(RandNum('med') * .75), monsterLvl, rock, monsterActions)
        return gnomes
    elif randNum == 2:
        goblins = Creature('monster', 'goblins', int(RandNum('med') * .75), int(RandNum('low') * .75), int(RandNum('high') * .75), int(RandNum('low') * .75), int(RandNum('low') * .75), int(RandNum('high') * .75), monsterLvl, spear, monsterActions)
        return goblins
    elif randNum == 3:
        hag = Creature('monster', 'hag', int(RandNum('low') * .75), int(RandNum('low') * .75), int(RandNum('med') * .75), int(RandNum('high') * .75), int(RandNum('high') * .75), int(RandNum('med') * .75), monsterLvl, rock, monsterActions)
        return hag
    elif randNum == 4:
        troll = Creature('monster', 'troll', int(RandNum('high') * .5), int(RandNum('med') * .75), int(RandNum('med') * .75), int(RandNum('low') * .75), int(RandNum('med') * .75), int(RandNum('low') * .75), monsterLvl, club, monsterActions)
        return troll
    elif randNum == 5:
        wolves = Creature('monster', 'wolves', int(RandNum('low') * .75), int(RandNum('med') * .75), int(RandNum('med') * .75), int(RandNum('low') * .75), int(RandNum('low') * .75), int(RandNum('high') * .75), monsterLvl, claw, monsterActions)
        return wolves

def CreateBoss():
    temp = [5, 15, 16, 17, 2] #custom make these to be good (entangle, something, something)
    monsterActions = [actions[index] for index in temp] # i think this works
    for monsterAction in monsterActions:
        monsterAction = copy.deepcopy(monsterAction)
    Boss = Creature('boss', 'The Forest Guardian', 50, 50, 50, 50, 50, 1, 5, club, monsterActions)
    return Boss
    
def MonsterAI(player, monster):
    print()
    randNum = random.randint(1,3) #pick if base attack or action
    if randNum == 1:
        monster.base.Use(monster, player) #use base attack
        playerSkipped = False
    else:
        actionAmts = []
        i = 0
        for action in monster.actions: #get how many actions monster has
            i += 1
            actionAmts.append(action.amt)
        # Check to see if all the monster's actions are used up
        if not all(amt == 0 for amt in actionAmts):
            randNum = random.randint(0,(i-1)) #pick random action
            while not monster.actions[randNum].amt > 0: # If the currently selected action has no uses, search again for one that does.
                randNum = random.randint(0,(i-1))
            playerSkipped = monster.actions[randNum].Use(monster, player) #use the action
        else:
            #use base attack if the monster cannot use the actions.
            monster.base.Use(monster, player) 
            playerSkipped = False
    return playerSkipped

def PlayerMove(player, monster): #need to do all the work here for the player to pick his move
    fleeTried = False
    fled = False
    monsterSkipped = False
    optionChoices = ['1']

    print('\nIt is your turn. What do you do?')
    print('Choose a move from the menu below:\n')
    print(f'1. {player.base.name}')
    i = 1
    for action in player.actions:
        i+=1
        optionChoices.append(str(i))
        print(f'{i}. {action.name}')
    optionChoices.append('r')
    optionChoices.append('?')
    optionChoices.append('!')
    print('\'r\' to flee')
    print(f'\'?\' for {player.name}\'s info')
    print(f'\'!\' for {monster.name}\'s info\n')

    choice = input('Enter here: ')
    while choice not in optionChoices:
        choice = input('Please only enter an option from the menu. Enter here: ')
    
    print()
    if choice == '1':
        player.base.Use(player, monster) #use base weapon
        monsterSkipped = False
    elif choice == '2':
        if player.actions[0].amt > 0:
            monsterSkipped = player.actions[0].Use(player, monster)
        else:
            print(f'You are out of uses of {player.actions[0].name}')
            time.sleep(0.5)
            monsterSkipped, fled = PlayerMove(player, monster)
    elif choice == '3':
        if player.actions[1].amt > 0:
            monsterSkipped = player.actions[1].Use(player, monster)
        else:
            print(f'You are out of uses of {player.actions[1].name}')
            time.sleep(0.5)
            monsterSkipped, fled = PlayerMove(player, monster)
    elif i >= 4 and choice == '4':
        if player.actions[2].amt > 0:
            monsterSkipped = player.actions[2].Use(player, monster)
        else:
            print(f'You are out of uses of {player.actions[2].name}')
            time.sleep(0.5)
            monsterSkipped, fled = PlayerMove(player, monster)
    elif i >= 5 and choice == '5':
        if player.actions[3].amt > 0:
            monsterSkipped = player.actions[3].Use(player, monster)
        else:
            print(f'You are out of uses of {player.actions[3].name}')
            time.sleep(0.5)
            monsterSkipped, fled = PlayerMove(player, monster)
    elif i >= 6 and choice == '6': #check if 5rd action exists and is useable
        if player.actions[4].amt > 0:
            monsterSkipped = player.actions[4].Use(player, monster)
        else:
            print(f'You are out of uses of {player.actions[4].name}')
            time.sleep(0.5)
            monsterSkipped, fled = PlayerMove(player, monster)
    elif choice == 'r':
        if not fleeTried:
            # If they didn't try to flee before, they get a 20-50% chance of fleeing.
            fleeTried = True
            fleeChance = random.randint(2,6)
            randNum = random.randint(1, 10)
            if randNum > fleeChance:
                # Didn't get to flee
                print('You tried to run, but couldn\'t escape. You must finish the battle.')
                time.sleep(1)
                PlayerMove(player, monster)
            else:
                # Was able to flee
                fled = True
                print('You fled and escaped the monster.')
                time.sleep(1)
        else:
            # Already tried to flee and couldn't
            print('You can\'t flee')
            PlayerMove(player, monster)
    elif choice == '?':
        ViewPlayerStats(player)
        monsterSkipped, fled = PlayerMove(player, monster)
    elif choice == '!':
        ViewPlayerStats(monster)
        monsterSkipped, fled = PlayerMove(player, monster)
    return (monsterSkipped, fled)

# Function for controlling a individual monster battle, creating the monster with it scaled based on the monsterLvl.
def BattleMonster(player, monsterLvl, gameLvl, boss = None):
    global monsterKillLvl1
    global monsterKillLvl2
    global monsterKillLvl3
    global monsterKillLvl4
    global monsterKillLvl5
    if boss: #boss battle time!
        monster = CreateBoss()
    else:
        monster = CreateMonster(monsterLvl, player.actions)
    continueGame = False
    monsterDefeated = False
    fled = False
    print(f'\nYou encountered {monster.name}')
    time.sleep(0.5)
    #probably a while loop or smth
    skipPlayer = False #skip player turn
    skipMonster = False #skip monster turn (probably easier way to do this all)
    
#I THINK ALL THIS LOGIC MAKES SENSE
    while monster.HP > 0 and player.HP > 0: #while both are alive
        if monster.SPE > player.SPE: #monster turn first
            if not skipMonster: #if not skipping monster
                skipPlayer = MonsterAI(player, monster) #play monster turn
                time.sleep(1.5)
            else: #if skipping monster
                skipMonster = False #set monster skipping to false
                
            if player.HP > 0:
                if not skipPlayer: #if not skipping player
                    skipMonster, fled = PlayerMove(player, monster) #do player turn
                    time.sleep(0.5)
                    if fled == True:
                        break
                else: #if skipping player
                    skipPlayer = False #set player skipping to false
            else:
                break #player is dead
                
        else: #player turn first
            if not skipPlayer:
                skipMonster, fled = PlayerMove(player, monster)
                time.sleep(0.5)
                if fled == True:
                    break
            else:
                skipPlayer = False
                
            if monster.HP > 0:
                if not skipMonster: #if not skipping monster
                    skipPlayer = MonsterAI(player, monster)
                    time.sleep(1.5)
                else:
                    skipMonster = False
            else:
                break #monster is dead
    if fled == True:
        if boss:
            print('Oops! can\'t flee from the boss!')
            fled = False
            continueGame = False
        else:
            continueGame = True
    elif player.HP <= 0:
        monsterLvl = 6
        continueGame = False
        time.sleep(0.5)
        print(f'You have died! Your adventure is now over, {player.name}.\n')
    elif monster.HP <= 0:
        if boss:
            print(f'\nYou have slain the once great Forest Guardian, all of Earth thanks you')
            DisplayGameGraph()
        else:
            print(f'You defeated {monster.name}!')
            if gameLvl == 1:
                monsterKillLvl1 += 1
            elif gameLvl == 2:
                monsterKillLvl2 += 1
            elif gameLvl == 3:
                monsterKillLvl3 += 1
            elif gameLvl == 4:
                monsterKillLvl4 += 1
            elif gameLvl == 5:
                monsterKillLvl5 += 1
            else:
                pass
        continueGame = True
        monsterDefeated = True
        time.sleep(0.5)
    return (continueGame, monsterDefeated)

# Function for the player to randomly search for treasure, with a 20% of getting any situation.
def TreasureSearch(player, gameLvl):
    global treasureFoundLvl1
    global treasureFoundLvl2
    global treasureFoundLvl3
    global treasureFoundLvl4
    stillPlaying = True
    monsterDefeated = False
    randNum = random.randint(0, 5)
    if randNum == 0 or randNum == 1: #higher chance of finding monster so you cant spam treasure :)
        stillPlaying, monsterDefeated = BattleMonster(player, gameLvl + 1, gameLvl)
    elif randNum == 2:
        NewAction(player)
        if len(player.actions) < 5:
            if gameLvl == 1:
                treasureFoundLvl1 += 1
            elif gameLvl == 2:
                treasureFoundLvl2 += 1
            elif gameLvl == 3:
                treasureFoundLvl3 += 1
            elif gameLvl == 4:
                treasureFoundLvl4 += 1
            else:
                pass
        else:
            pass
    elif randNum == 3:
        RestoreActions(player)
        if gameLvl == 1:
            treasureFoundLvl1 += 1
        elif gameLvl == 2:
            treasureFoundLvl2 += 1
        elif gameLvl == 3:
            treasureFoundLvl3 += 1
        elif gameLvl == 4:
            treasureFoundLvl4 += 1
        else:
            pass
    elif randNum == 4:
        HealPlayer(player)
        if gameLvl == 1:
            treasureFoundLvl1 += 1
        elif gameLvl == 2:
            treasureFoundLvl2 += 1
        elif gameLvl == 3:
            treasureFoundLvl3 += 1
        elif gameLvl == 4:
            treasureFoundLvl4 += 1
        else:
            pass
    elif randNum == 5:
        SwitchWeapon(player)
        if gameLvl == 1:
            treasureFoundLvl1 += 1
        elif gameLvl == 2:
            treasureFoundLvl2 += 1
        elif gameLvl == 3:
            treasureFoundLvl3 += 1
        elif gameLvl == 4:
            treasureFoundLvl4 += 1
        else:
            pass
    return (stillPlaying, monsterDefeated)

# Function to get a new action from the list of action objects, adding it to the user's list of actions if they have less than 5 (max) (Runs from TreasureSearch)
def NewAction(player):
    if not len(player.actions) == 5:
        randAction = copy.deepcopy(random.choice(actions))
        while randAction in player.actions:
            randAction = copy.deepcopy(random.choice(actions))
        player.actions.append(randAction)
        print(f'\nYou found the action: {randAction.name}')
        time.sleep(0.5)
    else:
        print('\nYou already have the max amount of 5 actions.')
        time.sleep(0.5)

# Function to restore the uses of one of the player's actions (Runs from TreasureSearch)
def RestoreActions(player):
    refilledAction = random.choice(player.actions)
    refilledAction.amt = refilledAction.amtMax
    print(f'\nYou found a potion that restored all uses of {refilledAction.name}!')
    time.sleep(0.5)

# Function to heal the player (Runs from TreasureSearch)
def HealPlayer(player):
    player.HP += round(RandNum('low') * 0.65)
    print('\nYou found a healing potion!')
    time.sleep(0.5)

# Function that gets a random weapon object that is not the player's current one, allowing for them to swap or keep their weapon. (Runs from TreasureSearch)
def SwitchWeapon(player):
    randWeapon = random.choice(weapons)
    while randWeapon.name == player.base.name:
        randWeapon = random.choice(weapons)
    print(f'\nYou found a {randWeapon.name}!'); time.sleep(0.5)
    print(f'Base Power: {randWeapon.bp}\nBuff: {randWeapon.buff}'); time.sleep(0.5)
    print(f'\nYou have a {player.base.name}!'); time.sleep(0.5)
    print(f'Base Power: {player.base.bp}\nBuff: {player.base.buff}'); time.sleep(0.5)
    choice = input(f'\nDo you want to switch out your {player.base.name}? (Enter \'Y\' or \'N\'): ')   
    time.sleep(0.5)
    while choice not in ['Y', 'y', 'N', 'n']:
        choice = input(f'Please only enter \'Y\' or \'N\' for your decision: ')
    if choice == 'Y' or choice == 'y':
        player.RemoveWeaponBuff(player.base.buff)
        player.base = randWeapon
        player.WeaponBuff()

# Function for displaying the player's stats.
def ViewPlayerStats(player):
    print(f'\n{player.name}')
    #level
    print(f'Level: {player.LVL}')
    time.sleep(0.5)
    #weapon
    print(f'\nWeapon: {player.base.name}')
    print(f'Base Power: {player.base.bp}')
    time.sleep(0.5)
    #actions
    for action in player.actions:
        print(f'\n{action.name}, Uses: {action.amt}/{action.amtMax}')
        print(f'Description: {action.desc}')
        time.sleep(0.3)
    #HP
    print(f'\nHP: {player.HP}')
    #ATK
    print(f'ATK: {player.ATK}')
    #DEF
    print(f'DEF: {player.DEF}')
    #MAG
    print(f'MAG: {player.MAG}')
    #RES
    print(f'RES: {player.RES}')
    #SPE
    print(f'SPE: {player.SPE}')
    time.sleep(1)

def FinalBattle(player, gameLvl):
    print('\nBOSS BATTLE')
    time.sleep(1)
    stillPlaying, monsterDefeated = BattleMonster(player, 5, gameLvl, boss = True)
    stillPlaying = False
    return (stillPlaying, monsterDefeated)

def DisplayGameGraph():
    left_coordinates=[1,2,3,4,5,6,7,8,9]
    
    
    heights=[monsterKillLvl1,treasureFoundLvl1,monsterKillLvl2,treasureFoundLvl2,monsterKillLvl3,treasureFoundLvl3,monsterKillLvl4,treasureFoundLvl4,monsterKillLvl5]
    bar_labels=['Lvl 1 Mon','Lvl 1 Trea','Lvl 2 Mon','Lvl 2 Trea','Lvl 3 Mon','Lvl 3 Trea','Lvl 4 Mon','Lvl 4 Trea','Lvl 5 Mon']
    plt.bar(left_coordinates,heights,tick_label=bar_labels,width=0.6,color=['green','gold'])
    plt.xlabel('Monsters & Treasures')
    plt.ylabel('Total Amount')
    plt.title("Amount of treasures found for and monsters slain per Level")
    plt.show()
    pass #add a thing in here to end the program when displayed!

# Function for writing data into the GameSaves.txt file when the user chooses to save and quit.
def SaveProgress(player, gameLvl, lvlMonstersLeft):
    global treasureFoundLvl1
    global treasureFoundLvl2
    global treasureFoundLvl3
    global treasureFoundLvl4
    global monsterKillLvl1
    global monsterKillLvl2
    global monsterKillLvl3
    global monsterKillLvl4
    global monsterKillLvl5
    actionsStr = ''
    for action in player.actions:
        actionsStr += f'{action.name}.{action.amt}-'
    if not os.path.isfile(saveFilePath):
        with open(saveFilePath, 'w') as newFile:
            newFile.write('Name,HP,ATK,DEF,MAG,RES,SPE,LVL,Base,Actions,Level,lvlMonstersLeft,treasureFoundLvl1,treasureFoundLvl2,treasureFoundLvl3treasureFoundLvl4,monsterKillLvl1,monsterKillLvl2,monsterKillLvl3,monsterKillLvl4,monsterKillLvl5')
    with open(saveFilePath, 'a') as file:
        file.write(f'\n{player.name},{player.HP},{player.ATK},{player.DEF},{player.MAG},{player.RES},{player.SPE},{player.LVL},{player.base.name},{actionsStr},{gameLvl},{lvlMonstersLeft},{treasureFoundLvl1},{treasureFoundLvl2},{treasureFoundLvl3},{treasureFoundLvl4},{monsterKillLvl1},{monsterKillLvl2},{monsterKillLvl3},{monsterKillLvl4},{monsterKillLvl5}')
    print('Your progress has been saved.')

# Begin of Run

# Variables for the file path of the text file storing game data and the bool for the outer loop.
saveFilePath = 'GameSaves.txt'
Playing = True


print('Welcome to Wilderness Explorers')

while(Playing):
    treasureFoundLvl1 = 0
    treasureFoundLvl2 = 0
    treasureFoundLvl3 = 0
    treasureFoundLvl4 = 0
    monsterKillLvl1 = 0
    monsterKillLvl2 = 0
    monsterKillLvl3 = 0
    monsterKillLvl4 = 0
    monsterKillLvl5 = 1
    # The user chooses at the start whether to continue a game or start a new one.
    print('1. Continue Game\n2. New Game')
    choice = input('Enter 1 or 2 here: ')
    if choice == '1':
        # If a save file exists, all saves are listed out (character name and game level).
        if os.path.isfile(saveFilePath):
            # WILL FIX SAVING AND CONTINUING FOR ACTION USES -- -- WIP -- -- 
            with open(saveFilePath, 'r') as file:
                lines = file.readlines()

                headers = lines[0].split(',')
                print(f'   {headers[0]: <12} {headers[10]}')

                # every line, except the headers, gets split by commas to display the name and game level.
                for i in range(1, len(lines)):
                    props = lines[i].split(',')
                    print(f'{i}. {props[0]: <12} {props[10]}')
            # The user chooses a specific save
            print('Choose a save from the menu')
            choice = int(input('Enter here: '))
            while choice not in range(1, len(lines)):
                choice = int(input('Please only enter a choice from the list: '))
            # Once chosen, the game info is split.
            gameStats = lines[choice].split(',')
            # The weapon object is assigned by finding the object with the name in the file.
            for weapon in weapons:
                if weapon.name == gameStats[8]:
                    curWeapon = weapon
            # All the player's actions are found the same as the weapon.
            curActionStrs = gameStats[9].split('-')
            curActionNames = []
            curActionUses = []
            for actionStr in curActionStrs:
                if actionStr != '':
                    actionInfo = actionStr.split('.')
                    curActionNames.append(actionInfo[0])
                    curActionUses.append(int(actionInfo[1]))

            curActions = []
            for i in range(len(curActionNames)):
                for action in actions:
                    if curActionNames[i] == action.name:
                        newAction = copy.deepcopy(action)
                        newAction.amt = curActionUses[i]
                        curActions.append(newAction)
            
            treasureFoundLvl1 = int(gameStats[12])
            treasureFoundLvl2 = int(gameStats[13])
            treasureFoundLvl3 = int(gameStats[14])
            treasureFoundLvl4 = int(gameStats[15])
            monsterKillLvl1 = int(gameStats[16])
            monsterKillLvl2 = int(gameStats[17])
            monsterKillLvl3 = int(gameStats[18])
            monsterKillLvl4 = int(gameStats[19])
            monsterKillLvl5 = int(gameStats[20])
            # Once all teh current game data is found, a new instance of the player is created.
            curPlayer = Creature('player', gameStats[0], int(gameStats[1]), int(gameStats[2]), int(gameStats[3]), int(gameStats[4]), int(gameStats[5]), int(gameStats[6]), int(gameStats[7]), curWeapon, curActions)
            # The game begins with the user's character, current game level and current lvlMonstersLeft
            PlayGame(curPlayer, int(gameStats[10]), int(gameStats[11]))
        else:
            # The path doesn't exist, no files have been saved yet.
            print('\nNo games saved. Please begin a new adventure.\n')
            continue
    elif choice == '2':
        # If the user wants a new game, StartGame runs to create their character
        newPlayer = StartGame()
        # The game begins with the new character and the default parameters for game level and lvlMonstersLeft
        PlayGame(newPlayer)
    else:
        print('Please only enter 1 or 2.\n')
        continue
    # Once the player is taken out of PlayGame() for quitting, dying, or beating the game, They are asked to play again.
    playAgain = input('Would you like to continue/play again? (Please enter \'Y\' or \'N\'): ')
    while playAgain not in ['Y', 'y', 'N', 'n']:
        playAgain = input('Please only enter \'Y\' or \'N\' for your choice: ')
    if playAgain == 'N' or playAgain == 'n':
        break
# End message when choosen not to play again.
print('Thank you for playing Wilderness Explorers!')
