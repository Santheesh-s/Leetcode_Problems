class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        s=sentence.split()
        for i in range(0,len(s)):
            if s[i][0] not in "aeiouAEIOU":
                s[i]=s[i][1:len(s[i])]+s[i][0]
            s[i]+='m'+'a'*(i+2)
        print(s)
        return " ".join(s)
