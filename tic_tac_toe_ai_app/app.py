from flask import Flask, render_template, request, jsonify
from game.ai import get_ai_move
from game.logic import check_winner, is_draw

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/move", methods=["POST"])
def move():
    data = request.json
    board = data["board"]
    difficulty = data["difficulty"]

    ai_move = get_ai_move(board, difficulty)
    board[ai_move] = "O"

    winner = check_winner(board)
    draw = is_draw(board)

    return jsonify({"move": ai_move, "winner": winner, "draw": draw})

if __name__ == "__main__":
    app.run(debug=True)
