class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        s=list(map(int,date.split("-")))
        return "-".join([bin(i)[2:] for i in s])
