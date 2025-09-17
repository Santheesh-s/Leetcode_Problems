class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<int>stack;
        int n=heights.size();
        int left,right,maxArea=0;
        for(int i=0;i<n;i++)
        {
            while(!stack.empty() && heights[stack.top()]>heights[i])
            {
                int topheight=stack.top();
                stack.pop();
                if(!stack.empty())
                    left=stack.top();
                else
                    left=-1;
                right=i;
                maxArea=max(maxArea,(right-left-1)*heights[topheight]);
            }
            stack.push(i);
        }
        while(!stack.empty())
            {
                int topheight=stack.top();
                stack.pop();
                if(!stack.empty())
                    left=stack.top();
                else
                    left=-1;
                right=n;
                maxArea=max(maxArea,(right-left-1)*heights[topheight]);
            }
        return maxArea;
    }
};
