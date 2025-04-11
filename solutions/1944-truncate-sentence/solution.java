class Solution {
    public String truncateSentence(String s, int k) {
        List<String>ls=new ArrayList<>();
        String[] a=s.split("\\ ");
        for(int i=0;i<a.length;i++)
        {
            if(i!=k)
                ls.add(a[i]);
            else
                break;
        }
        return String.join(" ",ls);
    }
}
