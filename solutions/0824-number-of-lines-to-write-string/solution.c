

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* numberOfLines(int* width, int widthsSize, char * s, int* rs){
        int line=0,p=0,k=0;
        int *arr=(int*)malloc(2*sizeof(int));
        *rs=2;
        for(int i=0;s[i]!='\0';i++)
        {
            if(p+width[s[i]-97]>100)
            {
                line++;
                p=0;
            }
            p+=width[s[i]-97];
        }
        arr[0]=line+1;
        arr[1]=p;
        return arr;
}
