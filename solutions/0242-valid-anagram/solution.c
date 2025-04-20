bool isAnagram(char* s, char* t) {
    int a=strlen(s);
    int b=strlen(t);
    int arr[26]={};
    if(a!=b) return false;
    for(int i=0;i<a;i++)
    {
        arr[s[i]-97]-=1;
        arr[t[i]-97]+=1;
    }
    for(int i=0;i<26;i++)
        if(arr[i]!=0)
            return false;
    return true;
}
