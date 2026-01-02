class Solution {
    public int matchPlayersAndTrainers(int[] players, int[] trainers) {
        Arrays.sort(players);
        Arrays.sort(trainers);
        int k=trainers.length-1,count=0;
        for(int i=players.length-1;i>=0;i--)
        {
            for(int j=k;j>=0;j--)
            {
                if(players[i]<=trainers[j])
                {
                    k--;
                    count++;
                    break;
                }
                else
                    break;
            }
        }
        return count;
    }
}
