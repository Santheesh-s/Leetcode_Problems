class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        title=lower(title)
        ls=title.split()
        for i in range(0,len(ls)):
            if len(ls[i])>2:
                ls[i]=capitalize(ls[i])
        return " ".join(ls)
