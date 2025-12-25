char* reverseWords(char* s) {
    char **arr = (char **)malloc(strlen(s) * sizeof(char*));
    arr[0]=(char *)malloc(10000);
    int k=0,j=0;
    for(int i=0;i<strlen(s);i++)
    {
        if(s[i]!=' ')
        {
            arr[k][j]=s[i];
            j++;
        }
        else
        {
            arr[k][j]='\0';
            k++;
            arr[k]=(char*)malloc(10000);
            j=0;
        }
    }
    arr[k][j]='\0';
    char *res=(char*)malloc(10000);
    res[0] = '\0';
    for(int i = k; i >= 0; i--)
    {
        if(strlen(arr[i]) > 0)
        {    
            strcat(res, arr[i]);
            strcat(res," ");
        }
    }
    res[strlen(res)-1]='\0';
    return res;
}
