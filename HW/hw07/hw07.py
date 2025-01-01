passphrase = 'gobears'

def midsem_survey(p):
    """
    You do not need to understand this code.
    >>> midsem_survey(passphrase)
    '2bf925d47c03503d3ebe5a6fc12d479b8d12f14c0494b43deba963a0'
    """
    import hashlib
    return hashlib.sha224(p.encode('utf-8')).hexdigest()


class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Nothing left to vend. Please restock.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'Please add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'Please add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    
    def __init__(self, product, price):
        self.product = product
        self.price = price
        self.balance = 0
        self.stock = 0

    def vend(self):
        if self.stock == 0:
            if self.balance > 0:
                refund = self.balance
                self.balance = 0
                return f"Nothing left to vend. Please restock. Here is your ${refund}."
            return 'Nothing left to vend. Please restock.'
        elif self.balance < self.price:
            return f"Please add ${self.price - self.balance} more funds."
        else:
            change = self.balance - self.price
            self.balance = 0
            self.stock -= 1
            if change > 0:
                return f"Here is your {self.product} and ${change} change."
            return f"Here is your {self.product}."


    def restock(self, amount):
        self.stock += amount
        return f"Current {self.product} stock: {self.stock}"

    def add_funds(self, amount):
        if self.stock == 0:
            return f"Nothing left to vend. Please restock. Here is your ${amount}."
        else:
            self.balance += amount
            return f"Current balance: ${self.balance}"
