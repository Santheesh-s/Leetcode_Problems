class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in board:
            ld={}
            for j in i:
                if j=='.':
                    pass
                elif j in ld:
                    return False
                else:
                    ld[j]=1
        for i in range(9):
            rd={}
            for j in range(9):
                if board[j][i]=='.':
                    pass
                elif board[j][i] in rd:
                    return False
                else:
                    rd[board[j][i]]=1
        for i in [0,3,6]:
            for j in [0,3,6]:
                rd={}
                for k in range(i, i + 3):
                    for l in range(j, j + 3):  
                        if board[k][l]=='.':
                            pass
                        elif board[k][l] in rd:
                            return False
                        else:
                            rd[board[k][l]]=1
                        print([k,l])
        return True
