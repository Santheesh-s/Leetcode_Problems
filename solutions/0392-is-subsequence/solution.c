bool isSubsequence(char* s, char* t) {
    int n=strlen(s),j=0;
    for(int i=0;i<strlen(t);i++)
        if(j<n)
            if(s[j]==t[i])
                j+=1;
    return (j==n)?true:false;
}
