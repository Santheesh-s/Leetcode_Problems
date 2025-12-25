bool isIsomorphic(char* s, char* t) {
    int a[256]={0},b[256]={0};
    for(int i=0;(s[i] && t[i]);i++)
    {
        if(a[s[i]]==0 && b[t[i]]==0)
        {
            a[s[i]]=t[i];
            b[t[i]]=s[i];
        }
        else if(a[s[i]]!=t[i] && b[t[i]]!=s[i])
            return false;
    }
    return strlen(s)==strlen(t);
}
