class Solution(object):
    def winningPlayer(self, x, y):
        """
        :type x: xnt
        :type y: xnt
        :rtype: str
        """
        count=0
        while x>=1 and y>=4:
            count+=1
            x-=1
            y-=4
        return 'Alice' if count%2!=0 else 'Bob'
