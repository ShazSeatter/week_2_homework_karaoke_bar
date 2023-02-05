
class Room: 
    def __init__(self, price):
        self.price = price 
        self.songs = []
        self.guests = []
        self.max_num_guests = 5

    def add_song(self, new_song):
        return self.songs.append(new_song)
        
    def find_song_by_title(self, title):
        found_song = None
        for song in self.songs:
            if song.title == title:
                found_song = title
                break
        return found_song