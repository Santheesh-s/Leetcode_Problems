class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        ind=word.find(ch)
        s=word[0:ind+1][::-1]+word[ind+1:]
        return s
