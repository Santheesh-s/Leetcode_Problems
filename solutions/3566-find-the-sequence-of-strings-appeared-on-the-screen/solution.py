class Solution(object):
    def stringSequence(self, target):
        """
        :type target: str
        :rtype: List[str]
        """
        ls=[]
        l=""
        for i in target:
            l1=l
            for j in range(97,ord(i)+1):
                ls.append(l1+chr(j))
            l+=i
        return ls
