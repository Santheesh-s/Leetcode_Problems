class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        if ruleKey=='type':
            ruleKey=0
        elif ruleKey=='color':
            ruleKey=1
        else:
            ruleKey=2
        ls=0
        for i in items:
            if i[ruleKey]==ruleValue:
                ls+=1
        return ls
        
        
