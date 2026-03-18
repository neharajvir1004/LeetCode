class Solution(object):
    def isMatch(self, s, p):
        s_ptr, p_ptr = 0, 0
        last_s_ptr, last_p_ptr = -1, -1
        
        while s_ptr < len(s):
            if p_ptr < len(p) and (p[p_ptr] == s[s_ptr] or p[p_ptr] == '?'):
                s_ptr += 1
                p_ptr += 1
            
            elif p_ptr < len(p) and p[p_ptr] == '*':
             
                last_p_ptr = p_ptr
                last_s_ptr = s_ptr
                p_ptr += 1
            
            elif last_p_ptr != -1:
           
                p_ptr = last_p_ptr + 1
                last_s_ptr += 1
                s_ptr = last_s_ptr
            
            else:
                return False
        
        return all(x == '*' for x in p[p_ptr:])