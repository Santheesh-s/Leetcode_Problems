int lengthOfLastWord(char* s) {
    int len = 0;
    int i;
    for (i = strlen(s) - 1; i >= 0 && s[i] == ' '; i--);
    for (; i >= 0 && s[i] != ' '; i--) {
        len++;
    }
    
    return len;
}
