class Solution {
    public boolean isBalanced(String num) {
        int a=0,b=0,n=num.length(),i=0;
        for(i=1;i<n;i+=2)
        {
            a+=Integer.parseInt(num.charAt(i)+"");
            b+=Integer.parseInt(num.charAt(i-1)+"");
        }
        if(n%2!=0)
            b+=Integer.parseInt(num.charAt(i-1)+"");
        return a==b;
    }
}
