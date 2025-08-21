class Solution(object):
    def divisibilityArray(self, word, m):
        """
        :type word: str
        :type m: int
        :rtype: List[int]
        """
        n=len(word)
        ls=[0]*n
        rem=''
        for i in range(n):
            rem+=word[i]
            k=int(rem)%m
            if k==0:
                ls[i]=1
            rem=str(k)
        return ls
