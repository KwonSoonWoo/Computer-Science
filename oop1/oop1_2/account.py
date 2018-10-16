class Account:
    num_acnt = 0            #1

    @classmethod
    def get_num_acnt(cls):  #2
        """
        cls.get_num_acnt() -> integer
        """
        return cls.num_acnt

    def __init__(self, name, money):
        self.user = name    #3
        self.balance = money
        Account.num_acnt += 1   #4

    def deposit(self, money):
        if money < 0:
            return
        self.balance += money

    def withdraw(self, money):
        if money > 0 and money <= self.balance:
            self.balance -= money
            return money
        else:
            return None

    def transfer(self, other, money):   #5
        '''
        obj.transfer(other, money) -> bool
        other: The object to interact with
        money: money the user wants to send

        returns True if the balance is enough to transfer
        returns False if not
        '''
        mon = self.withdraw(money)
        if mon:
            other.deposit(mon)
            return True
        else:
            return False


    def __str__(self):
        return 'user : {}, balance : {}'.format(self.user, self.balance)
