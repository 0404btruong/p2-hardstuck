from flask import Blueprint, render_template, request
from people.David.davidminilab import ChessPiece

people_David_bp = Blueprint('people_David', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@people_David_bp.route('/')
def index():
    return render_template("course/timelines.html", padlet="https://padlet.com/jmortensen7/csptime1_2")

@people_David_bp.route('/minilab', methods=["GET", "POST"])
def david_minilab():
    if request.form:
        piece = request.form.get("chessPiece")
    else:
        piece = "WB2"
    board = {"a8": "  ", "b8": "BR1", "c8": "BB1", "d8": "BQ1", "e8": "BK1", "f8": "BB2", "g8": "  ", "h8": "BR2",
             "a7": "bp1", "b7": "  ", "c7": "bp3", "d7": "bp4", "e7": "  ", "f7": "bp6", "g7": "bp7", "h7": "bp8",
             "a6": "  ", "b6": "  ", "c6": "  ", "d6": "  ", "e6": "  ", "f6": "BN2", "g6": "  ", "h6": "  ",
             "a5": "  ", "b5": "bp2", "c5": "  ", "d5": "WB2", "e5": "bp5", "f5": "  ", "g5": "  ", "h5": "  ",
             "a4": "  ", "b4": "BN1", "c4": "  ", "d4": "  ", "e4": "wp5", "f4": "  ", "g4": "  ", "h4": "  ",
             "a3": "  ", "b3": "  ", "c3": "  ", "d3": "wp4", "e3": "  ", "f3": "WN2", "g3": "  ", "h3": "  ",
             "a2": "wp1", "b2": "wp2", "c2": "wp3", "d2": "  ", "e2": "  ", "f2": "wp6", "g2": "wp7", "h2": "wp8",
             "a1": "WR1", "b1": "WN1", "c1": "WB1", "d1": "WQ1", "e1": "  ", "f1": "WR2", "g1": "WK1", "h1": "  "}

    chesspiece = ChessPiece(board, piece)
    allboard = [{}, {}, {}, {}, {}, {}, {}, {}]
    text_to_unicode = {"WR":"♖ ", "WN":"♘ ", "WB":"♗ ", "WQ":"♕ ", "WK":"♔ ", "wp":"♙ ", "  ":"  ",
                       "BR":"♜ ", "BN":"♞ ", "BB":"♝ ", "BQ":"♛ ", "BK":"♚ ", "bp":"♟ "}
    [[allboard[i].update({chr(k+97) + str(i+1):text_to_unicode[board[chr(k+97) + str(i+1)][0:2]]}) for k in range(8)] for i in range(8)]

    '''for i in range(8):
        for k in range(8):
            allboard[i].update({chr(k+97) + str(i+1)})'''
    allboard.reverse()
    if request.form:
        return render_template("davidminilab.html", space=chesspiece.space, piece=piece, allboard=allboard, chesspiece=ChessPiece(board, piece))
    return render_template("davidminilab.html", space=chesspiece.space, piece=piece, allboard=allboard, chesspiece=chesspiece)
