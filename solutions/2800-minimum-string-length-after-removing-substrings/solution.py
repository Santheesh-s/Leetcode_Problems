class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(re(s))
    
def re(ss):
        if ('AB' in ss):
            return re(ss.replace('AB',""))
        elif ('CD' in ss):
            return re(ss.replace('CD',""))
        else:
            return ss
