class Solution(object):
    def __init__(self):
        i=2
        self.ls=[[1],[1,1]]
        while(i<31):
            a=[1]
            for j in range(len(self.ls[i-1])-1):
                a.append(self.ls[i-1][j+1]+self.ls[i-1][j])
            a.append(1)
            self.ls.append(a)
            i+=1
    def generate(self, n):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        return self.ls[:n]
