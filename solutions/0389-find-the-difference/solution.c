char findTheDifference(char* s, char* t) {
    int result=0;
        for(int i=0;i<strlen(s);i++)
            result^=s[i];
        for(int i=0;i<strlen(t);i++)
            result^=t[i];
        return (char)result;
}
