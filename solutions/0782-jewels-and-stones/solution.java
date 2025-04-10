class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        int n=0;
        for(char a:jewels.toCharArray())
            for(char b:stones.toCharArray())
                if(a==b)
                    n++;
        return n;
    }
}
