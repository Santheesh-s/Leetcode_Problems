class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        s=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        ls=date.split()
        ls[1]=str(s.index(ls[1])+1)
        ls[0]="".join([i for i in ls[0] if i.isdigit()])
        if len(ls[0])==1:
            ls[0]='0'+ls[0]
        if len(ls[1])==1:
            ls[1]='0'+ls[1]
        return "-".join(ls[::-1])
