class Solution {
    public String convertDateToBinary(String date) {
        String[] a=date.split("\\-");
        for(int i=0;i<a.length;i++)
            a[i]=Integer.toBinaryString(Integer.parseInt(a[i]));
        return String.join("-",a);
    }
}
