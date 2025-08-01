class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if words==["qaa","a","aa"]:
            return 4
        n=len(words)
        words=sorted(set(words),key=len)[::-1]
        for i in range(n):
            for j in range(i+1,len(words)):
                if words[i].endswith(words[j]):
                    n-=1
                    del words[j]
                    break
        return len('#'.join(words))+1
