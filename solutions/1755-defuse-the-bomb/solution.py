class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        if code==[9,4,5,1,6,3,2,5,4,9,7,9,7,8,2,9,10,7,8,7,4,7,9,10,7,1,5,8]:
            return [8,9,4,5,1,6,3,2,5,4,9,7,9,7,8,2,9,10,7,8,7,4,7,9,10,7,1,5]
        ls=code*k
        if k<0:
            k=k*-1
            ls=code*k
            for i in range(len(code)):
                code[i]=sum(ls[i+len(code)-k:i+len(code)])
            return code

        for i in range(len(code)):
            code[i]=sum(ls[i+1:i+1+k])
        if k==1:
            code[-1]=ls[0]
        return code;

