class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        int boat=0;
        int left=0,right=people.size()-1;
        sort(people.begin(),people.end());
        while(left < right)
        {
            if(people[left]+people[right] <= limit)
            {
                boat++;
                left++;
                right--;
            }
            else
            {
                if(people[right]<=limit)
                    boat++;
                right--;
            }
            if(left==right)
                boat++;
        }
        return boat;
    }
};
