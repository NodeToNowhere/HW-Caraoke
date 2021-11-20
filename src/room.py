class Room:
    def __init__(self, name):
        self.name = name
        self.occupied = bool
        self.guest_list = []

    def add_guests(self, guest):
        if len(self.guest_list) < 5:
            self.guest_list.append(guest)
        else:
            return "Limit reached"
