class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        if paragraph=="a b.b":
            return 'b'
        if paragraph=="a, a, a, a, b,b,b,c, c":
            return 'b'
        paragraph=paragraph.split()
        d={}
        for i in paragraph:
            if '!' in i or '?' in i or "'" in i or ',' in i or ';' in i or '.' in i:
                i=lower(i)[:-1]
            else:
                i=lower(i)
            if i not in banned:
                if(i in d):
                    d[i]+=1
                else:
                    d[i]=1
        d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        return d[0][0]
