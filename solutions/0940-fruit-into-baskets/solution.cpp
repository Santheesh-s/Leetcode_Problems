class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        map<int,int> mp;
        int res=0;
        for(int left=0,right=0;right<fruits.size();right++)
        {
            mp[fruits[right]]++;
            while(mp.size()>2)
            {
                mp[fruits[left]]--;
                if(mp[fruits[left]]==0)
                    mp.erase(fruits[left]);
                left++;
            }
            res=max(res,right-left+1);
        }
        return res;
    }
};
