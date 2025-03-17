class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        ls="".join([str(ord(i)-97) for i in firstWord]).strip()
        ls1="".join([str(ord(i)-97) for i in secondWord]).strip()
        ls2="".join([str(ord(i)-97) for i in targetWord]).strip()
        return int(ls)+int(ls1)==int(ls2)
