class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while(len(s)>k):
            s1=[s[i:i + k] for i in range(0, len(s), k)]
            s=''
            for i in s1:
                s3=0
                for j in i:
                    s3+=int(j)
                s+=str(s3)
        return s
