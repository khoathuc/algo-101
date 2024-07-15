# Naive
- starting point choose the position with value = word[0]
- consequence index(i) choose from the adjacent positions(that has value equal to word[i])
- if can not find the next position, return and try new position of index i - 1


board, word.

board[i][j]: value of board at index i.
visited[i][j]: return true if board[i][j] was visited.

r: number of rows in board
c: number of columns in board

code: 
    
    backtrack(index, i, j):
        //check condition.
        if(board[i][j] != word[index]):
            return 
        
        if(i < 0 or j <0 or i > r-1 or j > c-1):
            return 

        if(visited[i][j]):
            return 

        //check if reach the end of word
        if(index == n):
            return True

        //if not, record that this position was visited and doing the backtrack with adjacent positions and index = index + 1
        visited[i][j] = true
        
        res = (
            backtrack(index + 1, i + 1, j) or 
            backtrack(index + 1, i, j + 1) or 
            backtrack(index + 1, i - 1, j) or 
            backtrack(index + 1, i, j - 1)
        )

        visited[i][j] = false
        
        return res
        


        