class Solution {
    public int splitNum(int num) {
        String a="",b="";
        char[] arr=String.valueOf(num).toCharArray();
        Arrays.sort(arr);
        for(int i=0;i<arr.length;i+=2)
            a+=arr[i];
        for(int i=1;i<arr.length;i+=2)
            b+=arr[i];
        return Integer.parseInt(a)+Integer.parseInt(b);
    }
}
