class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def santhu(l1,l2):
            ls=[]
            for i in l1:
                for j in l2:
                    ls.append(i+j)
            return ls
        ls=['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        res=[""]
        for i in range(len(digits)-1,-1,-1):
            res=santhu(ls[int(digits[i])-2],res)
        return res if res[0]!="" else []

