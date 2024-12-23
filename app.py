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

@app.route('/api/sudoku/validate', methods=['POST'])
def validate_puzzle():
    try:
        data = request.get_json()
        grid = data.get('grid')
    
        # Perform validation logic
        is_valid, message, solution = sudoku_generator.checkUserBoard(grid)
        sudoku_generator.printBoard()
        print(is_valid, message, solution)
        return jsonify({
            'success': is_valid,
            'message': message,
            'solution': solution if is_valid else None
        }), 200

    except Exception as e:
        return jsonify({
            'error': str(e),
            'message': 'Failed to validate puzzle'
        }), 500


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8080)
