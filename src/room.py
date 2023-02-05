
class Room: 
    def __init__(self, price):
        self.price = price 
        self.songs = []
        self.guests = []
        self.max_num_guests = 5

    def add_song(self, new_song):
        self.songs.append(new_song)