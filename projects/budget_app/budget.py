class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def get_balance(self):
        return 0 if len(self.ledger) == 0 else sum([x["amount"] for x in self.ledger])

    def check_funds(self, amount):
        return True if amount >= self.get_balance() else False

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=''):
        if self.check_funds(amount) == True:
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def transfer(self, amount, category):
        if self.check_funds(amount) == True:
            self.ledger.append({"amount": -amount, "description": f'Transfer to {category.name}'})
            category.ledger.append({"amount": amount, "description": f'Transfer from {self.name}'})
            return True
        else:
            return False


def create_spend_chart(categories):
    pass