class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        d={}
        res=[]
        for i in words:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        fr=sorted(d.items(),key=lambda x:len(x[0]))
        fr=sorted(d.items(),key=lambda x:x[0])        
        fr=sorted(fr,key=lambda x:x[1],reverse=True)
        for i in fr[:k]:
            res.append(i[0])
        return res
