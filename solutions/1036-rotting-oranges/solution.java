class Solution {
    Queue<int[]> q;
    int fresh;
    public Solution()
    {
        fresh=0;
        q=new LinkedList<>();
    }
    void bfs(int[][] grid,int r, int c)
    {
        if(r>=0 && c>=0 && r<grid.length && c<grid[0].length && grid[r][c]==1)
        {
            q.offer(new int[] {r,c});
            fresh--;
            grid[r][c]=2;
        }
    }
    public int orangesRotting(int[][] grid) {

        int time=0;
        for(int i=0;i<grid.length;i++)
            for(int j=0;j<grid[0].length;j++)
            {
                if(grid[i][j]==1)
                    fresh++;
                else if(grid[i][j]==2)
                    q.offer(new int[]{i,j});
            }
        if(fresh==0) return 0;
        while(!q.isEmpty())
        {
            int size=q.size();
            while(size-- >0)
            {
                int arr[]=q.poll();
                bfs(grid, arr[0]-1, arr[1]);
                bfs(grid, arr[0]+1, arr[1]);
                bfs(grid, arr[0], arr[1]-1);
                bfs(grid, arr[0], arr[1]+1);
            }
            if(!q.isEmpty())
                time++;
        }
        return fresh>0?-1:time;
    }
}
