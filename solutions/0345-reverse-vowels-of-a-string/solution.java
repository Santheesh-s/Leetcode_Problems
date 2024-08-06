class Solution {
    public String reverseVowels(String s) {
        char[] str=s.toCharArray();
        char[] ss=new char[str.length];int k=0;
        for(int i=0;i<str.length;i++)
        {
            if(str[i]=='A'||str[i]=='E'||str[i]=='I'||str[i]=='O'||str[i]=='U'||str[i]=='a'||str[i]=='e'||str[i]=='i'||str[i]=='o'||str[i]=='u')
            {
                ss[k++]=str[i];
            }
        }
        k=0;
        for(int i=str.length-1;i>=0;i--)
        {
            if(str[i]=='A'||str[i]=='E'||str[i]=='I'||str[i]=='O'||str[i]=='U'||str[i]=='a'||str[i]=='e'||str[i]=='i'||str[i]=='o'||str[i]=='u')
            {
                str[i]=ss[k++];
            }
        }
        return new String(str);
    }
}
