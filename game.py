import random

class Board:
    def init(self):
        self.snakes = {
            16: 6, 47: 26, 49: 11, 56: 53,
            62: 19, 64: 60, 87: 24, 93: 73,
            95: 75, 98: 78
        }
        self.ladders = {
            1: 38, 4: 14, 9: 31, 21: 42,
            28: 84, 36: 44, 51: 67, 71: 91,
            80: 100
        }

    def check_position(self, position):
        if position in self.snakes:
            print(f"🐍 Snake! Down from {position} to {self.snakes[position]}")
            return self.snakes[position]
        elif position in self.ladders:
            print(f"🪜 Ladder! Up from {position} to {self.ladders[position]}")
            return self.ladders[position]
        return position

class Player:
    def init(self, name):
        self.name = name
        self.position = 0

    def move(self, value):
        prev = self.position
        self.position += value
        if self.position > 100:
            self.position = prev
            print(f"{self.name} needs exact roll to reach 100. Still at {self.position}")
        else:
            print(f"{self.name} moved to {self.position}")

class Game:
    def init(self, player_names):
        self.board = Board()
        self.players = [Player(name) for name in player_names]
        self.dice = [1, 2, 3, 4, 5, 6]
        self.winner = None

    def roll_dice(self):
        return random.choice(self.dice)

    def play(self):
        print("\n🎯 Welcome to Snake & Ladder Game 🎯")
        print("First to reach exactly 100 wins!\n")

        while not self.winner:
            for player in self.players:
                input(f"{player.name}'s turn. Press ENTER to roll the dice...")
                roll = self.roll_dice()
                print(f"{player.name} rolled a 🎲 {roll}")
                player.move(roll)
                player.position = self.board.check_position(player.position)
                if player.position == 100:
                    self.winner = player
                    break

        print(f"\n🏆 {self.winner.name} WINS the game! Congratulations! 🎉")
if __name__ == "__main__":
    names = input("Enter player names separated by commas: ").split(",")
    names = [n.strip().capitalize() for n in names if n.strip()]
    if len(names) < 2:
        print("You need at least 2 players to start the game.")
    else:
        game = Game(names)
        game.play()
