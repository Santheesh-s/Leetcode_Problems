class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people=sorted(people)
        boat=0;
        left=0
        right=len(people)-1;
        while(left < right):
            if(people[left]+people[right] <= limit):
                boat+=1
                left+=1
                right-=1            
            else:
                if(people[right]<=limit):
                    boat+=1
                right-=1
            if(left==right):
                boat+=1
        return boat;
