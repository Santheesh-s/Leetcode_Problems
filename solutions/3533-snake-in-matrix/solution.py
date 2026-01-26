class Solution(object):
    def finalPositionOfSnake(self, n, commands):
        """
        :type n: int
        :type commands: List[str]
        :rtype: int
        """
        k=0
        for i in commands:
            if i=="RIGHT":
                k+=1
            elif i=="LEFT":
                k-=1
            elif i=="UP":
                k-=n
            else:
                k+=n
        return k
