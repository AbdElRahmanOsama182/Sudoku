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
            domainXbefore = domains[x].copy()

            if self.revise(x, y, domains):
                if(domainXbefore != domains[x]):
                    with open('algorithms.log', 'a') as log_file:
                            log_file.write(f"Domain before revision (x={x}): {domainXbefore.get_domain()}\n")
                            log_file.write(f"Domain after revision (x={x}): {domains[x].get_domain()}\n")
                            log_file.write(f"Domain of y (y={y}): {domains[y].get_domain()}\n")
                            log_file.write("="*50 + "\n")
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

    def validateSteps(self, board):
        # print(self.steps)
        for step in self.steps:
            for row, col, value in step:
                board[row][col] = value
        return True
    
    def solve(self):
        with open('algorithms.log', 'w') as log_file:
            log_file.write("")

        domainCopy = {key: v.copy() for key,v in self.domains.items()}
        self.ac3(self.domains)

        #just for getting steps
        for(k,v) in self.domains.items():
            if v.is_singleton() and not domainCopy[k].is_singleton():
                self.steps.append([(k[0],k[1], v.get_value())])

        return self.backtrackingSearch(self.domains), self.steps
