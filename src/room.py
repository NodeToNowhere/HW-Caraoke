class Room:
    def __init__(self, name):
        self.name = name
        self.occupied = bool
        self.guest_list = []
        self.song_list = []
        self.max_time = 1800

    def add_guests(self, guest):
        if len(self.guest_list) < 6:
            self.guest_list.append(guest)
        else:
            return "Limit reached only 5 allowed"

    def add_song(self, song):
        self.song_list.append(song)
        print(self.song_list)