class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.split()
        a=[int(i) for i in s if i.isdigit()]
        for i in range(1,len(a)):
            if a[i-1]>=a[i]:
                return False
        return True
