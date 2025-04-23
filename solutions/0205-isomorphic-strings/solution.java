class Solution {
    public boolean isIsomorphic(String s, String t) {
        Map<Character,Character>map=new HashMap<>();
        Set<Character>use=new HashSet<>();
        char[] arr=s.toCharArray();
        char[] brr=t.toCharArray();
        for(int i=0;i<s.length();i++)
        {
            char a=arr[i];
            char b=brr[i];
            if(map.containsKey(a))
            {
                if(map.get(a)!=b)
                    return false;
            }
            else
            {
                if (use.contains(b))
                    return false;
                map.put(a,b);
                use.add(b);
            }
        }
        return true;
    }
}
