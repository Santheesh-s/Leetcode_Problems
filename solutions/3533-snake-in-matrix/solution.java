class Solution {
    public int finalPositionOfSnake(int n, List<String> commands) {
        int j=0;
        for(int i=0;i<commands.size();i++)
        {
            if(commands.get(i).equals("RIGHT"))
                j++;
            if(commands.get(i).equals("LEFT"))
                j--;
            if(commands.get(i).equals("UP"))
                j-=n;
            if(commands.get(i).equals("DOWN"))
                j+=n;
        }
        return j;
    }
}
