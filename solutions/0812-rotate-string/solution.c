bool rotateString(char* s, char* goal) {
    if(strlen(s)==strlen(goal))
    {
        char temp[strlen(s)*2+1];
        return strstr(strcat(strcpy(temp,s),s),goal);
    }
    return false;
}
