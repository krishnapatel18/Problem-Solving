# leetcode problem no. 79(Medium )

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        len_of_board = len(board)
        len_of_row = len(board[0])

        if len(word) > len_of_board * len_of_row:
            return False

        count = Counter(sum(board, []))

        for character, wordCount in Counter(word).items():
            if count[character] < wordCount:
                return False
        
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        visited = set()

        def dfs(lb, lr, i):
            if i == len(word):
                return True
            
            if lb < 0 or lr < 0 or lb >= len_of_board or lr >= len_of_row or word[i] != board[lb][lr] or (lb, lr) in visited:
                return False
            
            visited.add((lb, lr))

            res = (
                dfs(lb + 1, lr, i + 1) or 
                dfs(lb - 1, lr, i + 1) or 
                dfs(lb, lr + 1, i + 1) or 
                dfs(lb, lr - 1, i + 1) 
            )

            visited.remove((lb, lr))

            return res 

        for i in range(len_of_board):
            for j in range(len_of_row):
                if dfs(i, j, 0):
                    return True 
        return False 