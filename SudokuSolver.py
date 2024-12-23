from collections import deque
from Domain import Domain  
from SudokuGenerator import SudokuGenerator  

class Solver:
    def __init__(self, board):
        self.board = board
        self.domains = self.initializeDomains(board)
        self.neighbors = self.buildNeighbors()      
        self.steps = []
    @staticmethod
    def buildNeighbors():
        neighbors = {}
        for row in range(9):
            for col in range(9):
                cell = (row, col)
                neighbors[cell] = set()
                
                
                for i in range(9):
                    neighbors[cell].add((row, i))
                              
                for i in range(9):
                    neighbors[cell].add((i, col))
                
                subgridRow, subgridCol = row // 3 * 3, col // 3 * 3
                for i in range(subgridRow, subgridRow + 3):
                    for j in range(subgridCol, subgridCol + 3):
                        neighbors[cell].add((i, j))
                
                neighbors[cell].remove(cell)
        return neighbors

    def initializeDomains(self, board):
        domains = {}
        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:  
                    domains[(i, j)] = Domain(1 << (board[i][j] - 1))  
                else:
                    domains[(i, j)] = Domain()  
        return domains

    def reconstructBoard(self, domains):
        board = [[0 for _ in range(9)] for _ in range(9)]
        for (row, col), domain in domains.items():
            value = domain.get_value()
            if value:
                board[row][col] = value
        return board

    def revise(self, x, y, domains):
        revised = False
        xDomain = domains[x]
        yDomain = domains[y]
        for value in xDomain.get_domain():
            # check if any value in y's domain is different from x's value
            if not any(value != yValue for yValue in yDomain.get_domain()):  
                xDomain.remove(value)  
                revised = True
        return revised

    def ac3(self,domains):
        queue = deque()
        for cell1 in domains:
            for cell2 in self.neighbors[cell1]:
                queue.append((cell1, cell2))

        while queue:
            x, y = queue.popleft()
            if self.revise(x, y, domains):
                if domains[x].is_empty():  
                    return False
                for neighbor in self.neighbors[x]:
                    if neighbor != y:
                        queue.append((neighbor, x))
        return True

    def selectMinimumUnassigned(self, domains):
        return min((cell for cell in domains if not domains[cell].is_singleton()), 
                   key=lambda cell: len(domains[cell].get_domain()))

    def isComplete(self, domains):
        return all(domains[cell].is_singleton() for cell in domains)
    
    def printDomains(self, domains):
        for cell, domain in domains.items():
            print(cell, domain.get_domain())
            
    def backtrackingSearch(self, domains):

        if self.isComplete(domains):
            return self.reconstructBoard(domains)
        
        cell = self.selectMinimumUnassigned(domains)
       
        for value in domains[cell].get_domain():
            domainCopy = {key: v.copy() for key,v in domains.items()}
            domainCopy[cell] = Domain(1 << (value - 1))

            step =[]
            if self.ac3(domainCopy):
                added = False
                for k, v in domainCopy.items():
                    if v.is_singleton() and not domains[k].is_singleton():
                        step.append((k[0],k[1], v.get_value()))
                if(step):
                    added = True
                self.steps.append(step)
                result = self.backtrackingSearch(domainCopy)
                if result:
                    return result
                else:
                    if added:
                        self.steps.pop()
        return False  
    
    
    def isValidSudoku(self, board):
        def is_valid_group(group):
            # Check for numbers 1-9 only
            numbers = [num for num in group if num != 0]
            return len(numbers) == len(set(numbers)) and all(1 <= num <= 9 for num in numbers)
    
        # Check rows
        for row in board:
            if not is_valid_group(row):
                return False
        
        # Check columns
        for col in range(9):
            if not is_valid_group([board[row][col] for row in range(9)]):
                return False
        
        # Check subgrids
        for subgridRow in range(0, 9, 3):
            for subgridCol in range(0, 9, 3):
                subgrid = [board[row][col]
                        for row in range(subgridRow, subgridRow + 3)
                        for col in range(subgridCol, subgridCol + 3)]
                if not is_valid_group(subgrid):
                    return False
        
        # Check for complete board
        if not all(1 <= board[row][col] <= 9 for row in range(9) for col in range(9)):
            return False
        
        return True

    def validateSteps(self, board):
        for step in self.steps:
            for row, col, value in step:
                board[row][col] = value
            # print("Step:")
            # for row in board:
            #     print(row)

        return True
    
    def solve(self):
        domainCopy = {key: v.copy() for key,v in self.domains.items()}
        self.ac3(self.domains)

        #just for getting steps
        for(k,v) in self.domains.items():
            if v.is_singleton() and not domainCopy[k].is_singleton():
                self.steps.append([(k[0],k[1], v.get_value())])

        return self.backtrackingSearch(self.domains)
    
if __name__ == "__main__":
    for _ in range(10000):  # Run the solver 5 times
        generator = SudokuGenerator()
        board = generator.board
        # board = [
        #     [6, 1, 7, 4, 2, 3, 8, 5, 9],
        #     [5, 4, 8, 1, 7, 9, 3, 2, 6],
        #     [9, 3, 2, 0, 8, 0, 1, 0, 0],
        #     [1, 6, 0, 0, 5, 7, 0, 8, 0],
        #     [0, 7, 0, 0, 4, 0, 0, 1, 5],
        #     [4, 8, 5, 9, 6, 1, 2, 0, 0],
        #     [7, 5, 1, 0, 9, 0, 0, 0, 2],
        #     [8, 0, 6, 7, 3, 0, 5, 0, 1],
        #     [0, 0, 4, 0, 1, 0, 7, 0, 8]
        # ] 
      
        # print("Initial Board:")
        # for row in board:
        #     print(row)

        solver = Solver(board)
        solvedBoard = solver.solve()
        
        if solvedBoard:
            # print("Solved Board:")
            if  solver.isValidSudoku(solvedBoard):

                # print("steps")
                
                solver.validateSteps(board)
                if(board != solvedBoard):
                    print("steps are incorrect")

                # for(row) in board:
                #     print(row)
                # print("done")
            else:
                print("Initial Board:")
                # for row in board:
                #     print(row)
                print("Solved Board:")
                for row in solvedBoard:
                    print(row)
                print("The solution is invalid.")
                break
        else:
            print("Initial Board:")
            for row in board:
                print(row)
            print("The solution is invalid.")
        # print("="*30)