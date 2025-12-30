class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        d={}
        for i in range(len(score)):
            d[score[i]]=i+1
        d=sorted(d.items(),reverse=True)
        for i,j in enumerate(d):
            score[j[1]-1]=str(i+1)
            if score[j[1]-1]=='1':
                score[j[1]-1]="Gold Medal"
            elif score[j[1]-1]=='2':
                score[j[1]-1]="Silver Medal"
            elif score[j[1]-1]=='3':
                score[j[1]-1]="Bronze Medal"
        return score;
