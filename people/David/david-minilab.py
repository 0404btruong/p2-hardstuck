"""Calculating various sets of data from a chess piece within a given chess board """


class ChessPiece:
    def __init__(self, board, piece):
        if piece not in board.values():
            raise ValueError("Invalid Piece")
        self._piece = piece
        self._board = board
        piecenamedict = {"wp":"white pawn", "bp":"black pawn", "WR":"white rook", "BR":"black rook",
                         "WN":"white knight", "BN":"black knight", "WB":"white bishop", "BB":"black bishop",
                         "WQ":"white queen", "BQ":"black queen", "WK":"white king", "BK":"black king"}
        self._piecename = piecenamedict[piece[0:2]]
        self._space = ""
        self._moveset = []
        self._attacking = []
        self._defending = []
        self._attacked_by = []
        self._defended_by = []
        self._value = 0

        self.storeboardset()

    def getname(self, piece1):
        piecenamedict = {"wp":"white pawn", "bp":"black pawn", "WR":"white rook", "BR":"black rook",
                         "WN":"white knight", "BN":"black knight", "WB":"white bishop", "BB":"black bishop",
                         "WQ":"white queen", "BQ":"black queen", "WK":"white king", "BK":"black king"}
        return piecenamedict[piece1[0:2]]
    def storeboardset(self):
        board = dict(self._board)
        storeboard = {
            "a8": [], "b8": [], "c8": [], "d8": [], "e8": [], "f8": [], "g8": [], "h8": [],
            "a7": [], "b7": [], "c7": [], "d7": [], "e7": [], "f7": [], "g7": [], "h7": [],
            "a6": [], "b6": [], "c6": [], "d6": [], "e6": [], "f6": [], "g6": [], "h6": [],
            "a5": [], "b5": [], "c5": [], "d5": [], "e5": [], "f5": [], "g5": [], "h5": [],
            "a4": [], "b4": [], "c4": [], "d4": [], "e4": [], "f4": [], "g4": [], "h4": [],
            "a3": [], "b3": [], "c3": [], "d3": [], "e3": [], "f3": [], "g3": [], "h3": [],
            "a2": [], "b2": [], "c2": [], "d2": [], "e2": [], "f2": [], "g2": [], "h2": [],
            "a1": [], "b1": [], "c1": [], "d1": [], "e1": [], "f1": [], "g1": [], "h1": []}
        piecefunc = {"wp": wpawn, "bp": bpawn, "WN": wknight, "BN": bknight, "WR": wrook, "BR": brook, "WB": wbishop,
                     "BB": bbishop, "WQ": wqueen, "BQ": bqueen, "WK": wking, "BK": bking}
        for i in board:
            if board[i] == self._piece:
                self._space = i
            piece = board[i][0:2]
            if piece != '  ':
                storeboard1 = dict(storeboard)
                storeboard = dict(piecefunc[piece](dict(board), dict(storeboard), board[i], i[0], int(i[1])))
        dictionary = {
            "bp1": [], "bp2": [], "bp3": [], "bp4": [], "bp5": [], "bp6": [], "bp7": [], "bp8": [],
            "BR1": [], "BN1": [], "BB1": [], "BQ1": [], "BK1": [], "BB2": [], "BN2": [], "BR2": [],
            "WR1": [], "WN1": [], "WB1": [], "WQ1": [], "WK1": [], "WB2": [], "WN2": [], "WR2": [],
            "wp1": [], "wp2": [], "wp3": [], "wp4": [], "wp5": [], "wp6": [], "wp7": [], "wp8": []}
        for i in storeboard:
            for k in storeboard[i]:
                dictionary[k[0:3]].append(i)
        protdict = {
            "bp1": [], "bp2": [], "bp3": [], "bp4": [], "bp5": [], "bp6": [], "bp7": [], "bp8": [],
            "BR1": [], "BN1": [], "BB1": [], "BQ1": [], "BK1": [], "BB2": [], "BN2": [], "BR2": [],
            "WR1": [], "WN1": [], "WB1": [], "WQ1": [], "WK1": [], "WB2": [], "WN2": [], "WR2": [],
            "wp1": [], "wp2": [], "wp3": [], "wp4": [], "wp5": [], "wp6": [], "wp7": [], "wp8": []}
        protfunc = {"wp": wpawnprot, "bp": bpawnprot, "WN": knightprot, "BN": knightprot, "WR": wrookprot, "BR": brookprot,
                    "WB": wbishopprot, "BB": bbishopprot, "WQ": wqueenprot, "BQ": bqueenprot}

        for i in board:
            piece = board[i][0:2]
            if piece != '  ' and piece[1] != 'K':
                protdict = protfunc[piece](board, protdict, board[i][0:3], i[0], int(i[1]))
            elif piece[1] == 'K':
                # print("Ky")
                protdict = kingprot(board, protdict, board[i][0:3], i[0], int(i[1]), storeboard)
        
        # setting values
        self._moveset = dictionary[self._piece]
        for i in self._moveset:
            if board[i][0].lower() != self._piece[0].lower() and board[i][0].lower() != " ":
                self._attacking.append(board[i])
        for i in storeboard[self._space]:
            if i[0].lower() != self._piece[0].lower():
                self._attacked_by.append(i)
        self._defending = protdict[self._piece]
        for k,v in protdict.items():
            if self._piece in v:
                self._defended_by.append(k)

        value_dictionary = {"p":1, "r":5, "n":3, "b":3, "q":9 ,"k":104}
        self._value = value_dictionary[self._piece[1].lower()]

    @property
    def piecename(self):
        return self._piecename
    @property
    def space(self):
        return self._space

    @property
    def moveset(self):
        return self._moveset
      
    @property
    def attacking(self):
        return self._attacking

    @property
    def defending(self):
        return self._defending
    
    @property
    def attacked_by(self):
        return self._attacked_by
      
    @property
    def defended_by(self):
        return self._defended_by
    
    @property
    def value(self):
        return self._value
      
# piece definitions for operating storeboard
def wpawn(board, storeboard, piece, file, rank):
    if board[file + str(rank + 1)].lower() == '  ':
        storeboard[file + str(rank + 1)].append(piece)
        if rank == 2:
            if board[file + str(rank + 2)].lower() == '  ':
                storeboard[file + str(rank + 2)].append(piece)
    try:
        if board[chr(ord(file) + 1) + str(rank + 1)][0].lower() == 'b':
            storeboard[chr(ord(file) + 1) + str(rank + 1)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank + 1)][0].lower() == 'b':
            storeboard[chr(ord(file) - 1) + str(rank + 1)].append(piece)
    except Exception:
        pass
    return storeboard


def bpawn(board, storeboard, piece, file, rank):
    if board[file + str(rank - 1)].lower() == '  ':
        storeboard[file + str(rank - 1)].append(piece)
        if rank == 7:
            if board[file + str(rank - 2)].lower() == '  ':
                storeboard[file + str(rank - 2)].append(piece)
    try:
        if board[chr(ord(file) + 1) + str(rank - 1)][0].lower() == 'w':
            storeboard[chr(ord(file) + 1) + str(rank - 1)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank - 1)][0].lower() == 'w':
            storeboard[chr(ord(file) - 1) + str(rank - 1)].append(piece)
    except Exception:
        pass
    return storeboard


def wknight(board, storeboard, piece, file, rank):
    try:
        if board[chr(ord(file) + 1) + str(rank + 2)][0].lower() != 'w':
            storeboard[chr(ord(file) + 1) + str(rank + 2)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank + 2)][0].lower() != 'w':
            storeboard[chr(ord(file) - 1) + str(rank + 2)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 1) + str(rank - 2)][0].lower() != 'w':
            storeboard[chr(ord(file) + 1) + str(rank - 2)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank - 2)][0].lower() != 'w':
            storeboard[chr(ord(file) - 1) + str(rank - 2)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 2) + str(rank + 1)][0].lower() != 'w':
            storeboard[chr(ord(file) + 2) + str(rank + 1)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 2) + str(rank + 1)][0].lower() != 'w':
            storeboard[chr(ord(file) - 2) + str(rank + 1)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 2) + str(rank - 1)][0].lower() != 'w':
            storeboard[chr(ord(file) + 2) + str(rank - 1)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 2) + str(rank - 1)][0].lower() != 'w':
            storeboard[chr(ord(file) - 2) + str(rank - 1)].append(piece)
    except Exception:
        pass
    return storeboard


def bknight(board, storeboard, piece, file, rank):
    try:
        if board[chr(ord(file) + 1) + str(rank + 2)][0].lower() != 'b':
            storeboard[chr(ord(file) + 1) + str(rank + 2)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank + 2)][0].lower() != 'b':
            storeboard[chr(ord(file) - 1) + str(rank + 2)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 1) + str(rank - 2)][0].lower() != 'b':
            storeboard[chr(ord(file) + 1) + str(rank - 2)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank - 2)][0].lower() != 'b':
            storeboard[chr(ord(file) - 1) + str(rank - 2)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 2) + str(rank + 1)][0].lower() != 'b':
            storeboard[chr(ord(file) + 2) + str(rank + 1)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 2) + str(rank + 1)][0].lower() != 'b':
            storeboard[chr(ord(file) - 2) + str(rank + 1)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 2) + str(rank - 1)][0].lower() != 'b':
            storeboard[chr(ord(file) + 2) + str(rank - 1)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 2) + str(rank - 1)][0].lower() != 'b':
            storeboard[chr(ord(file) - 2) + str(rank - 1)].append(piece)
    except Exception:
        pass
    return storeboard


def wrook(board, storeboard, piece, file, rank):
    # mccabe cyclomatic complexity, please have mercy on my code
    x = file
    y = int(rank)
    up = 8 - y
    down = y - 1
    right = 104 - ord(x)
    left = ord(x) - 97
    # up
    if up != 0:
        for i in range(1, up + 1):
            if board[file + str(rank + i)].lower() != '  ':
                if board[file + str(rank + i)][0].lower() == 'w':
                    break
                elif board[file + str(rank + i)][0].lower() == 'b':
                    storeboard[file + str(rank + i)].append(piece)
                    break
            else:
                storeboard[file + str(rank + i)].append(piece)
    # down
    if down != 0:
        for i in range(1, down + 1):
            if board[file + str(rank - i)].lower() != '  ':
                if board[file + str(rank - i)][0].lower() == 'w':
                    break
                elif board[file + str(rank - i)][0].lower() == 'b':
                    storeboard[file + str(rank - i)].append(piece)
                    break
            else:
                storeboard[file + str(rank - i)].append(piece)
    # right
    if right != 0:
        for i in range(1, right + 1):
            if board[chr(ord(file) + i) + str(rank)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) + i) + str(rank)][0].lower() == 'b':
                    storeboard[chr(ord(file) + i) + str(rank)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) + i) + str(rank)].append(piece)
    # left
    if left != 0:
        for i in range(1, left + 1):
            if board[chr(ord(file) - i) + str(rank)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) - i) + str(rank)][0].lower() == 'b':
                    storeboard[chr(ord(file) - i) + str(rank)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) - i) + str(rank)].append(piece)
    return storeboard


def brook(board, storeboard, piece, file, rank):
    # mccabe cyclomatic complexity, please have mercy on my code
    x = file
    y = int(rank)
    up = 8 - y
    down = y - 1
    right = 104 - ord(x)
    left = ord(x) - 97
    # up
    if up != 0:
        for i in range(1, up + 1):
            if board[file + str(rank + i)].lower() != '  ':
                if board[file + str(rank + i)][0].lower() == 'b':
                    break
                elif board[file + str(rank + i)][0].lower() == 'w':
                    storeboard[file + str(rank + i)].append(piece)
                    break
            else:
                storeboard[file + str(rank + i)].append(piece)
    # down
    if down != 0:
        for i in range(1, down + 1):
            if board[file + str(rank - i)].lower() != '  ':
                if board[file + str(rank - i)][0].lower() == 'b':
                    break
                elif board[file + str(rank - i)][0].lower() == 'w':
                    storeboard[file + str(rank - i)].append(piece)
                    break
            else:
                storeboard[file + str(rank - i)].append(piece)
    # right
    if right != 0:
        for i in range(1, right + 1):
            if board[chr(ord(file) + i) + str(rank)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) + i) + str(rank)][0].lower() == 'w':
                    storeboard[chr(ord(file) + i) + str(rank)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) + i) + str(rank)].append(piece)
    # left
    if left != 0:
        for i in range(1, left + 1):
            if board[chr(ord(file) - i) + str(rank)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) - i) + str(rank)][0].lower() == 'w':
                    storeboard[chr(ord(file) - i) + str(rank)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) - i) + str(rank)].append(piece)
    return storeboard


def wbishop(board, storeboard, piece, file, rank):
    # mccabe cyclomatic complexity, please have mercy on my code
    x = file
    y = int(rank)
    up = 8 - y
    down = y - 1
    right = 104 - ord(x)
    left = ord(x) - 97
    # up and to the left
    if up != 0 and left != 0:
        if up > left:
            displacement = left
        elif up < left:
            displacement = up
        else:
            displacement = left
        for i in range(1, displacement + 1):
            if board[chr(ord(file) - i) + str(rank + i)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank + i)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) - i) + str(rank + i)][0].lower() == 'b':
                    storeboard[chr(ord(file) - i) + str(rank + i)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) - i) + str(rank + i)].append(piece)
    # down and to the left
    if down != 0 and left != 0:
        if down > left:
            displacement = left
        elif down < left:
            displacement = down
        else:
            displacement = left
        for i in range(1, displacement + 1):
            if board[chr(ord(file) - i) + str(rank - i)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank - i)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) - i) + str(rank - i)][0].lower() == 'b':
                    storeboard[chr(ord(file) - i) + str(rank - i)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) - i) + str(rank - i)].append(piece)
    # up and to the right
    if up != 0 and right != 0:
        if up > right:
            displacement = right
        elif up < right:
            displacement = up
        else:
            displacement = right
        for i in range(1, displacement + 1):
            if board[chr(ord(file) + i) + str(rank + i)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank + i)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) + i) + str(rank + i)][0].lower() == 'b':
                    storeboard[chr(ord(file) + i) + str(rank + i)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) + i) + str(rank + i)].append(piece)
    # down and to the right
    if down != 0 and right != 0:
        if down > right:
            displacement = right
        elif down < right:
            displacement = down
        else:
            displacement = right
        for i in range(1, displacement + 1):
            if board[chr(ord(file) + i) + str(rank - i)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank - i)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) + i) + str(rank - i)][0].lower() == 'b':
                    storeboard[chr(ord(file) + i) + str(rank - i)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) + i) + str(rank - i)].append(piece)
    return storeboard


def bbishop(board, storeboard, piece, file, rank):
    # mccabe cyclomatic complexity, please have mercy on my code
    x = file
    y = int(rank)
    up = 8 - y
    down = y - 1
    right = 104 - ord(x)
    left = ord(x) - 97
    # up and to the left
    if up != 0 and left != 0:
        if up > left:
            displacement = left
        elif up < left:
            displacement = up
        else:
            displacement = left
        for i in range(1, displacement + 1):
            if board[chr(ord(file) - i) + str(rank + i)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank + i)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) - i) + str(rank + i)][0].lower() == 'w':
                    storeboard[chr(ord(file) - i) + str(rank + i)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) - i) + str(rank + i)].append(piece)
    # down and to the left
    if down != 0 and left != 0:
        if down > left:
            displacement = left
        elif down < left:
            displacement = down
        else:
            displacement = left
        for i in range(1, displacement + 1):
            if board[chr(ord(file) - i) + str(rank - i)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank - i)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) - i) + str(rank - i)][0].lower() == 'w':
                    storeboard[chr(ord(file) - i) + str(rank - i)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) - i) + str(rank - i)].append(piece)
    # up and to the right
    if up != 0 and right != 0:
        if up > right:
            displacement = right
        elif up < right:
            displacement = up
        else:
            displacement = right
        for i in range(1, displacement + 1):
            if board[chr(ord(file) + i) + str(rank + i)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank + i)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) + i) + str(rank + i)][0].lower() == 'w':
                    storeboard[chr(ord(file) + i) + str(rank + i)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) + i) + str(rank + i)].append(piece)
    # down and to the right
    if down != 0 and right != 0:
        if down > right:
            displacement = right
        elif down < right:
            displacement = down
        else:
            displacement = right
        for i in range(1, displacement + 1):
            if board[chr(ord(file) + i) + str(rank - i)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank - i)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) + i) + str(rank - i)][0].lower() == 'w':
                    storeboard[chr(ord(file) + i) + str(rank - i)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) + i) + str(rank - i)].append(piece)
    return storeboard


def wqueen(board, storeboard, piece, file, rank):
    # mccabe cyclomatic complexity, please have mercy on my code
    x = file
    y = int(rank)
    up = 8 - y
    down = y - 1
    right = 104 - ord(x)
    left = ord(x) - 97
    # up
    if up != 0:
        for i in range(1, up + 1):
            if board[file + str(rank + i)].lower() != '  ':
                if board[file + str(rank + i)][0].lower() == 'w':
                    break
                elif board[file + str(rank + i)][0].lower() == 'b':
                    storeboard[file + str(rank + i)].append(piece)
                    break
            else:
                storeboard[file + str(rank + i)].append(piece)
    # down
    if down != 0:
        for i in range(1, down + 1):
            if board[file + str(rank - i)].lower() != '  ':
                if board[file + str(rank - i)][0].lower() == 'w':
                    break
                elif board[file + str(rank - i)][0].lower() == 'b':
                    storeboard[file + str(rank - i)].append(piece)
                    break
            else:
                storeboard[file + str(rank - i)].append(piece)
    # right
    if right != 0:
        for i in range(1, right + 1):
            if board[chr(ord(file) + i) + str(rank)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) + i) + str(rank)][0].lower() == 'b':
                    storeboard[chr(ord(file) + i) + str(rank)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) + i) + str(rank)].append(piece)
    # left
    if left != 0:
        for i in range(1, left + 1):
            if board[chr(ord(file) - i) + str(rank)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) - i) + str(rank)][0].lower() == 'b':
                    storeboard[chr(ord(file) - i) + str(rank)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) - i) + str(rank)].append(piece)
    # up and to the left
    if up != 0 and left != 0:
        if up > left:
            displacement = left
        elif up < left:
            displacement = up
        else:
            displacement = left
        for i in range(1, displacement + 1):
            if board[chr(ord(file) - i) + str(rank + i)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank + i)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) - i) + str(rank + i)][0].lower() == 'b':
                    storeboard[chr(ord(file) - i) + str(rank + i)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) - i) + str(rank + i)].append(piece)
    # down and to the left
    if down != 0 and left != 0:
        if down > left:
            displacement = left
        elif down < left:
            displacement = down
        else:
            displacement = left
        for i in range(1, displacement + 1):
            if board[chr(ord(file) - i) + str(rank - i)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank - i)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) - i) + str(rank - i)][0].lower() == 'b':
                    storeboard[chr(ord(file) - i) + str(rank - i)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) - i) + str(rank - i)].append(piece)
    # up and to the right
    if up != 0 and right != 0:
        if up > right:
            displacement = right
        elif up < right:
            displacement = up
        else:
            displacement = right
        for i in range(1, displacement + 1):
            if board[chr(ord(file) + i) + str(rank + i)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank + i)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) + i) + str(rank + i)][0].lower() == 'b':
                    storeboard[chr(ord(file) + i) + str(rank + i)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) + i) + str(rank + i)].append(piece)
    # down and to the right
    if down != 0 and right != 0:
        if down > right:
            displacement = right
        elif down < right:
            displacement = down
        else:
            displacement = right
        for i in range(1, displacement + 1):
            if board[chr(ord(file) + i) + str(rank - i)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank - i)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) + i) + str(rank - i)][0].lower() == 'b':
                    storeboard[chr(ord(file) + i) + str(rank - i)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) + i) + str(rank - i)].append(piece)
    return storeboard


def bqueen(board, storeboard, piece, file, rank):
    # mccabe cyclomatic complexity, please have mercy on my code
    x = file
    y = int(rank)
    up = 8 - y
    down = y - 1
    right = 104 - ord(x)
    left = ord(x) - 97
    # up
    if up != 0:
        for i in range(1, up + 1):
            if board[file + str(rank + i)].lower() != '  ':
                if board[file + str(rank + i)][0].lower() == 'b':
                    break
                elif board[file + str(rank + i)][0].lower() == 'w':
                    storeboard[file + str(rank + i)].append(piece)
                    break
            else:
                storeboard[file + str(rank + i)].append(piece)
    # down
    if down != 0:
        for i in range(1, down + 1):
            if board[file + str(rank - i)].lower() != '  ':
                if board[file + str(rank - i)][0].lower() == 'b':
                    break
                elif board[file + str(rank - i)][0].lower() == 'w':
                    storeboard[file + str(rank - i)].append(piece)
                    break
            else:
                storeboard[file + str(rank - i)].append(piece)
    # right
    if right != 0:
        for i in range(1, right + 1):
            if board[chr(ord(file) + i) + str(rank)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) + i) + str(rank)][0].lower() == 'w':
                    storeboard[chr(ord(file) + i) + str(rank)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) + i) + str(rank)].append(piece)
    # left
    if left != 0:
        for i in range(1, left + 1):
            if board[chr(ord(file) - i) + str(rank)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) - i) + str(rank)][0].lower() == 'w':
                    storeboard[chr(ord(file) - i) + str(rank)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) - i) + str(rank)].append(piece)
    # up and to the left
    if up != 0 and left != 0:
        if up > left:
            displacement = left
        elif up < left:
            displacement = up
        else:
            displacement = left
        for i in range(1, displacement + 1):
            if board[chr(ord(file) - i) + str(rank + i)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank + i)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) - i) + str(rank + i)][0].lower() == 'w':
                    storeboard[chr(ord(file) - i) + str(rank + i)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) - i) + str(rank + i)].append(piece)
    # down and to the left
    if down != 0 and left != 0:
        if down > left:
            displacement = left
        elif down < left:
            displacement = down
        else:
            displacement = left
        for i in range(1, displacement + 1):
            if board[chr(ord(file) - i) + str(rank - i)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank - i)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) - i) + str(rank - i)][0].lower() == 'w':
                    storeboard[chr(ord(file) - i) + str(rank - i)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) - i) + str(rank - i)].append(piece)
    # up and to the right
    if up != 0 and right != 0:
        if up > right:
            displacement = right
        elif up < right:
            displacement = up
        else:
            displacement = right
        for i in range(1, displacement + 1):
            if board[chr(ord(file) + i) + str(rank + i)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank + i)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) + i) + str(rank + i)][0].lower() == 'w':
                    storeboard[chr(ord(file) + i) + str(rank + i)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) + i) + str(rank + i)].append(piece)
    # down and to the right
    if down != 0 and right != 0:
        if down > right:
            displacement = right
        elif down < right:
            displacement = down
        else:
            displacement = right
        for i in range(1, displacement + 1):
            if board[chr(ord(file) + i) + str(rank - i)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank - i)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) + i) + str(rank - i)][0].lower() == 'w':
                    storeboard[chr(ord(file) + i) + str(rank - i)].append(piece)
                    break
            else:
                storeboard[chr(ord(file) + i) + str(rank - i)].append(piece)
    return storeboard


def wking(board, storeboard, piece, file, rank):
    try:
        if board[file + str(rank + 1)][0].lower() != 'w':
            storeboard[file + str(rank + 1)].append(piece)
    except Exception:
        pass
    try:
        if board[file + str(rank - 1)][0].lower() != 'w':
            storeboard[file + str(rank - 1)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 1) + str(rank)][0].lower() != 'w':
            storeboard[chr(ord(file) + 1) + str(rank)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank)][0].lower() != 'w':
            storeboard[chr(ord(file) - 1) + str(rank)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 1) + str(rank + 1)][0].lower() != 'w':
            storeboard[chr(ord(file) + 1) + str(rank + 1)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank + 1)][0].lower() != 'w':
            storeboard[chr(ord(file) - 1) + str(rank + 1)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 1) + str(rank - 1)][0].lower() != 'w':
            storeboard[chr(ord(file) + 1) + str(rank - 1)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank - 1)][0].lower() != 'w':
            storeboard[chr(ord(file) - 1) + str(rank - 1)].append(piece)
    except Exception:
        pass
    return storeboard


def bking(board, storeboard, piece, file, rank):
    try:
        if board[file + str(rank + 1)][0].lower() != 'b':
            storeboard[file + str(rank + 1)].append(piece)
    except Exception:
        pass
    try:
        if board[file + str(rank - 1)][0].lower() != 'b':
            storeboard[file + str(rank - 1)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 1) + str(rank)][0].lower() != 'b':
            storeboard[chr(ord(file) + 1) + str(rank)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank)][0].lower() != 'b':
            storeboard[chr(ord(file) - 1) + str(rank)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 1) + str(rank + 1)][0].lower() != 'b':
            storeboard[chr(ord(file) + 1) + str(rank + 1)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank + 1)][0].lower() != 'b':
            storeboard[chr(ord(file) - 1) + str(rank + 1)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 1) + str(rank - 1)][0].lower() != 'b':
            storeboard[chr(ord(file) + 1) + str(rank - 1)].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank - 1)][0].lower() != 'b':
            storeboard[chr(ord(file) - 1) + str(rank - 1)].append(piece)
    except Exception:
        pass
    return storeboard

# protection functions for protdict
def wpawnprot(board, protdict, piece, file, rank):
    try:
        if board[chr(ord(file) + 1) + str(rank + 1)][0].lower() == 'w':
            protdict[board[chr(ord(file) + 1) + str(rank + 1)][0:3]].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank + 1)][0].lower() == 'w':
            protdict[board[chr(ord(file) - 1) + str(rank + 1)][0:3]].append(piece)
    except Exception:
        pass
    return protdict


def bpawnprot(board, protdict, piece, file, rank):
    try:
        if board[chr(ord(file) + 1) + str(rank - 1)][0].lower() == 'b':
            protdict[board[chr(ord(file) + 1) + str(rank - 1)][0:3]].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank - 1)][0].lower() == 'b':
            protdict[board[chr(ord(file) - 1) + str(rank - 1)][0:3]].append(piece)
    except Exception:
        pass
    return protdict


def knightprot(board, protdict, piece, file, rank):
    try:
        if board[chr(ord(file) + 1) + str(rank + 2)][0].lower() == piece[0].lower():
            protdict[board[chr(ord(file) + 1) + str(rank + 2)][0:3]].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank + 2)][0].lower() == piece[0].lower():
            protdict[board[chr(ord(file) - 1) + str(rank + 2)][0:3]].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 1) + str(rank - 2)][0].lower() == piece[0].lower():
            protdict[board[chr(ord(file) + 1) + str(rank - 2)][0:3]].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank - 2)][0].lower() == piece[0].lower():
            protdict[board[chr(ord(file) - 1) + str(rank - 2)][0:3]].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 2) + str(rank + 1)][0].lower() == piece[0].lower():
            protdict[board[chr(ord(file) + 2) + str(rank + 1)][0:3]].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 2) + str(rank + 1)][0].lower() == piece[0].lower():
            protdict[board[chr(ord(file) - 2) + str(rank + 1)][0:3]].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 2) + str(rank - 1)][0].lower() == piece[0].lower():
            protdict[board[chr(ord(file) + 2) + str(rank - 1)][0:3]].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 2) + str(rank - 1)][0].lower() == piece[0].lower():
            protdict[board[chr(ord(file) - 2) + str(rank - 1)][0:3]].append(piece)
    except Exception:
        pass
    return protdict


def wrookprot(board, protdict, piece, file, rank):
    # mccabe cyclomatic complexity, please have mercy on my code
    x = file
    y = int(rank)
    up = 8 - y
    down = y - 1
    right = 104 - ord(x)
    left = ord(x) - 97
    # up
    if up != 0:
        for i in range(1, up + 1):
            if board[file + str(rank + i)].lower() != '  ':
                if board[file + str(rank + i)][0].lower() == 'b':
                    break
                elif board[file + str(rank + i)][0].lower() == 'w':
                    protdict[board[file + str(rank + i)][0:3]].append(piece)
                    break
    # down
    if down != 0:
        for i in range(1, down + 1):
            if board[file + str(rank - i)].lower() != '  ':
                if board[file + str(rank - i)][0].lower() == 'b':
                    break
                elif board[file + str(rank - i)][0].lower() == 'w':
                    protdict[board[file + str(rank - i)][0:3]].append(piece)
                    break
    # right
    if right != 0:
        for i in range(1, right + 1):
            if board[chr(ord(file) + i) + str(rank)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) + i) + str(rank)][0].lower() == 'w':
                    protdict[board[chr(ord(file) + i) + str(rank)][0:3]].append(piece)
                    break
    # left
    if left != 0:
        for i in range(1, left + 1):
            if board[chr(ord(file) - i) + str(rank)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) - i) + str(rank)][0].lower() == 'w':
                    protdict[board[chr(ord(file) - i) + str(rank)][0:3]].append(piece)
                    break
    return protdict


def brookprot(board, protdict, piece, file, rank):
    # mccabe cyclomatic complexity, please have mercy on my code
    x = file
    y = int(rank)
    up = 8 - y
    down = y - 1
    right = 104 - ord(x)
    left = ord(x) - 97
    # up
    if up != 0:
        for i in range(1, up + 1):
            if board[file + str(rank + i)].lower() != '  ':
                if board[file + str(rank + i)][0].lower() == 'w':
                    break
                elif board[file + str(rank + i)][0].lower() == 'b':
                    protdict[board[file + str(rank + i)][0:3]].append(piece)
                    break
    # down
    if down != 0:
        for i in range(1, down + 1):
            if board[file + str(rank - i)].lower() != '  ':
                if board[file + str(rank - i)][0].lower() == 'w':
                    break
                elif board[file + str(rank - i)][0].lower() == 'b':
                    protdict[board[file + str(rank - i)][0:3]].append(piece)
                    break
    # right
    if right != 0:
        for i in range(1, right + 1):
            if board[chr(ord(file) + i) + str(rank)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) + i) + str(rank)][0].lower() == 'b':
                    protdict[board[chr(ord(file) + i) + str(rank)][0:3]].append(piece)
                    break
    # left
    if left != 0:
        for i in range(1, left + 1):
            if board[chr(ord(file) - i) + str(rank)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) - i) + str(rank)][0].lower() == 'b':
                    protdict[board[chr(ord(file) - i) + str(rank)][0:3]].append(piece)
                    break
    return protdict


def wbishopprot(board, protdict, piece, file, rank):
    # mccabe cyclomatic complexity, please have mercy on my code
    x = file
    y = int(rank)
    up = 8 - y
    down = y - 1
    right = 104 - ord(x)
    left = ord(x) - 97
    # up and to the left
    if up != 0 and left != 0:
        if up > left:
            displacement = left
        elif up < left:
            displacement = up
        else:
            displacement = left
        for i in range(1, displacement + 1):
            if board[chr(ord(file) - i) + str(rank + i)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank + i)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) - i) + str(rank + i)][0].lower() == 'w':
                    protdict[board[chr(ord(file) - i) + str(rank + i)][0:3]].append(piece)
                    break
    # down and to the left
    if down != 0 and left != 0:
        if down > left:
            displacement = left
        elif down < left:
            displacement = down
        else:
            displacement = left
        for i in range(1, displacement + 1):
            if board[chr(ord(file) - i) + str(rank - i)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank - i)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) - i) + str(rank - i)][0].lower() == 'w':
                    protdict[board[chr(ord(file) - i) + str(rank - i)][0:3]].append(piece)
                    break
    # up and to the right
    if up != 0 and right != 0:
        if up > right:
            displacement = right
        elif up < right:
            displacement = up
        else:
            displacement = right
        for i in range(1, displacement + 1):
            if board[chr(ord(file) + i) + str(rank + i)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank + i)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) + i) + str(rank + i)][0].lower() == 'w':
                    protdict[board[chr(ord(file) + i) + str(rank + i)][0:3]].append(piece)
                    break
    # down and to the right
    if down != 0 and right != 0:
        if down > right:
            displacement = right
        elif down < right:
            displacement = down
        else:
            displacement = right
        for i in range(1, displacement + 1):
            if board[chr(ord(file) + i) + str(rank - i)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank - i)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) + i) + str(rank - i)][0].lower() == 'w':
                    protdict[board[chr(ord(file) + i) + str(rank - i)][0:3]].append(piece)

    return protdict


def bbishopprot(board, protdict, piece, file, rank):
    # mccabe cyclomatic complexity, please have mercy on my code
    x = file
    y = int(rank)
    up = 8 - y
    down = y - 1
    right = 104 - ord(x)
    left = ord(x) - 97
    # up and to the left
    if up != 0 and left != 0:
        if up > left:
            displacement = left
        elif up < left:
            displacement = up
        else:
            displacement = left
        for i in range(1, displacement + 1):
            if board[chr(ord(file) - i) + str(rank + i)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank + i)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) - i) + str(rank + i)][0].lower() == 'b':
                    protdict[board[chr(ord(file) - i) + str(rank + i)][0:3]].append(piece)
                    break
    # down and to the left
    if down != 0 and left != 0:
        if down > left:
            displacement = left
        elif down < left:
            displacement = down
        else:
            displacement = left
        for i in range(1, displacement + 1):
            if board[chr(ord(file) - i) + str(rank - i)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank - i)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) - i) + str(rank - i)][0].lower() == 'b':
                    protdict[board[chr(ord(file) - i) + str(rank - i)][0:3]].append(piece)
                    break
    # up and to the right
    if up != 0 and right != 0:
        if up > right:
            displacement = right
        elif up < right:
            displacement = up
        else:
            displacement = right
        for i in range(1, displacement + 1):
            if board[chr(ord(file) + i) + str(rank + i)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank + i)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) + i) + str(rank + i)][0].lower() == 'b':
                    protdict[board[chr(ord(file) + i) + str(rank + i)][0:3]].append(piece)
                    break
    # down and to the right
    if down != 0 and right != 0:
        if down > right:
            displacement = right
        elif down < right:
            displacement = down
        else:
            displacement = right
        for i in range(1, displacement + 1):
            if board[chr(ord(file) + i) + str(rank - i)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank - i)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) + i) + str(rank - i)][0].lower() == 'b':
                    protdict[board[chr(ord(file) + i) + str(rank - i)][0:3]].append(piece)
                    break
    return protdict


def wqueenprot(board, protdict, piece, file, rank):
    # mccabe cyclomatic complexity, please have mercy on my code
    x = file
    y = int(rank)
    up = 8 - y
    down = y - 1
    right = 104 - ord(x)
    left = ord(x) - 97
    # up
    if up != 0:
        for i in range(1, up + 1):
            if board[file + str(rank + i)].lower() != '  ':
                if board[file + str(rank + i)][0].lower() == 'b':
                    break
                elif board[file + str(rank + i)][0].lower() == 'w':
                    protdict[board[file + str(rank + i)][0:3]].append(piece)
                    break
    # down
    if down != 0:
        for i in range(1, down + 1):
            if board[file + str(rank - i)].lower() != '  ':
                if board[file + str(rank - i)][0].lower() == 'b':
                    break
                elif board[file + str(rank - i)][0].lower() == 'w':
                    protdict[board[file + str(rank - i)][0:3]].append(piece)
                    break
    # right
    if right != 0:
        for i in range(1, right + 1):
            if board[chr(ord(file) + i) + str(rank)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) + i) + str(rank)][0].lower() == 'w':
                    protdict[board[chr(ord(file) + i) + str(rank)][0:3]].append(piece)
                    break
    # left
    if left != 0:
        for i in range(1, left + 1):
            if board[chr(ord(file) - i) + str(rank)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) - i) + str(rank)][0].lower() == 'w':
                    protdict[board[chr(ord(file) - i) + str(rank)][0:3]].append(piece)
                    break
    # up and to the left
    if up != 0 and left != 0:
        if up > left:
            displacement = left
        elif up < left:
            displacement = up
        else:
            displacement = left
        for i in range(1, displacement + 1):
            if board[chr(ord(file) - i) + str(rank + i)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank + i)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) - i) + str(rank + i)][0].lower() == 'w':
                    protdict[board[chr(ord(file) - i) + str(rank + i)][0:3]].append(piece)
                    break
    # down and to the left
    if down != 0 and left != 0:
        if down > left:
            displacement = left
        elif down < left:
            displacement = down
        else:
            displacement = left
        for i in range(1, displacement + 1):
            if board[chr(ord(file) - i) + str(rank - i)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank - i)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) - i) + str(rank - i)][0].lower() == 'w':
                    protdict[board[chr(ord(file) - i) + str(rank - i)][0:3]].append(piece)
                    break
    # up and to the right
    if up != 0 and right != 0:
        if up > right:
            displacement = right
        elif up < right:
            displacement = up
        else:
            displacement = right
        for i in range(1, displacement + 1):
            if board[chr(ord(file) + i) + str(rank + i)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank + i)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) + i) + str(rank + i)][0].lower() == 'w':
                    protdict[board[chr(ord(file) + i) + str(rank + i)][0:3]].append(piece)
                    break
    # down and to the right
    if down != 0 and right != 0:
        if down > right:
            displacement = right
        elif down < right:
            displacement = down
        else:
            displacement = right
        for i in range(1, displacement + 1):
            if board[chr(ord(file) + i) + str(rank - i)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank - i)][0].lower() == 'b':
                    break
                elif board[chr(ord(file) + i) + str(rank - i)][0].lower() == 'w':
                    protdict[board[chr(ord(file) + i) + str(rank - i)][0:3]].append(piece)
                    break
    return protdict


def bqueenprot(board, protdict, piece, file, rank):
    # mccabe cyclomatic complexity, please have mercy on my code
    x = file
    y = int(rank)
    up = 8 - y
    down = y - 1
    right = 104 - ord(x)
    left = ord(x) - 97
    # up
    if up != 0:
        for i in range(1, up + 1):
            if board[file + str(rank + i)].lower() != '  ':
                if board[file + str(rank + i)][0].lower() == 'w':
                    break
                elif board[file + str(rank + i)][0].lower() == 'b':
                    protdict[board[file + str(rank + i)][0:3]].append(piece)
                    break
    # down
    if down != 0:
        for i in range(1, down + 1):
            if board[file + str(rank - i)].lower() != '  ':
                if board[file + str(rank - i)][0].lower() == 'w':
                    break
                elif board[file + str(rank - i)][0].lower() == 'b':
                    protdict[board[file + str(rank - i)][0:3]].append(piece)
                    break
    # right
    if right != 0:
        for i in range(1, right + 1):
            if board[chr(ord(file) + i) + str(rank)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) + i) + str(rank)][0].lower() == 'b':
                    protdict[board[chr(ord(file) + i) + str(rank)][0:3]].append(piece)
                    break
    # left
    if left != 0:
        for i in range(1, left + 1):
            if board[chr(ord(file) - i) + str(rank)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) - i) + str(rank)][0].lower() == 'b':
                    protdict[board[chr(ord(file) - i) + str(rank)][0:3]].append(piece)
                    break
    # up and to the left
    if up != 0 and left != 0:
        if up > left:
            displacement = left
        elif up < left:
            displacement = up
        else:
            displacement = left
        for i in range(1, displacement + 1):
            if board[chr(ord(file) - i) + str(rank + i)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank + i)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) - i) + str(rank + i)][0].lower() == 'b':
                    protdict[board[chr(ord(file) - i) + str(rank + i)][0:3]].append(piece)
                    break
    # down and to the left
    if down != 0 and left != 0:
        if down > left:
            displacement = left
        elif down < left:
            displacement = down
        else:
            displacement = left
        for i in range(1, displacement + 1):
            if board[chr(ord(file) - i) + str(rank - i)].lower() != '  ':
                if board[chr(ord(file) - i) + str(rank - i)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) - i) + str(rank - i)][0].lower() == 'b':
                    protdict[board[chr(ord(file) - i) + str(rank - i)][0:3]].append(piece)
                    break
    # up and to the right
    if up != 0 and right != 0:
        if up > right:
            displacement = right
        elif up < right:
            displacement = up
        else:
            displacement = right
        for i in range(1, displacement + 1):
            if board[chr(ord(file) + i) + str(rank + i)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank + i)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) + i) + str(rank + i)][0].lower() == 'b':
                    protdict[board[chr(ord(file) + i) + str(rank + i)][0:3]].append(piece)
                    break
    # down and to the right
    if down != 0 and right != 0:
        if down > right:
            displacement = right
        elif down < right:
            displacement = down
        else:
            displacement = right
        for i in range(1, displacement + 1):
            if board[chr(ord(file) + i) + str(rank - i)].lower() != '  ':
                if board[chr(ord(file) + i) + str(rank - i)][0].lower() == 'w':
                    break
                elif board[chr(ord(file) + i) + str(rank - i)][0].lower() == 'b':
                    protdict[board[chr(ord(file) + i) + str(rank - i)][0:3]].append(piece)
                    break
    return protdict


def kingprot(board, protdict, piece, file, rank, storeboard):
    try:
        if board[file + str(rank + 1)][0].lower() == piece[0].lower():
            for i in storeboard[file + str(rank + 1)]:
                if i[0].lower() != piece[0].lower():
                    raise Exception("Exception")
            protdict[board[file + str(rank + 1)]].append(piece)
    except Exception:
        pass
    try:
        if board[file + str(rank - 1)][0].lower() == piece[0].lower():
            for i in storeboard[file + str(rank - 1)]:
                if i[0].lower() != piece[0].lower():
                    raise Exception("Exception")
            protdict[board[file + str(rank - 1)]].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 1) + str(rank)][0].lower() == piece[0].lower():
            for i in storeboard[chr(ord(file) + 1) + str(rank)]:
                if i[0].lower() != piece[0].lower():
                    raise Exception("Exception")
            protdict[board[chr(ord(file) + 1) + str(rank)]].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank)][0].lower() == piece[0].lower():
            for i in storeboard[chr(ord(file) - 1) + str(rank)]:
                if i[0].lower() != piece[0].lower():
                    raise Exception("Exception")
            protdict[board[chr(ord(file) - 1) + str(rank)]].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 1) + str(rank + 1)][0].lower() == piece[0].lower():
            for i in storeboard[chr(ord(file) + 1) + str(rank + 1)]:
                if i[0].lower() != piece[0].lower():
                    raise Exception("Exception")
            protdict[board[chr(ord(file) + 1) + str(rank + 1)]].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank + 1)][0].lower() == piece[0].lower():
            for i in storeboard[chr(ord(file) - 1) + str(rank + 1)]:
                if i[0].lower() != piece[0].lower():
                    raise Exception("Exception")
            protdict[board[chr(ord(file) - 1) + str(rank + 1)]].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) + 1) + str(rank - 1)][0].lower() == piece[0].lower():
            for i in storeboard[chr(ord(file) + 1) + str(rank - 1)]:
                if i[0].lower() != piece[0].lower():
                    raise Exception("Exception")
            protdict[board[chr(ord(file) + 1) + str(rank - 1)]].append(piece)
    except Exception:
        pass
    try:
        if board[chr(ord(file) - 1) + str(rank - 1)][0].lower() == piece[0].lower():
            for i in storeboard[chr(ord(file) - 1) + str(rank - 1)]:
                if i[0].lower() != piece[0].lower():
                    raise Exception("Exception")
            protdict[board[chr(ord(file) - 1) + str(rank - 1)]].append(piece)
    except Exception:
        pass
    return protdict

# Tester Code
if __name__ == "__main__":
    piece = "WB2"
    board = {"a8": "  ", "b8": "BR1n", "c8": "BB1", "d8": "BQ1", "e8": "BK1n", "f8": "BB2", "g8": "  ", "h8": "BR2n", 
             "a7": "bp1", "b7": "  ", "c7": "bp3", "d7": "bp4", "e7": "  ", "f7": "bp6", "g7": "bp7", "h7": "bp8", 
             "a6": "  ", "b6": "  ", "c6": "  ", "d6": "  ", "e6": "  ", "f6": "BN2", "g6": "  ", "h6": "  ", 
             "a5": "  ", "b5": "bp2", "c5": "  ", "d5": "WB2", "e5": "bp5", "f5": "  ", "g5": "  ", "h5": "  ", 
             "a4": "  ", "b4": "BN1", "c4": "  ", "d4": "  ", "e4": "wp5", "f4": "  ", "g4": "  ", "h4": "  ", 
             "a3": "  ", "b3": "  ", "c3": "  ", "d3": "wp4", "e3": "  ", "f3": "WN2", "g3": "  ", "h3": "  ", 
             "a2": "wp1", "b2": "wp2", "c2": "wp3", "d2": "  ", "e2": "  ", "f2": "wp6", "g2": "wp7", "h2": "wp8", 
             "a1": "WR1n", "b1": "WN1", "c1": "WB1", "d1": "WQ1", "e1": "  ", "f1": "WR2", "g1": "WK1", "h1": "  "}

    chesspiece = ChessPiece(board, piece)

    print(f"A {chesspiece.piecename} with the designation {piece} is on {chesspiece.space}")
    print(f"It is attacking {chesspiece.attacking} while defending {chesspiece.defending}")
    print(f"It is being attacked by {chesspiece.attacked_by} while being defended by {chesspiece.defended_by}")
    print(f"The value of a {chesspiece.piecename} is {chesspiece.value}")
