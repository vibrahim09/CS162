from velasquez_ibrahim_bank_account import BankAccount

def main():
    a1 = BankAccount("Ibrahim Velasquez", 100, 3)
    a2 = BankAccount("Joe Paris", 5000, 2)
    
    
    a1.deposit(50)
    a1.deposit(250)
    a1.deposit(65)
    print("balance after all deposits")
    print(a1.balance)
    a1.withdraw(50)
    a1.withdraw(60)
    a1.withdraw(20)
    a1.withdraw(50)

    print("Name:")
    print(a1.name)
    print()
    print("Ledger after all deposits and withdrawals")
    print(a1.ledger)
    print()
    print("Balance after withdrawals: ")
    print(a1.balance)
    print()
    print("String representation of BankAccount:")
    print(a1)
    print()
    print("rep() of BankAccount: ")
    print(a1.__repr__())
    print(a2.__repr__())

    a1.transfer(a2, 50)
    
    print()
    print("Balance after one transfer.")
    print()
    print(a1.__repr__())
    print()
    print(a2.__repr__())

    a1.transfer(a2, 219)

    print()
    print("Balance after second transfer.")
    print()
    print(a1.__repr__())
    print()
    print(a2.__repr__())
    
if __name__ == "__main__":
    main()