from collections import defaultdict
class Solution(object):
    def countPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        diff_map=defaultdict(int)
        ans=0
        for w in words:
            diffs=[]
            for i in range(len(w)-1):
                diff=(ord(w[i+1])-ord(w[i]))%26
                diffs.append(diff)
            t_diff=tuple(diffs)
            ans+=diff_map[t_diff]
            diff_map[t_diff]+=1
        return ans
