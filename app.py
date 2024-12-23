import time
from flask import Flask, jsonify, request
from flask_cors import CORS
from SudokuGenerator import SudokuGenerator
from SudokuSolver import Solver

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
    
@app.route('/api/sudoku/solve-steps', methods=['POST'])
def solve_puzzle():
    try:
        data = request.get_json()
        grid = data.get('grid')
        
        # Solve the puzzle
        solver = Solver(grid)
        start_time = time.time()
        solved_board, steps = solver.solve()
        end_time = time.time()
        time_taken = end_time - start_time

        if solved_board:
            return jsonify({
                'time_taken': time_taken,
                'steps': steps,
            }), 200
        else:
            return jsonify({
                'error': 'Failed to solve the puzzle'
            }), 500

    except Exception as e:
        return jsonify({
            'error': str(e),
            'message': 'Failed to solve puzzle'
        }), 500


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8080)
