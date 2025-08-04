class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        ls=set()
        for i in emails:
            ind=i.index('@')
            rem=i[ind:]
            i=i[:ind].replace('.','')+rem
            if '+' in i:
                ind=i.index('@')
                p=i.index('+')
                i=i[:p]+i[ind:]
            ls.add(i)
        return len(ls)


            
