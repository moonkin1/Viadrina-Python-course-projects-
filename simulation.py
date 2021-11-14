from randomWalk import Game
from randomWalk import Player
gm = Game()

def start_simulation():
    total = []
    for i in range(100):
        gm.play()
        total.append(gm.play())
        Player.position = 0
    average_result = sum(total)/len(total)
    print("This is the average position after 100 games: ", average_result)

start_simulation()