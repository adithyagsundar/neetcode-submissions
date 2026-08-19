class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        use a hashset to check for duplicates
        for rows and columns its pretty simple, just add to the hashset during each iteraiton if not already in the hashset
        for the squares, use the equation r // 3, c // 3 as the key for the hashmap. because that will alwyas give you the INDEX of whatveer square you want. from there, check within the square. each square is a key in the hashmap
        """



        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": #occupied spaces only
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3, c // 3)]: #use a tuple pair in squares to access the values
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True
                