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
a2=Account()
print(a1)
print(type(a1))
print(id(a1)) #address of the object #2363278673488