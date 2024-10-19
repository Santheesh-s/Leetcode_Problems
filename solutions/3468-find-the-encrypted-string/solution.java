class Solution {
    public String getEncryptedString(String s, int k) {
        int len=s.length();
        k = k % len;
        s+=s;
        String h="";
        for(int i=0;i<len;i++)
        {
            h+=s.charAt(i+k);
        }
        return h;
    }
}
