class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        c=0
        for i in words:
            n=chars
            for j in i:
                if j not in n:
                    break
                n=n.replace(j,"",1)
            else:
                c+=len(i)
        return c
