#!/usr/bin/env python3


class BankAccount:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.ledger: list[float] = []

    def deposit(self, amount: float) -> float:
        pass

    def withdraw(self, amount: float) -> float:
        pass
