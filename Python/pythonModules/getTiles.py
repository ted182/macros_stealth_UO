from stealth import GetX, GetY, GetLandTilesArray, GetStaticTilesArray, WorldNum, Self, Dead

def getTiles(radius: int, tiles: list[int]):
    """ Returns list of tiles, found in specified radius.
       Uses GetLandTilesArray + GetStaticTilesArray for improved shard compatibility.
    Args:
        radius int: Radius of search
        tiles list: List of tiles to find
    Returns
        list: List of tuples (tile, x, y, z)
    """
    x, y = GetX(Self()), GetY(Self())
    tilesxy = []
    tilesDict = []
    
    if Dead():
        return tilesDict

    for currenttile in tiles:
        tilesxy += GetLandTilesArray(x - radius, y - radius, x + radius, y + radius, WorldNum(), currenttile)
        tilesxy += GetStaticTilesArray(x - radius, y - radius, x + radius, y + radius, WorldNum(), currenttile)
    for tile, x, y, z in tilesxy:
        tilesDict.append( {'Tile': tile,'X': x,'Y': y,'Z': z} )
    return tilesDict