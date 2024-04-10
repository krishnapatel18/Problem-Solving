# leetcode problem no. 1431(Easy )

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_ = max(candies)
        result = [True] * len(candies)

        for i, candy in enumerate(candies):
            if candy + extraCandies < max_:
                result[i] = False  
                  
        return result 