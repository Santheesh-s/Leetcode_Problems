class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1=num1.split('+')
        num2=num2.split('+')
        a=int(num1[0])
        b=int(num1[1][0:-1])
        c=int(num2[0])
        d=int(num2[1][0:-1])
        r=(a*c)-(b*d)
        i=(a*d)+(b*c)
        return str(r)+'+'+str(i)+'i'
