
class Guest:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash

    def enough_cash_for_karaoke_room(self, guest_cash, room_price):
        if guest_cash > room_price:
            return True
        else:
            return False


    def reduce_cash(self, guest, amount):
        if guest > amount:
            self.cash -= amount
        elif guest < amount:
            return "You can't afford the entry fee"