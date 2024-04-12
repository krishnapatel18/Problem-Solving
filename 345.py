# leetcode problem no. 345(Easy )

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = 'aeiouAEIOU'
        new = []

        for char in s:
            if char in vowels:
                new.append(char)
            
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = new.pop()
        
        return ''.join(s)