class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        c=0
        for i in details:
            if int(i[-4:-2])>60:
                c+=1
        return c
