class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        ls=sentence.split()
        n=len(ls)
        for i in dictionary:
            for j in range(n):
                if i in ls[j][:len(i)]:
                    ls[j]=i
        return " ".join(ls)

