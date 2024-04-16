# leetcode problem no. 649(Medium )

class Solution:
    def predictPartyVictory(self, senate: str) -> str: 
        senate = list(senate)
        r_q, d_q = deque(), deque()  
        visited = [] 

        for i, voter in enumerate(senate):
            if voter == 'R':
                r_q.append(i) 
            else:
                d_q.append(i) 
        
        while r_q and d_q: 
            rTurn = r_q.popleft()
            dTurn = d_q.popleft() 

            if rTurn < dTurn:
                r_q.append(dTurn + len(senate))
            else:
                d_q.append(rTurn + len(senate))

        return "Radiant" if r_q else "Dire" 