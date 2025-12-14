class Bank(object):

    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.ls = balance   # store balance list properly

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        # validate account numbers
        if account1 < 1 or account2 < 1 or \
           account1 > len(self.ls) or account2 > len(self.ls):
            return False

        # check sufficient balance
        if self.ls[account1 - 1] < money:
            return False

        # perform transfer
        self.ls[account1 - 1] -= money
        self.ls[account2 - 1] += money
        return True

    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if account < 1 or account > len(self.ls):
            return False

        self.ls[account - 1] += money
        return True

    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if account < 1 or account > len(self.ls):
            return False

        if self.ls[account - 1] < money:
            return False

        self.ls[account - 1] -= money
        return True

