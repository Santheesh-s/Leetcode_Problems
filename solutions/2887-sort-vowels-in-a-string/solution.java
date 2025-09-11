class Solution {
    public String sortVowels(String s) {
        int len=s.length();
        ArrayList<Character> arr=new ArrayList<>();
        int k=0;
        char[] brr=s.toCharArray();
        for(char c:brr)
            if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u'||c=='A'||c=='E'||c=='I'||c=='O'||c=='U')
                arr.add(c);
        Collections.sort(arr);
        for(int i=0;i<len;i++)
            if(brr[i]=='a'||brr[i]=='e'||brr[i]=='i'||brr[i]=='o'||brr[i]=='u'||brr[i]=='A'||brr[i]=='E'||brr[i]=='I'||brr[i]=='O'||brr[i]=='U')
                brr[i]=arr.get(k++);
        return new String(brr);
    }
}
