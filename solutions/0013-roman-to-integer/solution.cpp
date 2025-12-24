class Solution {
public:
    int romanToInt(string s) {
        map<char,int>mp;
        mp['I']=1;
        mp['V']=5;
        mp['X']=10;
        mp['L']=50;
        mp['C']=100;
        mp['D']=500;
        mp['M']=1000;
        int max1=-1,sum=0;
        for(int i=s.size()-1;i>=0;i--)
        {
            int val=mp[s[i]];
            max1=max(max1,val);
            if(val>=max1) sum+=val;
            else sum-=val;
        }
        return sum;
    }
};
