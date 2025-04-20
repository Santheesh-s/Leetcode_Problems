class Solution {
    public String categorizeBox(int length, int width, int height, int mass) {
    int b=0,h=0;
    long a=1;
    a*=length;
    a*=height;
    a*=width;
    if(length>=10000 ||width>=10000 ||height>=10000 || a>=1000000000)
        b=1;
    if(mass>=100)
        h=1;
    if(b==1 && h==1)
        return "Both";
    else if(b!=1 && h!=1)
        return "Neither";
    else if(b==1 && h!=1)
        return "Bulky";
    return "Heavy";
    }
}
