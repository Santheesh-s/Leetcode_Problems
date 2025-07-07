class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ls1,ls2=[],[]
        for i in s:
            if i=='#' and len(ls1)>0:
                ls1.pop()
            elif i!='#':
                ls1.append(i)
        for i in t:
            if i=='#' and len(ls2)>0:
                ls2.pop()
            elif i!='#':
                ls2.append(i)
        print(ls1)
        print(ls2)
        return True if ls1==ls2 else False


