from flask import Flask, Blueprint, render_template
from people import people_bp
from people.prep import people_prep_bp
from people.David import people_David_bp, davidminilab
from people.Brandon import people_Brandon_bp
from people.Kian import people_Kian_bp
from people.Gavin import people_Gavin_bp
from people.David.davidminilab import ChessPiece

app = Flask(__name__)
app.register_blueprint(people_bp, url_prefix='/people/repos')
app.register_blueprint(people_prep_bp, url_prefix='/people/prep')
app.register_blueprint(people_David_bp, url_prefix='/people/David')
app.register_blueprint(people_Brandon_bp, url_prefix='/people/Brandon')
app.register_blueprint(people_Kian_bp, url_prefix='/people/Kian')
app.register_blueprint(people_Gavin_bp, url_prefix='/people/Gavin')


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/itunes')
def itunes():
    return render_template("itunes.html")

@app.route('/soundcloud')
def soundcloud():
    return render_template("soundcloud.html")

@app.route('/spotify')
def spotify():
    return render_template("spotify.html")

@app.route('/minilab/david')
def david_minilab():
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
    allboard = [{}, {}, {}, {}, {}, {}, {}, {}]
    [[allboard[i].update({chr(k+97) + str(i+1):board[chr(k+97) + str(i+1)]}) for k in range(8)] for i in range(8)]
    return render_template("davidminilab.html", piece=piece, board=board, chesspiece=chesspiece)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404



if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True, port="5001")
