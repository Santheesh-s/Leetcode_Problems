bool squareIsWhite(char* s) {
    int a=s[0]%2==0;
    int b=s[1]%2==0;
    if(a && b)
        return false;
    else if(!a && !b)
        return false;
    else if(a && !b)
        return true;
    return true;
}
