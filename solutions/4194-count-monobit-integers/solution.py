class Solution(object):
    def countMonobit(self, n):
        """
        :type n: int
        :rtype: int
        """
        k=1
        count=1
        while True:
            val=(1<<k)-1
            if val<=n:
                count+=1
                k+=1
            else:
                break
        return count;
