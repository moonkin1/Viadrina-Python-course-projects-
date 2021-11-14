import random

class Coin:

    def flip(self):
        self.fl = random.choice([-1,1])
        return self.fl

class Dice:

    def roll(self):
        self.rl = random.randint(1,6)
        return self.rl

class Player:
    position = 0

    def update_position(self):
        Player.position += Dice().roll()*Coin().flip()
        return (Player.position)

    def make_turn(self):
        Player().update_position()


class Game():
    def play(self):
        for i in range(20):
            Player().make_turn()
        return Player.position



