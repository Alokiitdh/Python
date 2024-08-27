class Atm:
    #constructor: class ke andar ka code exactly kab execute hota hai jab oska object create hotahai
    def __init__(self):
        self.__pin = ""
        self.__balance = 0

        self.menu()# no need to pass self here 

    def menu(self):
        while True:
            user_input = input("""
                  Hello how would you like to proceed?
                  1. Enter 1 to create pib
                  2. Enter 2 to deposit
                  3. Enter 3 to withdraw
                  4. Enter 4 to check balance
                  5. Enter 5 to exit                                               
                 """)
            if user_input == '1':
                self.create_pin()
            elif user_input == '2':
                self.deposit()
            elif user_input == '3':
                self.withdraw()
            elif user_input == '4':
                self.check_balance()
            else:
                print('Byeee')   
    def create_pin(self):
        self.__pin = input('Enter Your PIN: ')
        print('Pin Successfully created')
    def deposit(self):
        temp = input('Enter your Pin: ')
        if temp == self.__pin:
            amount = int(input('Enter Amount: '))
            self.__balance = self.__balance + amount
            print('Deposit Successuful')
        else:
            print('Invalid pin')   
    def withdraw(self):
        temp = input('Enter your Pin: ')
        if temp == self.__pin:
            amount = int(input('Enter Amount: '))
            if amount < self.__balance:
                self.__balance-= amount
                print('Operation successful')
            else:
                print('Transaction Failed: Insufficient FUNDS!!!')
        else:
            print('Invalid Pin')
     
    def check_balance(self):
        temp = input('Enter your Pin: ')
        if temp == self.__pin:
            print(self.__balance)
        else:
            print('invalid Pin')


sbi =Atm()
