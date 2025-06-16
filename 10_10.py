class BankAccount:
    def __init__(self, name, acoount_number):
        self.name = name
        self.acoount_number = acoount_number
        self.__balance = 0

    def __str__(self):
        return f"{self.name}님의 계좌{self.acoount_number} 의 잔고는 {self.__balance}원입니다."

    def get_name(self):
        return self.name

    def get_acoount_number(self):
        return self.acoount_number

    def get___balance(self):
        return self.__balance

    def deposit(self, won):
        self.__balance += won
        print(f"{won}원이 입금되었습니다. 잔고는 {self.__balance}원입니다.")

    def withdraw(self, won):
        if self.__balance >= won:
            self.__balance -= won
        else:
            print(f"계좌 잔고는 {self.__balance}원으로 인출 요구 금액 {won}원보다 작습니다.")


account1 = BankAccount(name= '홍길동', acoount_number= '1234-0001')
print(account1)
account1.deposit(2000)
print(account1)
account1.withdraw(500)
print(account1)
account1.withdraw(5000)