class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        print(s.count(letter))
        return s.count(letter)*100/len(s)
