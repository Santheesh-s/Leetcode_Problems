class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        length=len(image)
        for i in range(length):
            l=0
            r=length-1
            while(l<r):
                if image[i][l]==0:
                    temp1=1
                else:
                    temp1=0
                if image[i][r]==0:
                    temp2=1
                else:
                    temp2=0
                
                image[i][r]=temp1
                image[i][l]=temp2
                l+=1
                r-=1
            if length%2==1:
                if image[i][length/2]==1:
                    image[i][length/2]=0
                else:
                    image[i][length/2]=1
        return image
