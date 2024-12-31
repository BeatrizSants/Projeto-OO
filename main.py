from package.models.game import Game
from package.models.cheese_trap import Cheese, Trap
if __name__ == "__main__":
    trap = Trap(None)
    cheese=Cheese(trap)
    trap.cheese = cheese
    game = Game(cheese, trap)
    game.run()
