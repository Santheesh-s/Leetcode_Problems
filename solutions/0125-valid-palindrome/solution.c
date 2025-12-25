bool isPalindrome(char* s) {
    char arr[strlen(s)+1];
    int i,j=0;
    for(i=0;i<strlen(s);i++)
    {
        if( s[i]>=65 && s[i]<65+26 )
            arr[j++]=s[i]+32;
        else if( (s[i]>=97 && s[i]<97+26) || (s[i]>=48 && s[i]<58) )
            arr[j++]=s[i];
    }
    arr[j]='\0';
    i=0;j--;
    while(i<j)
    {
        if(arr[i]!=arr[j])
            return false;
        i++;j--;
    }
    return true;
}
