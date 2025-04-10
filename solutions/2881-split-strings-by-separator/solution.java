class Solution {
    public List<String> splitWordsBySeparator(List<String> words, char separator) {
        List<String> ls=new ArrayList<>();
        String sep="\\"+String.valueOf(separator);
        for(String a:words)
        {
            String[] b=a.split(sep);
            for(String c:b)
                if(!c.isEmpty())
                    ls.add(c);
        }
        return ls;
    }
}
