int compare(const void *a,const void *b)
{
    return *(char*)a - *(char *)b;
}

bool isAnagram(char* s, char* t) {
    qsort(s,strlen(s),sizeof(char),compare);
    qsort(t,strlen(t),sizeof(char),compare);
    return 0==strcmp(s,t);

}
