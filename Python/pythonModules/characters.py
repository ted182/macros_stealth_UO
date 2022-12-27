from stealth import CharName

def getCharacter(_characters):
    for i in _characters:
        if i['name'] == CharName():
            return i
    print('[characters] -> personagem não encontrado na base de dados, finalizando script...')
    exit()


characters = [
    {
        'name': 'char1',
        'restock-bag-mining': 0x00000000,             # <- colocar reags de recall e picareta
        'ores-bag': 0x00000000,                       # <- onde são depositados os ores
        'gems-bag': 0x00000000,                       # <- onde são depositados as pedras preciosas
        'rune-bank': [111, 222, 1, 3, 'Runa Banco'],  # <- rune: {x, y, page, rune, id}
        'rune-mine': [111, 222, 1, 4, 'Runa Mina']
    },
    {
        'name': 'char2',
        'restock-bag-mining': 0x00000000,
        'ores-bag': 0x00000000,
        'gems-bag': 0x00000000,        
        'rune-bank': [111, 222, 1, 3, 'Runa Banco'],
        'rune-mine': [111, 222, 1, 7, 'Runa Mina']
    },
    {
        'name': 'char3',
        'restock-bag-mining': 0x000000,
        'ores-bag': 0x000000,  
        'gems-bag': 0x000000,       
        'rune-bank': [111, 222, 1, 3, 'Runa Banco'],
        'rune-mine': [111, 222, 1, 7, 'Runa Mina']
    }
]
