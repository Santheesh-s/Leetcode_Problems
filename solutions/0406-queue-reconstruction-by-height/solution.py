class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # print(sorted(people,key=lambda p: (-p[0], p[1])))
        people=sorted(people,key=lambda p: (-p[0], p[1]))
        res=[]

        for i in people:
            res.insert(i[1],i)
        return res
