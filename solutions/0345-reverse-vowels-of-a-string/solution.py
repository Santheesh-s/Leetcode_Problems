class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        ls=[i for i in s if i in "aeiouAEIOU"][::-1]
        n=list(s)
        k=0
        for i in range(len(n)):
            if n[i] in "AEIOUaeiou":
                n[i]=ls[k]
                k+=1
        return "".join(n)
