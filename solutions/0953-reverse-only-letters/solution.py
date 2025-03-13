class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        ls=[i for i in s if i.isalpha()][::-1]
        for i in range(len(s)):
            if not s[i].isalpha():
                ls.insert(i,s[i])
        return "".join(ls)
