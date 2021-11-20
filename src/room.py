class Room:
    def __init__(self, name):
        self.name = name
        self.occupied = bool
        self.guest_list = []

    def add_guests(self, guest):
        if len(self.guest_list) < 5:
            self.guest_list.append(guest)
            # print(self.guest_list) # *delete later*
        else:
            return "Limit reached only 5 allowed"
