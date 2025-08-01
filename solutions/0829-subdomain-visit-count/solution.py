class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        ls,ls1={},[]
        for i in cpdomains:
            sp=i.split()
            m=sp[1].split('.')
            m1=['.'.join(m[a:]) for a in range(len(m))]
            for j in m1:
                if j in ls:
                    ls[j]+=int(sp[0])
                else:
                    ls[j]=int(sp[0])
        for i,j in ls.items():
            ls1.append(str(j)+" "+i)
        return ls1
