class Solution {
    public boolean wordPattern(String pattern, String s) {
        Map<Character,String> map=new HashMap<>();
        String[] arr=s.split("\\s+");
        int i=0;
        if(arr.length!=pattern.length()) return false;
        for(char a:pattern.toCharArray())
        {
            if(!map.containsKey(a))
            {
                if(map.containsValue(arr[i]))
                    return false;
                map.put(a,arr[i++]);
            }
            else
                if(!map.get(a).equals(arr[i++]))
                    return false;
        }
        return true;
    }
}
