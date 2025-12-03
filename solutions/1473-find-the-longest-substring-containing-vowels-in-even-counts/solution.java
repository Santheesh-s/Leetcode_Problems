class Solution {
    public int findTheLongestSubstring(String s) {
        int n=s.length(),length=0,cur=0;
        Map<Integer,Integer>map=new HashMap<>();
        map.put(0,-1);
        for(int i=0;i<n;i++)
        {
            char a=s.charAt(i);
            if(a=='a')
                cur=cur^1;
            else if(a=='e')
                cur=cur^2;
            else if(a=='i')
                cur=cur^4;
            else if(a=='o')
                cur=cur^8;
            else if(a=='u')
                cur=cur^16;
            if(map.containsKey(cur))
                length=Math.max(length,i-map.get(cur));
            else
                map.put(cur,i);
        }
        return length;
    }
}
