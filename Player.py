
class Player:
    def __init__(self):
        self.type = "X"
        self.name = "Player1"

    def insert_player_name(self,name):
        self.name = name

    def get_player_name(self):
        return self.name

    def get_player_symbol(self):
        return self.type
