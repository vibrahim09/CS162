#!/usr/bin/env python3
from dataclasses import dataclass, field

@dataclass
class BankAccount:
    """A Class representing a Bank account
    args:
        name:(str) The name on the account.
        balance:(float) The initial balance of the account.
        ledger:(list[floats]) The ledger for the account (tracks transactions) default empty
        transaction_fee:(float) The initial transaction fee of the account. default is 0.
    """
    
    __name: str
    __balance: float = 0.0
    __ledger: list[float] = field(init=False, default_factory=list)
    __transaction_fee: float = 0.0

    def deposit(self, amount: float) -> None:
        """Deposits money to the account.
        
        args:
            amount: float: the amount to deposit. (can't be negative)
        """
        if not isinstance(amount, (float, int)):
            print("Enter monetary value.")
        elif amount < 0:
            print("Can't deposit negative money.")
        else:    
            self.__balance += amount
            self.__ledger.append(amount)
            return f"A deposit of {amount}"
        

    def withdraw(self, amount: float) -> None:
        """Withdraws money from the account. If balance becomes negative, an error is raised.
        Withdraws have a transaction fee applied to them.
        
        args:
            amount: float: the amount to withdraw.
        """
        if not isinstance(amount, (float, int)):
            print("Enter monetary value.")
        elif amount >= self.__balance:
           raise self.InsufficientFunds()
        elif amount < 0:
            print("Can't withdraw negative money.")
        else:
            amount += self.transaction_fee
            self.__balance -= amount
            self.__ledger.append(-amount)
            
    def transfer(self, other, amount: float) -> None:
        """Amount transfer from one account to the next
        
        Args:
            other: Instance of a class BankAccount.
            amount: (float) amount of money to transfer
        """
        if not isinstance(other, BankAccount):
            print("Not a  valid BankAccount")
        
        elif self.__balance <= 5:
            print("Transaction is cancelled, Insufficient funds.")
        elif amount < 0:
            print("Can't transfer negative amount.")
        elif amount == self.__balance:
            transfer_fee = 5.0
            self.__balance -= transfer_fee
            temp_balance = self.__balance
            self.__balance -= temp_balance
            other.deposit(temp_balance)
            self.__ledger.append(-(temp_balance + 5))
        elif amount + 5 >= self.__balance and self.__balance <= amount + 5:
            transfer_fee = 5.0
            self.__balance -= transfer_fee
            temp_balance = self.__balance
            self.__balance -= temp_balance
            other.deposit(temp_balance)
            self.__ledger.append(-(temp_balance + 5))
        else:
            temp_amount = amount
            transfer_fee = 5.0
            amount += transfer_fee
            self.withdraw(amount - self.__transaction_fee)
            other.deposit(temp_amount)
        
        
    
    @property
    def name(self):
        """Returns the name for the account.
        Returns:
            str: The name for the account.
        """
        return self.__name
    
    @property
    def ledger(self):
        """Returns the ledger for the account.
        
        Returns: 
            list: All the transactions for the account.
        """
        return self.__ledger
    
    @property
    def balance(self):
        """Returns the balance for the account.
        
        Returns: 
            float: The current balance for the account.
        """
        return self.__balance
    
    @property
    def transaction_fee(self):
        """Returns the transaction fee for the account.
        
        Returns: 
            float: The transaction fee.
        """
        return self.__transaction_fee
    
    def __str__(self) -> str:
        """Return a string representation of the BankAccount.
        Meant to be human readable.
        
        Returns:
            str: a string representation of the BankAccount
        """
        return f"{self.__name}, ${self.__balance}"
    
    def __repr__(self) -> str:
        """Return a string representation of the BankAccount
        This is to aid debugging
        
        Returns:
            str: a string representation of the BankAccount
        """
        return f"BankAccount(Name: {self.__name}, Balance: ${self.__balance}, Transactions:{self.__ledger}, transaction fee: ${self.__transaction_fee})"
    
    @dataclass
    class InsufficientFunds(Exception):
        """Raise when account balance is negative."""
        pass
            
            
            