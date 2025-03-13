class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        c=0
        for i in set(word):
            if i.islower():
                if i.upper() in word:
                    c+=1
            else:
                if i.lower() in word:
                    c+=1
        return c/2
