class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        map<int,int>map;
        stack<int>stack;

        int n2=nums2.size(),n1=nums1.size();
        vector<int> res(n1,-1);

        for(int i=n2-1;i>=0;i--)
        {
            while(!stack.empty() && stack.top()<=nums2[i])
                stack.pop();
            if(stack.empty())
                map[nums2[i]]=-1;
            else
                map[nums2[i]]=stack.top();
            stack.push(nums2[i]);
        }
        for(int i=0;i<n1;i++)
            res[i]=map[nums1[i]];
        return res;
    }
};
