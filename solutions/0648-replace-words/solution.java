class Solution {
    public String replaceWords(List<String> dictionary, String sentence) {
        String[] ls=sentence.split("\\ ");
        int n=ls.length;
        for(String i:dictionary)
        {
            for(int j=0;j<n;j++)
            {
                if(ls[j].startsWith(i))
                    ls[j]=i;
            }
        }
        return String.join(" ",ls);
    }
}
