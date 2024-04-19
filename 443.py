# leetcode problem no. 443(Medium )

class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        len_res = 0

        while i < len(chars):
            group_length = 1
            while (i + group_length < len(chars) and chars[i + group_length] == chars[i]):
                group_length += 1
            chars[len_res] = chars[i]
            len_res += 1 

            if group_length > 1: 
                str_repr = str(group_length)
                chars[len_res:len_res + len(str_repr)] = list(str_repr)
                len_res += len(str_repr)
            
            i += group_length 

        return len_res