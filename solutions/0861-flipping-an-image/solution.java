class Solution {
    public int[][] flipAndInvertImage(int[][] image) {
        int length1=image.length;
        int temp1,temp2;
        for(int i=0;i<length1;i++)
        {
            int l=0;
            int r=length1-1;
            while(l<r)
            {
                if(image[i][l]==0)
                    temp1=1;
                else
                    temp1=0;
                if(image[i][r]==0)
                    temp2=1;
                else
                    temp2=0;
                
                image[i][r]=temp1;
                image[i][l]=temp2;
                l+=1;
                r-=1;
            }
            if(length1%2==1)
            {
                if(image[i][length1/2]==1)
                    image[i][length1/2]=0;
                else
                    image[i][length1/2]=1;
            }
        }
        return image;
    }
}
