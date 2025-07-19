class Solution {
    public int[] replaceElements(int[] arr) {
        for(int i=arr.length-1;i>0;i--)
            if(arr[i]>arr[i-1])
                arr[i-1]=arr[i];
        for(int i=1;i<arr.length;i++)
            arr[i-1]=arr[i];
        arr[arr.length-1]=-1;
        return arr;
    }
}
