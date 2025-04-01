class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        s,ls=words[0],[]
        for i in s:
            for m,j in enumerate(words):
                if i in j:
                    words[m]=words[m].replace(i,"",1)
                if i not in j:
                    break
            else:
                ls.append(i)
        return ls

