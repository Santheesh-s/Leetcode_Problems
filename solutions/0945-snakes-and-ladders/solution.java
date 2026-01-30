class Solution {
    public int snakesAndLadders(int[][] board) {
        Queue<Integer>q=new LinkedList<>();
        
        int roll=0,cur=1,n=board.length;
        int sq=n*n;
        q.offer(cur);
        boolean visited[]=new boolean[n*n+1];
        while(!q.isEmpty())
        {
            int size=q.size();
            while(size-->0)
            {
                cur=q.poll();
                if(cur==sq) return roll;
                for(int dice=1;dice<=6 && cur+dice<=sq;dice++)
                {
                    int next=cur+dice;
                    int row=(next-1)/n;
                    int col=(next-1)%n;
                    if(row%2==1) 
                        col=n-1-col;
                    row=n-1-row;
                    if(board[row][col]!=-1)
                        next=board[row][col];
                    if(visited[next]==false)
                    {
                        q.offer(next);
                        visited[next]=true;
                    }
                }
            }
            roll++;
        }
        return -1;
    }
}
