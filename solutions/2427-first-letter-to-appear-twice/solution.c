char repeatedCharacter(char* str) {
    int arr[26]={};
    for(int i=0;i<strlen(str);i++)
    {
        if(arr[str[i]-97]!=0)
            return str[i];
        arr[str[i]-97]++;
    }
    return 'a';    
}
