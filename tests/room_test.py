import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest
#from src.karaoke_bar import KaraokeBar


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(20)

# GETTING PRICE OF RENTING ROOM 
    def test_price_of_room(self):
        expected = 20
        actual = self.room.price
        self.assertEqual(expected, actual)

# LOOKING AT LIST OF SONGS
    def test_has_songs(self):
        expected = []
        actual = self.room.songs
        self.assertEqual(expected, actual)

# LOOKING AT LIST OF GUESTS 
    def test_has_guests(self):
        expected = []
        actual = self.room.guests
        self.assertEqual(expected, actual)

# # # LOOKING AT THE STARTING POINT FOR THE ROOM 
#     def test_num_of_guests_in_room_starts_at_0(self):
#         expected = 0
#         actual = self.room.num_of_guests_in_room
#         self.assertEqual(expected, actual)


# ADDING SONGS TO SONG LIST IN ROOM 
    def test_add_songs_to_room(self):
        song = Song("Hound Dog", "Elvis Presley", "Rock")
        self.room.add_song(song)
        expected = song
        actual = self.room.songs[0]
        self.assertEqual(expected, actual)

# ADDING GUESTS TO GUSTS LIST IN ROOM 
    def test_add_guests_to_room(self):
        guest = Guest("John Smith", 50)
        self.room.add_guest(guest)
        expected = guest
        actual = self.room.guests[0]
        self.assertEqual(expected, actual)

# FINDING SONG BY TITLE - NOT FOUND 
    def test_can_find_song_by_title__not_found(self):
        expected = None
        actual = self.room.find_song_by_title("Hound Dog")
        self.assertEqual(expected, actual)
    
# FINDING SONG BY TITLE - FOUND (ADDING SONG FIRST THEN LOOKING)
    def test_can_find_song_by_title__found(self):
        song = Song("Hound Dog", "Elvis Presley", "Rock")
        self.room.add_song(song)
        expected = song.title
        actual = self.room.find_song_by_title("Hound Dog")
        self.assertEqual(expected, actual)

# CHECKING GUESTS IN - max num of rooms need to decrease 
    # def test_check_in_guest(self):
    #     guest = Guest("John Smith", 50)
    #     self.room.add_guest(guest) #[John smith]
    #     expected = self.room.num_of_guests_in_room
    #     actual = self.room.check_in_guest()
    #     self.assertEqual(expected, actual)

# LOOKING AT THE LENGTH OF THE GUEST LIST 
    def test_room_guest_count(self):
         guest = Guest("John Smith", 50)
         self.room.add_guest(guest)
         expected = 1
         actual = self.room.guest_count() #returns length of guest list
         self.assertEqual(expected, actual)

# TOO MANY GUESTS TRYING TO CHECK IN
    def test_too_many_guests_checking_in(self):
        guest_1 = Guest("John Smith", 50)
        guest_2 = Guest("David Doe", 20)
        guest_3 = Guest("Jane Doe", 30)
        guest_4 = Guest("Patrick Macdonald", 40)
        self.room.add_guest(guest_1)
        self.room.add_guest(guest_2)
        self.room.add_guest(guest_3)
        self.room.add_guest(guest_4) # [John Smith, David Doe, Jane Doe, Patrick Macdonald]
        expected = "Too Many Guests are checking in"
        actual = self.room.max_num_of_guests(4)
        self.assertEqual(expected, actual)
        self.assertEqual(4, self.room.guest_count())


# CHECKING OUT GUEST FROM ROOM 
    def test_check_out_guest(self):
        guest_1 = Guest("John Smith", 50)
        guest_2 = Guest("John Doe", 50)
        self.room.add_guest(guest_1)
        self.room.add_guest(guest_2) # [John Smith, John Doe]
        self.room.remove_guest(guest_1)
        expected = 1 # [John Doe]
        actual = self.room.guest_count() # len of guest = 1
        self.assertEqual(expected, actual)

# GUESTS FAVORITE SONG
    def test_guest_fav_song__is_listed(self):
        song_1 = Song("Hound Dog", "Elvis Presley", "Rock")
        song_2 = Song("If I Can Dream", "Elvis Presley", "Rock")
        guest = Guest("John Smith", 50)
        self.room.add_song(song_1) # ["Hound Dog", "If I Can Dream"]
        self.room.add_song(song_2) # 
        self.room.add_guest(guest) # [John Smith]
        expected = "Whoo!"
        actual = self.room.guest_fav_song("If I Can Dream")
        self.assertEqual(expected, actual)

