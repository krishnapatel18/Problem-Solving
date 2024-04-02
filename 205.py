# leetcode problem no. 205(Easy )

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st = {}
        ht = {}
        
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in st:
                st[s[i]] = t[i]
            if t[i] not in ht:
                ht[t[i]] = s[i]
            if st[s[i]] != t[i] or ht[t[i]]!=s[i]: 
                return False
        return True