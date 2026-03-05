class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Base cases
        if n <= 2:
            return n
        
        # dp approach (Fibonacci)
        a, b = 1, 2  # ways for step 1 and step 2
        
        for _ in range(3, n + 1):
            a, b = b, a + b
        
        return b