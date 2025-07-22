import random

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self, steps):
        self.position += steps
        if self.position > 100:
            self.position = 100
        print(f"{self.name} moves to {self.position}")

    def climb_or_slide(self, board):
        if self.position in board.snakes:
            print(f"🐍 {self.name} got bitten by a snake at {self.position}!")
            self.position = board.snakes[self.position]
            print(f"{self.name} slides to {self.position}")
        elif self.position in board.ladders:
            print(f"🪜 {self.name} climbed a ladder at {self.position}!")
            self.position = board.ladders[self.position]
            print(f"{self.name} climbs to {self.position}")

    def has_won(self):
        return self.position == 100

class Board:
    def __init__(self):
        self.snakes = {16: 6, 48: 30, 62: 19, 88: 24, 95: 56, 97: 78}
        self.ladders = {3: 22, 8: 26, 20: 38, 27: 84, 50: 91, 71: 92}

class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player("Player 1"), Player("Player 2")]
        self.current = 0

    def roll_dice(self):
        return random.randint(1, 6)

    def play(self):
        print("\n🎮 Welcome to Snake and Ladders!")
        print("Game starting with Player 1 and Player 2...\n")
        while True:
            player = self.players[self.current]
            input(f"{player.name}'s turn. Press Enter to roll dice... 🎲 ")
            dice = self.roll_dice()
            print(f"{player.name} rolled a {dice}")
            player.move(dice)
            player.climb_or_slide(self.board)

            if player.has_won():
                print(f"\n🏆 {player.name} wins the game!")
                break

            self.current = (self.current + 1) % len(self.players)



if __name__ == "__main__":
    game = Game()
    game.play()



