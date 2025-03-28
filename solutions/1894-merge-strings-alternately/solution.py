class Solution(object):
    def mergeAlternately(self, word1, word2):
        a=len(word1)
        b=len(word2)
        s=""
        for i,j in zip(word1,word2):
            s+=i+j
        if a>b:
            s+=word1[b:]
        elif a<b:
            s+=word2[a:]
        return s
