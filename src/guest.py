class Guests:
    def __init__(self, name, wallet, favorite_song):
        self.name = name
        self.wallet = wallet
        self.favorite_song = favorite_song


    def guest_check_song_list(self, guest, song_list):
        for song in song_list:
            if guest.favorite_song == song.name:
                return (f"{guest.name}: Oh yeah! {song.name} is my jam!")
            else:
                return (f"{guest.name}: This music sucks...")