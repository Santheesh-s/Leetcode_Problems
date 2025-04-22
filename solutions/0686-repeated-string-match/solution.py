class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        rep = int(math.ceil(len(b) / float(len(a))))
        if b in a*rep: return rep
        elif b in a*(rep+1): return rep+1
        return -1; 
