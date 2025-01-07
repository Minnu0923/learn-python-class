class Account:
    min_bal=500 #static variable or class level variable

    def __init__(self,a,b,c): #proportional to object arguments
        self.acc_id=a
        self.acc_name=b
        self.acc_bal=c

    def get_bal(self):
        return self.acc_bal-self.min_bal

    def deposit_amount(self,amount):
        self.acc_bal=self.acc_bal+amount

    def withdrawl_amount(self,amount):
        self.acc_bal=self.acc_bal-amount

a1=Account(101,'Rahul',1500)
a2=Account(102,'Sonia',5000)



a1.deposit_amount(200)
a2.deposit_amount(500)


a1.withdrawl_amount(50)
a2.withdrawl_amount(50)

print("Account Holder Bal")
print("Account Name:",a1.acc_name,- and Bal:"")


