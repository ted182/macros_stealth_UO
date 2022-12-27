from stealth import *
from datetime import datetime, timedelta


from pythonModules.characters import *
from pythonModules.aguardar import *
from pythonModules.recall import recall
from pythonModules.mover import *
from pythonModules.openBank import *
from pythonModules.openContainer import *
from pythonModules.getTiles import *
from pythonModules.macroDuration import *
from pythonModules.unloadToBank import *
from pythonModules.restockMacroReags import *
from pythonModules.callHelpRoom import callHelpRoom


_radius = 20
_maxRetries = 25
_maxWeight = Weight() + 40

oreTypes = [0x19B9, 0x19BA, 0x19B7, 0x19B8]
pickaxeType = 0x0E85
playerX = 0
playerY = 0
deathCount = 0
startMacroTime = 0
char = getCharacter(characters)



ores = [
    {'name': 'Iron', 'type': oreTypes, 'color': 0x0000, 'amount': 0},
    {'name': 'Ceramic', 'type': oreTypes, 'color': 0x00f2, 'amount': 0}, 
    {'name': 'Rusty', 'type': oreTypes, 'color': 0x0750, 'amount': 0},
    {'name': 'Old Copper', 'type': oreTypes, 'color': 0x0590, 'amount': 0},
    {'name': 'Dull Copper', 'type': oreTypes, 'color': 0x060A, 'amount': 0},
    {'name': 'Copper', 'type': oreTypes, 'color': 0x0641, 'amount': 0},
    {'name': 'Bronze', 'type': oreTypes, 'color': 0x06D6, 'amount': 0},   
    {'name': 'Silver', 'type': oreTypes, 'color': 0x0231, 'amount': 0},
    {'name': 'Shadow', 'type': oreTypes, 'color': 0x0770, 'amount': 0},
    {'name': 'Agapite', 'type': oreTypes, 'color': 0x0400, 'amount': 0},
    {'name': 'Rose', 'type': oreTypes, 'color': 0x0665, 'amount': 0},
    {'name': 'Valorite', 'type': oreTypes, 'color': 0x0515, 'amount': 0},
    {'name': 'Verite', 'type': oreTypes, 'color': 0x07d1, 'amount': 0},
    {'name': 'Gold', 'type': oreTypes, 'color': 0x045E, 'amount': 0},
    {'name': 'Bloodrock', 'type': oreTypes, 'color': 0x04c2, 'amount': 0},
    {'name': 'Blackrock', 'type': oreTypes, 'color': 0x0455, 'amount': 0},
    {'name': 'Mytheril', 'type': oreTypes, 'color': 0x052d, 'amount': 0},
    {'name': 'Chaos', 'type': oreTypes, 'color': 0x03df, 'amount': 0},
    {'name': 'Order', 'type': oreTypes, 'color': 0x024f, 'amount': 0},
    {'name': 'Adamantium', 'type': oreTypes, 'color': 0x07A1, 'amount': 0}
]

gems = [
    {'name': 'rubies', 'type': [0x0F13], 'color': 0x0000, 'amount': 0},
    {'name': 'emeralds', 'type': [0x0F10], 'color': 0x0000, 'amount': 0},
    {'name': 'tourmalines', 'type': [0x0F18], 'color': 0x0000, 'amount': 0},
    {'name': 'star sapphires', 'type': [0x0F0F], 'color': 0x0000, 'amount': 0},
    {'name': 'diamonds', 'type': [0x0F26], 'color': 0x0000, 'amount': 0},
    {'name': 'citrines', 'type': [0x0F15], 'color': 0x0000, 'amount': 0},
    {'name': 'sapphires', 'type': [0x0F11], 'color': 0x0000, 'amount': 0},
    {'name': 'amethysts', 'type': [0x0F16], 'color': 0x0000, 'amount': 0}
]

reags = [
    {'name': 'Black Perls', 'type': 0x0F7A, 'bankAmount': 0, 'bagAmount': 3},
    {'name': 'Blood Moss', 'type': 0x0F7B, 'bankAmount': 0, 'bagAmount': 3},
    {'name': 'Mandrake Roots', 'type': 0x0F86, 'bankAmount': 0, 'bagAmount': 3},
    {'name': 'Pickaxe', 'type': pickaxeType, 'bankAmount': 0, 'bagAmount': 1}
]

mountainAndCaveTiles = [
    1339, 1386, 1363, 1362, 1361, 1359, 1358, 1357, 
    1356, 1355, 1354, 1353, 1352, 1351, 1350, 1349, 
    1348, 1347, 1346, 1345, 1344, 1343, 1342, 1341, 
    1340 
]



def distance(val: dict):
    #recebe um dictionary com {tile,x,y,z} e retorna a distancia do char ao ponto xy informado no dict
    return ( ( (val['X'] - playerX)**2 + (val['Y'] - playerY)**2 )**0.5 )    

def ordenaSpots(spots: list[dict]):
    global playerX, playerY
    playerX = GetX(Self())
    playerY = GetY(Self())
    spots.sort(key=distance)
    return spots    

def mine(spot):
    
    journalSucess = 'You put|' \
                    'You loosen some rocks'
                    
    journalFail =   'Try mining elsewhere|' \
                    'That is too far away|' \
                    'You cannot|' \
                    'nothing here to mine for|' \
                    'have no line of sight'
    
    journalAll = journalSucess + '|' + journalFail
    retries = 0

    while not Dead():
        start = datetime.now()
        end = start + timedelta(seconds=10)
        if checkPickaxe():
            WaitTargetTile(spot['Tile'], spot['X'], spot['Y'], spot['Z'])
            UseType(pickaxeType, -1)
            retries += 1
            WaitJournalLine(start, journalAll, 10000)
            
            if InJournalBetweenTimes('nothing here to mine for', start, end) > 0:
                #print( str(spot) + ' <- nothing here' )
                break
            
            if InJournalBetweenTimes('cannot mine so close', start, end) > 0:
                #print( str(spot) + ' <- so close' )
                break
            
            if InJournalBetweenTimes('have no line of sight', start, end) > 0:
                #print( str(spot) + ' <- line of sight' )
                break
            
            if InJournalBetweenTimes('That is too far away', start, end) > 0:
                #print( str(spot) + ' <- far away' )
                break
            
            if InJournalBetweenTimes('Try mining elsewhere', start, end) > 0:
                #print( str(spot) + ' <- mining elsewhere' )
                break
            
            #print( str(spot) + ' <- sucess!!' )
            
            if (retries > _maxRetries):
                break
            
            aguardar(100)

        else:
            print ('[mine] -> sem picareta na bag...')
            restockProtocol()            


def checkWeight():
    if ( Weight() > _maxWeight ):
        return True
    return False

def checkPickaxe():
    if ( ObjAtLayerEx(LhandLayer(),Self()) or ObjAtLayerEx(RhandLayer(),Self()) or FindType(pickaxeType, Backpack()) ) > 0:
        return True
    return False

def restockProtocol():
    global char
    if Dead():
        return True
    recall( char['rune-bank'] )
    unloadOres()
    unloadGems()
    restockReags()
    macroDuration(startMacroTime)
    print( 'mortes: ' + str(deathCount) )
    print( '###############################################################' )
    print( '###############################################################' )
    recall( char['rune-mine'] )
    aguardar(100)
    return True

def unloadOres():
    global ores, char
    ores = unloadToBank(char['ores-bag'], ores)

def unloadGems():
    global gems, char
    gems = unloadToBank(char['gems-bag'], gems)

def restockReags():
    global char
    restockMacroReags(char['restock-bag-mining'], reags)

def deathRoutine():
    global deathCount
    print('[death routine] -> char morto!!!')
    deathCount += 1
    callHelpRoom()
    restockProtocol()


def main():
    
    global startMacroTime, char
    
    startMacroTime = datetime.now()
    SetGlobal('Stealth','TestVar1', 'P.Max')
    SetGlobal('Stealth','TestVar2', str(_maxWeight))
    spots = []

    restockProtocol()

    if Dead():
        deathRoutine()
    
    while True:      
        
        aguardar(100)
        spots = getTiles(_radius, mountainAndCaveTiles)
        spots = ordenaSpots(spots)
        print('foram achados: ' + str(len(spots)) + ' spots')
        if ( not len(spots) ):
            print('[main] -> o char não está em uma mina!')
            break
        
        while len(spots) > 0:
            
            spot = spots[0]
            
            if Dead():
                deathRoutine()                
                break
            
            if checkWeight():
                print('[main] -> atingiu o peso max ...')
                restockProtocol()
                break            
            
            if distance(spot) > 2 :
                mover( spot['X'], spot['Y'] )
                spots = ordenaSpots(spots)
                spot = spots[0]
            
            mine(spot)
            spots.remove(spot)


main()
