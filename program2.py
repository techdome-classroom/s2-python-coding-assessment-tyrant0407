class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }
        result=0
        prev_value=0
        for char in s:
            value=roman_map[char]
            if value>prev_value:
                
        pass



