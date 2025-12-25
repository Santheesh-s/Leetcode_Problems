int strStr(char* haystack, char* needle) {
    int k=strlen(needle);
    int j=0,i;
    for(i=0;i<strlen(haystack);i++)
    {
        if(haystack[i]==needle[j])
        {
            j++;
            if(j==k)
                return i-k+1;
        }
        else
        {
            i = i - j;
            j=0;
        }
    }
    return -1;
}
