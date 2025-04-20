class Solution(object):
    def categorizeBox(self, length, width, height, mass):
        """
        :type length: int
        :type width: int
        :type height: int
        :type mass: int
        :rtype: str
        """
        b=0
        h=0;
        a=1
        a*=length;
        a*=height;
        a*=width;
        if(length>=10000 or width>=10000 or height>=10000 or a>=1000000000):
            b=1;
        if(mass>=100):
            h=1;
        if(b and h):
            return "Both";
        elif(not b and not h):
            return "Neither";
        elif(b and not h):
            return "Bulky";
        return "Heavy";
        
