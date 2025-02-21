class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ls=[]
        st=".".join(words)
        for i in range(0,len(words)):
            st1=st.replace(words[i],"",1)
            if words[i] in st1:
                ls.append(words[i])
        return ls

