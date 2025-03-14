class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        n=sentence.split()
        n1=len(n)
        if n1==1:
            return n[0][0]==n[0][-1]
        if sentence[0]==sentence[-1]:
            for i in range(n1-1):
                if not n[i][-1]==n[i+1][0]:
                    return False
        else:
            return False
        return True
