class Account:
    acc_min_bal=100
    branch_name="Marathahalli"

    def open_account(self):
        print("Account Opened Successfully")
    def deposit_amount(self):
        print("Amount Deposited ")
    def withdrawl_amount(self):
        print("Amount withdrawn")
    def get_bal(self):
        print("Amount")
    def close_account(self):
        print("Balance is negative please maintain mininum balance")
a1=Account()
a1.open_account()
a1.deposit_amount()
a1.withdrawl_amount()
a1.get_bal()
a1.close_account()