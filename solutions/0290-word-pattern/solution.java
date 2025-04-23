class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] arr=s.split("\\ ");
        if(arr.length!=pattern.length())
            return false;
        Map<Character,String>map=new HashMap<>();
        Set<String>usedWords=new HashSet<>();
        int b=0;
        for(char a:pattern.toCharArray())
        {
            if(map.containsKey(a))
            {
                if(!(map.get(a)).equals(arr[b]))
                    return false;
            }
            else
            {
                if (usedWords.contains(arr[b]))
                    return false;
                map.put(a, arr[b]);
                usedWords.add(arr[b]);
            }
            b++;
        }
        return true;
    }
}
