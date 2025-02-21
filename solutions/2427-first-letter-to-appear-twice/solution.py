class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        st=set()
        b=0
        for i in s:
            if i not in st:
                st.add(i)
            else:
                return i
        
