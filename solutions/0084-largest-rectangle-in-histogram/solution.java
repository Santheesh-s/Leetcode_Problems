class Solution {
    public int largestRectangleArea(int[] heights) {
        Stack<Integer>stack =new Stack<>();
        int n=heights.length;
        int left,right,maxArea=0;
        for(int i=0;i<n;i++)
        {
            while(!stack.isEmpty() && heights[stack.peek()]>heights[i])
            {
                int topheight=stack.pop();
                if(!stack.isEmpty())
                    left=stack.peek();
                else
                    left=-1;
                right=i;
                maxArea=Math.max(maxArea,(right-left-1)*heights[topheight]);
            }
            stack.push(i);
        }
        while(!stack.isEmpty())
            {
                int topheight=stack.pop();
                if(!stack.isEmpty())
                    left=stack.peek();
                else
                    left=-1;
                right=n;
                maxArea=Math.max(maxArea,(right-left-1)*heights[topheight]);
            }
        return maxArea;
    }
}
