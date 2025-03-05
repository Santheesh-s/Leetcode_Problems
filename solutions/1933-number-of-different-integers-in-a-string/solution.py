class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        ls=set()
        ls.add("")
        n=len(word)
        s=""
        for i in range(0,n):
            if word[i].isdigit():
                s+=word[i]
            else:
                if s!="" and str(int(s))=='0':
                    ls.add(str(int(s)))
                else:
                    ls.add(s.lstrip('0'))
                s=""
        if s!="" and str(int(s))=='0':
            ls.add(str(int(s)))
        else:
            ls.add(s.lstrip('0'))
        return len(ls)-1
