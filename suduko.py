def row_unused_digit(grid, valid_digit, i):
    for k in range(9):
        if grid[i][k] > 0:
            valid_digit[grid[i][k] - 1] = 0

def col_unused_digit(grid,valid_digit,j):
    for k in range(9):
        if grid[k][j] > 0:
            valid_digit[grid[k][j] - 1] = 0
            
def block_unused_digit(grid, valid_digit, i, j):
    
    
    if i < 3:
        
        if j < 3:
            
            for m in range(3):
                for n in range(3):
                    if grid[m][n] > 0:
                        valid_digit[grid[m][n] - 1] = 0   
        elif j < 6:
            for m in range(3):
                for n in range(3,6):
                    if grid[m][n] > 0:
                        valid_digit[grid[m][n] - 1] = 0  
        else:
            for m in range(3):
                for n in range(6,9):
                    if grid[m][n] > 0:
                        valid_digit[grid[m][n] - 1] = 0  
            
        
    elif i < 6:
        
        if j < 3:
            
            for m in range(3,6):
                for n in range(3):
                    if grid[m][n] > 0:
                        valid_digit[grid[m][n] - 1] = 0 
            
        elif j < 6:
            
            for m in range(3,6):
                for n in range(3,6):
                    if grid[m][n] > 0:
                        valid_digit[grid[m][n] - 1] = 0 
            
        else:
            
            for m in range(3,6):
                for n in range(6,9):
                    if grid[m][n] > 0:
                        valid_digit[grid[m][n] - 1] = 0
        
    else:
        
        if j < 3:
            
             for m in range(6,9):
                for n in range(3):
                    if grid[m][n] > 0:
                        valid_digit[grid[m][n] - 1] = 0
            
        elif j < 6:
            
             for m in range(6,9):
                for n in range(3,6):
                    if grid[m][n] > 0:
                        valid_digit[grid[m][n] - 1] = 0
            
        else:
            
             for m in range(6,9):
                for n in range(6,9):
                    if grid[m][n] > 0:
                        valid_digit[grid[m][n] - 1] = 0 
    
    
def possible_number(grid, i, j):
    possibleN = [1,1,1,1,1,1,1,1,1] 
    row_unused_digit(grid,possibleN,i)          
    col_unused_digit(grid,possibleN,j)
    block_unused_digit(grid,possibleN,i,j)
    resultPossibleN = []
    for r in range(9):
        if possibleN[r] ==1:
            resultPossibleN.append(r+1)
    return resultPossibleN


def best_cell(grid):
    countV = 0
    listToReturn = []
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                countV = countV + 1
                possibleN = [1,1,1,1,1,1,1,1,1] 
                row_unused_digit(grid,possibleN,r)          
                col_unused_digit(grid,possibleN,c)
                block_unused_digit(grid,possibleN,r,c) 
                numberOfOnes = possibleN.count(1)
                
                if countV == 1:
                    
                    SmallestNumberOfOne = possibleN.count(1)
                    listToReturn = [r,c,possibleN]
                    if SmallestNumberOfOne == 1:
                        return listToReturn
                    
                else:
                    
                    if SmallestNumberOfOne > numberOfOnes:
                        
                        SmallestNumberOfOne = numberOfOnes
                        listToReturn = [r,c,possibleN]
                        if SmallestNumberOfOne == 1:
                            return listToReturn
                        
    return listToReturn


def solve_sudoku(grid):
    
    updateList = best_cell(grid)    
    if len(updateList) != 0:
        for m in range(9):              
            if updateList[2][m] == 1:
                
                grid[updateList[0]][updateList[1]] = m + 1
                
                solve_sudoku(grid)
                
    return grid
   

        
        
        
grid_wiki =   [[5, 3, 0, 0, 7, 0, 0, 0, 0],
               [6, 0, 0, 1, 9, 5, 0, 0, 0],
               [0, 9, 8, 0, 0, 0, 0, 6, 0],
               [8, 0, 0, 0, 6, 0, 0, 0, 3],
               [4, 0, 0, 8, 0, 3, 0, 0, 1],
               [7, 0, 0, 0, 2, 0, 0, 0, 6],
               [0, 6, 0, 0, 0, 0, 2, 8, 0],
               [0, 0, 0, 4, 1, 9, 0, 0, 5],
               [0, 0, 0, 0, 8, 0, 0, 7, 9]]

FinalGrid = solve_sudoku(grid_wiki)
def Print_Board(FinalGrid):

    print("\n-------------------------")

    for i in range(9):
        for j in range(9):
            if FinalGrid[i][j] is not None:
                if j == 0:
                    print("|", end=" ")
                print(f"{FinalGrid[i][j]} ", end="")
            if (j + 1) % 3 == 0:
                print("|", end=" ")
        if (i + 1) % 3 == 0:
            print("\n-------------------------", end=" ")
        print()
print(Print_Board(FinalGrid))

best_cell(grid_wiki)

possible_number(grid_wiki,2,3)