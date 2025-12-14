class Solution(object):
    def minMoves(self, balance):
        """
        :type balance: List[int]
        :rtype: int
        """
        neg=-1
        moves=0
        n=len(balance)
        for i in range(n):
            if(balance[i]<0):
                neg=i
                break;
        sum1=sum(balance)
        a=-balance[neg]
        if(sum1<0):
            return -1
        elif(neg==-1):
            return 0;
        else:
            i=neg-1
            j=neg+1
            distance=1
            while(a>0):
                i=(neg-distance)%n
                j=(neg+distance)%n

                t=min(balance[i],a)
                balance[i]-=t
                a-=t
                moves+=(t*distance)

                if a>0:
                    t=min(balance[j],a)
                    balance[j]-=t
                    a-=t
                    moves+=(t*distance)
                distance+=1
        return moves
                     
        
