from flask import Flask, jsonify, request
from flask_cors import CORS
from SudokuGenerator import SudokuGenerator

app = Flask(__name__)
CORS(app)
sudoku_generator = SudokuGenerator(debug=True)

@app.route('/api/sudoku/generate', methods=['POST'])
def generate_puzzle():
    try:
        data = request.get_json()
        difficulty = data.get('difficulty', 'Intermediate')
        sudoku_generator.generateSudoku(difficulty)
        return jsonify({
            'grid': sudoku_generator.board
        }), 200

    except Exception as e:
        return jsonify({
            'error': str(e),
            'message': 'Failed to generate puzzle'
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8080)
