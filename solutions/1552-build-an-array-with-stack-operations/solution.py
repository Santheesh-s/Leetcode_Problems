class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        ss=[]
        ls=[]
        for i in range(1,n+1):
            if ss==target:
                return ls
            else:
                ls.append("Push")
                ss.append(i)
                if i not in target:
                    ls.append("Pop")
                    ss.remove(i)
        return ls
