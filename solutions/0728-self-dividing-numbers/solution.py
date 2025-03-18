class Solution(object):
    def selfDividingNumbers(self, left, right):
        def ss(n):
            if '0' in str(n):
                return False
            for i in str(n):
                if n%int(i)!=0:
                    return False
            return True
        ls=[]
        for i in range(left,right+1):
            if ss(i):
                ls.append(i)
        return ls
