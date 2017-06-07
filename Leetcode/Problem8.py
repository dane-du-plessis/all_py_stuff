class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = str
        i = 0
        res = []
        
        # trivial case
        if len(s) == 0:
            return 0
        
        # burn through whitespace
        while(s[i] == ' '):
            i += 1
            
        # take a + or - into account
        if s[i] == '+' or s[i] == '-':
            res.append(s[i])
            if i+1 == len(s): return 0
            i += 1
            
        if not Solution.isint(self, s[i]):
            print('Invalid String, returning empty list.')
            return 0
            
        # read the rest of the integer value from string, stop at non-int
        while(Solution.isint(self, s[i])):
            res.append(s[i])
            i += 1
            if i+1 > len(s): break
        
        #return the int
        r= int(''.join(res))
        if r > (2**31-1):
            return 2**31-1
        if r < (-2**31):
            return (-2**31)
            
        return r
        
    def isint(self, c):
        '''
        Return True only if c is an integral value
        '''
        for a in range(0,10):
            if str(a) == c: return True
        return False
"""
++++++++++++++++++++++++++++++++++++++++
"""

s = Solution()
r = s.myAtoi('')
print(r)

r = s.myAtoi('+')
print(r)


r = s.myAtoi('-1')
print(r)

r = s.myAtoi('+1')
print(r)

r = s.myAtoi('         +')
print(r)

r = s.myAtoi('         + 123   ')
print(r)

r = s.myAtoi('-12 +12 ')
print(r)

r = s.myAtoi(' ab +97')
print(r)

r = s.myAtoi(' -23 12 sdf')
print(r)










