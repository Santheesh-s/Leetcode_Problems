class Solution(object):
    def numberOfLines(self, width, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        line=0
        p=0
        k=0;
        for a in s:
            if(p+width[ord(a)-97]>100):
                line+=1;
                p=0;
            p+=width[ord(a)-97];
        return [line+1,p]
        
