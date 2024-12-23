import time
from SudokuGenerator import SudokuGenerator

def run_test(iterations=10):
    mrv_times = []
    no_mrv_times = []
    sudoku_mrv = SudokuGenerator("hard", mrv=True)
    sudoku_no_mrv = SudokuGenerator("hard")
    for _ in range(iterations):
        print(f"Iteration {_ + 1} of {iterations}")
        # Using MRV
        start_time = time.time()
        sudoku_mrv.generateSudoku()
        end_time = time.time()
        mrv_times.append(end_time - start_time)

        # Without MRV
        start_time = time.time()
        sudoku_no_mrv.generateSudoku()
        end_time = time.time()
        no_mrv_times.append(end_time - start_time)

    return mrv_times, no_mrv_times

if __name__ == '__main__':
    iterations = 10
    mrv_times, no_mrv_times = run_test(iterations)

    avg_mrv_time = sum(mrv_times) / iterations
    avg_no_mrv_time = sum(no_mrv_times) / iterations

    max_mrv_time = max(mrv_times)
    max_no_mrv_time = max(no_mrv_times)
    print(f"MRV average time: {avg_mrv_time:.4f} seconds")
    print(f"MRV max time: {max_mrv_time:.4f} seconds")
    print(f"Without MRV average time: {avg_no_mrv_time:.4f} seconds")
    print(f"Without MRV max time: {max_no_mrv_time:.4f} seconds")
    
