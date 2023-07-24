class Bank:
    __bank_name = 'Bro Bank'
    __interest_rate = 10

    #this initializes the bank account properties
    def __init__(self, f_name, l_name, user_age, user_balance=0):
        self.first_name = f_name
        self.last_name = l_name
        self.age = user_age
        self.balance = user_balance
    
    #this method checks the user current balance
    def check_balance(self):
        print(f'Your current balance is {self.balance}')
    
    #this method allows user to deposit balance
    def deposit_amount(self, deposit_amount):
        if deposit_amount <= 0:
            print('Enter valid amount.')
        else:
            self.balance = self.balance + deposit_amount
            self.check_balance()
    
    #this method allows user to withdraw balance
    def withdraw_balance(self, withdraw_amount):
        if withdraw_amount <=0:
            print('Enter valid amount.') 
        else:   
            if withdraw_amount > self.balance:
                self.check_balance()
                print(f'You can withdraw only upto {self.balance}')
            else:
                self.balance = self.balance - withdraw_amount
                self.check_balance()
    
    def get_account_details(self):
        print(f'Account Details : {self.first_name} {self.last_name}')

    @classmethod
    def get_interest_rate(cls):
        print(f"Bank's current interest rate is {Bank.__interest_rate}") 

    @classmethod
    def set_interest_rate(cls, new_interest_rate):
        Bank.__interest_rate = new_interest_rate
        Bank.get_interest_rate()

    #this method returns the bank name
    @classmethod
    def get_bank_name(cls):
        return Bank.__bank_name
    
    #this method prints the bank's holiday list
    #returns None
    @staticmethod
    def print_bank_holiday_list():
        print('Every saturday is a holiday')
        print('Dashain holiday lasts from Ghatasthapana to Purnima.')

user = None
while True:
    print('*' * 20)
    print(f'Welcome to {Bank.get_bank_name()}')
    
    user_choice = input('Enter 1 to open account. \nEnter 2 to check balance. \nEnter 3 to deposit balance. \nEnter 4 to withdraw balance. \nEnter 5 to check bank holiday list. \nEnter 6 to get current interest rate. \nEnter 7 to change interest rate. ')
    if user_choice == '1':
        first_name = input('Enter your first name: ')
        last_name = input('Enter your last name: ')
        age = int(input('Enter your age : '))

        user = Bank(first_name, last_name, age)

        print('YAAAAAAAAAAYYYYYY')
        print('An account has been created.')
        user.get_account_details()
    
    elif user_choice == '2' and user is not None:
        user.check_balance()
    
    elif user_choice == '3' and user is not None:
        deposit_amount = int(input('Enter the amount you want to deposit: '))
        user.deposit_amount(deposit_amount)
    
    elif user_choice == '4' and user is not None:
        withdraw_amount = int(input('Enter the amount you want to withdraw: '))
        user.withdraw_balance(withdraw_amount)

    elif user_choice == '5':
        Bank.print_bank_holiday_list()

    elif user_choice == '6':
        Bank.get_interest_rate()
    
    elif user_choice == '7':
        print('!!!!!!!!WARNING!!!!!!!!!')
        print('Interest rate cannot be changes without the permission of the board committee.')
        print('If someone is found changing the interest rate, he will be punished accoring to the bank law.')

        print('Are your sure you want to continue')
        want_to_continue = input('Enter 0 to exit. \nEnter 1 to continue: ')

        if want_to_continue == '0':
            continue
        
        elif want_to_continue == '1':
            new_rate = int(input('Enter new interest rate: '))
            Bank.set_interest_rate(new_rate)
    
    elif user is None:
        print('Please create an account first')
        continue
    else:
        print('Invalid user choice')
        continue