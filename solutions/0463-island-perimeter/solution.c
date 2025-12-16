int islandPerimeter(int** grid, int gridSize, int* gridColSize) {
    int count=0;

    for(int i=0;i<gridSize;i++)
    {
        for(int j=0;j<*gridColSize;j++)
        {
            if(grid[i][j]==1)
            {
                if((j>0 && grid[i][j-1]==0) || j==0)
                    count++;
                if((j<*gridColSize-1 && grid[i][j+1]==0) || j==*gridColSize-1)
                    count++;
                if((i>0 && grid[i-1][j]==0) || i==0)
                    count++;
                if((i<gridSize-1 && grid[i+1][j]==0) || i==gridSize-1)
                    count++;
            }
        }
    }
    return count;
}
