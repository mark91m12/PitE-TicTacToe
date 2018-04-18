
class Player:
    def __init__(self):
        self.type = "X"
        self.name = "Player1"

    def insert_player_name(self):
        print ("Hello player, you are welcome....")
        name = input("Insert Your Name \n")
        self.set_player_name(name)
        return self.name

    def get_player_name(self):
        return self.name

    def set_player_name(self, name):
        self.name = name

    def get_player_symbol(self):
        return self.type
