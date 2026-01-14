from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Initialize empty board
board = [""] * 9
current_player = "X"

def check_winner():
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]
    if "" not in board:
        return "Draw"
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    global current_player
    data = request.get_json()
    idx = data.get('index')

    if board[idx] == "":
        board[idx] = current_player
        winner = check_winner()
        if winner:
            response = {'board': board, 'winner': winner}
            board[:] = [""] * 9  # reset for next game
        else:
            current_player = "O" if current_player == "X" else "X"
            response = {'board': board, 'winner': None}
        return jsonify(response)
    else:
        return jsonify({'error': 'Invalid move'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

