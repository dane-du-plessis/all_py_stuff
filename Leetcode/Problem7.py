class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT32_MAX = (2**31)-1
        INT32_MIN = -(2**31)
        
        # temp var
        t = x
        # magnitude var
        magnitude = 0
        # result var
        r = 0
        
        # negative case
        if t < 0: t = -t
        
        #determine magnitude of x
        if t > 0: magnitude = 1
        while(t>0):
            t = t/10
            if t > 0: magnitude += 1
        print('m =', magnitude)
        
        # reset temp var
        t = x
        if t < 0: t = -t
        
        # build new int
        for i in range(0,magnitude):
            r += (t%10)*10**(magnitude - i-1)
            print('i = ', i, 'r = ',r)
            t /= 10
            
        # apply correct sign
        if x < 0: r = -r
        
        # r too big?
        if r > INT32_MAX or r < INT32_MIN:
            return 0
        else:
            return r
            
