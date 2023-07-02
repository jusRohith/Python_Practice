class Customer:
    bankName = 'Axis Bank Of India'
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f'Account Balance after deposit : {self.balance}')
    def withdraw(self,amount):
        if self.balance<amount:
            print('Insufficient Funds')
        else:
            self.balance=self.balance-amount
            print(f'Balance in your account after withdrawal : {self.balancef}')
print(f'Welcome to {Customer.bankName}')
name=input('Enter your name :')
c=Customer(name)
while True:
    print('d - Deposit \n w - Withdrawal \n e - Exit')
    option=input('Choose your option :')
    if option.lower()=='d':
        amount=float(input('Enter the amount you want to Deposit'))
        c.deposit(amount)
    elif option.lower()=='w':
        amount=float(input('Enter the amount you want to WithDrawal'))
        c.withdraw(amount)
    elif option.lower()=='e':
        print('Thanks For Banking with us')
        break
    else:
        print('Please Enter Valid option')