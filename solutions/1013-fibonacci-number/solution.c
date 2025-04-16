

int fib(int n){
    int a=0,b=1,fib=1,i=1;
        if(n==0)
            return 0;
        if(n<=2)
            return 1;
        while(i<n-1)
        {
            a=b;
            b=fib;
            fib=a+b;
            i++;
        }
        return fib;
}
