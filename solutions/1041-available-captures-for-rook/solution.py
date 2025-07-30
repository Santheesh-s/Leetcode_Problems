class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        p=0
        ls=[]
        for i in range(8):
            if 'R' in board[i]:
                for j in range(8):
                    if board[i][j]!='.':
                        if board[i][j]=='R':
                            a=j
                            if len(ls)>0 and ls[-1]=='p':
                                p+=1
                        if board[i][j]=='p' and len(ls)>0 and ls[-1]=='R':
                            p+=1 
                        ls.append(board[i][j])         
                break
        ls1=[]
        for i in range(8):
            if board[i][a]!='.' :
                if board[i][a]=='R':
                    if len(ls1)>0 and ls1[-1]=='p':
                                p+=1
                if board[i][a]=='p' and len(ls1)>0 and ls1[-1]=='R':
                        p+=1 
                ls1.append(board[i][a]) 
        return p
