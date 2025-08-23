class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        first=0
        second=0
        temp=0
        count=0;
        for i in range(0,len(row),2):
            first=row[i];
            second=row[i]^1;
            if(row[i+1]==second):
                continue;
            for j in range(i+1,len(row)):
                if(second==row[j]):
                    temp=row[i+1];
                    row[i+1]=row[j];
                    row[j]=temp;
                    count+=1;
                    break;
        return count;
