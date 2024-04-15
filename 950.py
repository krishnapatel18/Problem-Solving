# leetcode problem no. 950(Medium )

# Interview Tip: In-place Algorithms
# This approach sorts the deck in-place. In-place algorithms overwrite the input to save space, but sometimes this can cause problems.
# Here are a couple of situations where an in-place algorithm might not be suitable:
# The algorithm needs to run in a multi-threaded environment, without exclusive access to the array. Other threads might need to read the array too, and might not expect it to be modified.
# Even if there is only a single thread, or the algorithm has exclusive access to the array while running, the array might need to be reused later or by another thread once the lock has been released.
# In an interview, you should always check whether the interviewer minds you overwriting the input. Be ready to explain the pros and cons of doing so if asked!

# Two pointer technique[In place Algorithm ]
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        N = len(deck)
        result = [0] * N
        skip = False 
        index_inDeck, index_inResult = 0, 0 

        deck.sort()   
        while index_inDeck < N:
            if result[index_inResult] == 0:
                if not skip:
                    result[index_inResult] = deck[index_inDeck]
                    index_inDeck += 1 
                skip = not skip 
                    
            index_inResult = (index_inResult + 1) % N 

        return result  