def validateBoard(boardDict):
    if 'bking' not in boardDict.values() or 'wking' not in boardDict.values():
        return False

    blackPieces = 0
    blackPawns = 0
    whitePieces = 0
    whitePawns = 0
    for colour in boardDict.values():
        if colour[0] == 'b':
            blackPawns += 1
            if colour == 'bpawn':
                blackPawn += 1
        elif colour[0] == 'w':
            whitePieces += 1
            if colour == 'wpawn':
                whitePawns += 1
    if blackPieces >= 17 or whitePieces >= 17:
        return False
    if blackPawns > 8 or whitePawns > 8:
        return False

    boardKeys = list(boardDict)
    y = ['1', '2', '3', '4', '5', '6', '7', '8']
    boardY = [s[:1] for s in boardKeys] 
    if not all(elem in y for elem in boardY): 
        return False

    x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    boardX = [s[1:] for s in boardKeys] 
    if not all(elem in x for elem in boardX): 
        return False


    for pieces in boardDict.values():
        if pieces[0] != 'b' and pieces[0] != 'w':
            return False

   
    pieceNames = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
    for names in boardDict.values():
        if names[1:] not in pieceNames:
            return False
    return True


print(validateBoard({'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}))  
print(validateBoard({'1a': 'bpawn', '2a': 'wking'})) 
print(validateBoard({'1a': 'wking', '2a': 'wking', '3c': 'bbishop'}))  
print(validateBoard({'1a': 'bking', '9z': 'wking'})) 