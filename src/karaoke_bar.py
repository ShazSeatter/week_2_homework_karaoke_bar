
class KaraokeBar:
    def __init__(self, name, total_cash):
        self.name = name
        self.total_cash = total_cash
        # total rooms in bar 5 

    def increase_total_cash(self, amount, entry_fee):
        self.total_cash += (amount + entry_fee)
