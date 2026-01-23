bool checkRecord(char* s) {
    int l=0,a=0;
    for(int i=0;s[i];i++)
    {
        if(s[i]=='A')
        {
            a+=1;
            l=0;
        }
        else if(s[i]=='L')
        {
            l+=1;
            if(l==3)
                return false;
        }
        else
            l=0;
    }
    return a<2?true:false;
}
