class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        s=[words[0]]
        for i in words[1:]:
            for j in s:
                flag=0
                if "".join(sorted(i))=="".join(sorted(j)):
                    flag=1
            if flag==0:
                s.append(i)
        return list(s)
