import math
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

    def __repr__(self) -> str:
        def format_ledger_item(item):
            return f'{str(item["description"][:23]).ljust(23)} {str(item["amount"]).rjust(6)}'

        lines_list = [format_ledger_item(x) for x in self.ledger]
        lines_list.insert(0, str(self.name).center(30, '*'))
        lines_list.append(f'Total: {self.get_balance()}')

        return '\n'.join(lines_list)

def create_spend_chart(categories):
    tot_amount = sum([x.get_balance() for x in categories])

    def round_up_to_nearest_10(num):
        return math.ceil(num / 10) * 10

    cat_list = [ {"name": c.name, "pc": round_up_to_nearest_10(float((c.get_balance() / tot_amount) * 100)) } for c in categories]
    print(cat_list[0])

    bars = [ f'{i}|'.rjust(4) for i in range(100, -1, -10)]
    return '\n'.join(bars)