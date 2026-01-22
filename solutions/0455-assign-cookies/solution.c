int compare(const void *a , const void *b)
{
    return *(int *)a-*(int *)b;
}
int findContentChildren(int* g, int gSize, int* s, int sSize) {
    qsort(g,gSize,sizeof(int),compare);
    qsort(s,sSize,sizeof(int),compare);
    int n = gSize, m = sSize, i = 0, j = 0;
    while (i < m && j < n) {
        if (g[j] <= s[i]) j++;
        i++;
    }
    return j;    
}
