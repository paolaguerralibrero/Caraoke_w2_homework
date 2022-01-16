
class Room:
    def __init__(self, space, fee):
        self.guests = []
        self.songs = []
        self.space = space
        self.fee = fee
        
    def add_guest(self, guests):
        self.guests.append(guests)
        
    def check_out_guest(self, guests):
        self.guests.pop(0)

    def add_song(self, song):
        self.songs.append(song)

    def guest_count(self):
        return len(self.guests)

    def room_no_space(self):
        if self.space <= self.guest_count():
            return "Room is full"   
        else:
            return "Come in"

    def can_affod_entry_fee(self, guest):
        if guest.wallet >= self.fee:
            return True
        else:
            return False