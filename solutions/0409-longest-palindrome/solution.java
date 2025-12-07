class Solution {
    public int longestPalindrome(String s) {
        Map<Character,Integer>map=new HashMap<>();
        int sum=0,flag=0;
        for(char a:s.toCharArray())
            map.put(a,map.getOrDefault(a,0)+1);
        for(int a:map.values())
        {
            int b=(a/2)*2;
            if(a-b==1)
                flag=1;
            sum+=b;
        }
        return sum+flag;
    }
}
