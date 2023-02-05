
class Room: 
    def __init__(self, price):
        self.price = price 
        self.songs = []
        self.guests = []
        # self.num_of_guests_in_room = 0
        self.entry_fee = 5

    def add_song(self, new_song):
        return self.songs.append(new_song)
    
    def add_guest(self, new_guest):
        return self.guests.append(new_guest)
        
    def num_guests_in_room(self):
        self.num_guests_in_room += 1


    def find_song_by_title(self, title):
        found_song = None
        for song in self.songs:
            if song.title == title:
                found_song = title
                break
        return found_song
    
    # Return length of the guest list 

    def guest_count(self):
        return len(self.guests)
    

    def max_num_of_guests(self, total_guests_in_room):
        if total_guests_in_room >= 3:
            return "Too Many Guests are checking in"
   

    def remove_guest(self, guest_to_remove):
        self.guests.remove(guest_to_remove)


    def guest_fav_song(self, song):
        for fav_song in self.songs:
            if fav_song.title == song:
                return "Whoo!"
