class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer>stack=new Stack<>();
        int n=asteroids.length;
        for(int i=0;i<n;i++)
        {
            boolean destroyed=false;
            while(!stack.isEmpty() && (stack.peek()>0 && asteroids[i]<0))
            {
                if(stack.peek()< -asteroids[i])
                {
                    stack.pop();
                    continue;
                }
                else if(stack.peek()==-asteroids[i])
                    stack.pop();
                destroyed=true;
                break;
            }
            if(!destroyed)
            {
                stack.push(asteroids[i]);
            }
        }
        n=stack.size();
        int[] arr=new int[n];
        for(int i=n-1;i>=0;i--)
        {
            arr[i]=stack.pop();
        }
        return arr;

    }
}
