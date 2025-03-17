class Solution(object):
    def finalString(self, s):
        k=""
        for i in s:
            if i=='i':
                k=k[::-1]
            else:
                k+=i
        return k
