class Room:
    def __init__(self, name):
        self.name = name
        self.guest_list = []
        self.song_list = []
        self.entry_fee = 15.00

    def add_guests(self, guest):
        if len(self.guest_list) < 6:
            self.guest_list.append(guest)
        else:
            return "Limit reached only 5 allowed"

    def add_song(self, song):
        self.song_list.append(song)
        

    def group_money_check(self, guest_list):
        total_money = 0
        for guest in guest_list:
            total_money += guest.wallet
        if total_money >= self.entry_fee:
            return True
        else:
            False
