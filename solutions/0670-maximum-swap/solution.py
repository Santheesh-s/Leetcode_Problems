class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        n=list(str(num))
        ideal=sorted(n,reverse=True)
        for i in range(len(n)):
            if n[i] != ideal[i]:
                for j in range(len(n) - 1, i, -1):
                    if n[j] == ideal[i]:
                        n[i], n[j] = n[j], n[i]
                        return int("".join(n))
        return num

