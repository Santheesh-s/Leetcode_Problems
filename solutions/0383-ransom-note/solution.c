bool canConstruct(char* ransomNote, char* magazine) {
    int  b[26]={0};
    for(int i=0;magazine[i] != '\0';i++)
        b[magazine[i]-'a']++;
    for(int i=0;i<ransomNote[i] != '\0';i++)
    {
        if(b[ransomNote[i]-'a']>0)
            b[ransomNote[i]-'a']--;
        else
            return false;
    }
    return true;
}
