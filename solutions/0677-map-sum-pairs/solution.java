class MapSum {
    Map<String,Integer>map;
    public MapSum() {
        map=new HashMap<>();
    }
    
    public void insert(String key, int val) {
        map.put(key,val);
    }
    
    public int sum(String prefix) {
        int s=0;
        for(Map.Entry<String,Integer> entry:map.entrySet())
            if(entry.getKey().startsWith(prefix))
                s+=entry.getValue();
        return s;   
    }
}

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum obj = new MapSum();
 * obj.insert(key,val);
 * int param_2 = obj.sum(prefix);
 */
