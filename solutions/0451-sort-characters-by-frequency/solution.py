class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        ls={}
        for i in s:
            if i in ls:
                ls[i]+=1
            else:
                ls[i]=1
        ls=sorted(ls.items(),key=lambda x:x[1],reverse=True)
        print(ls)
        s=""
        for i in ls:
            s+=(i[0])*i[1]
        return s
