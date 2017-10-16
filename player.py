"""
Example of a competing program. Please read the doc and the comments.
"""

""" 
playerinterface provides the functions to generate valid return values.
You do need this one. Do not delete.
"""
from playerinterface import spawn_into, move_from_to, fire_at, do_pass

from random import randint

"""
You have to provide a class Player implementing 3 methods as below
(start_game, next_move, moves_in_last_round).  You can add state and
helpers. But you cannot communicate with the external world, nor
persist anything between games. Use a web service if you want to.
"""
class Player:
    def start_game(self, boardCols, boardRows, numPlayers, playerId):
        """
        boardCols, boardRows - int, columns and rows of the board.
        numPlayers - int, the number of players in the game.
        playerId - int, your player. See moves_in_last_round.
        """
        self.boardCols = boardCols
        self.boardRows = boardRows

        col = randint(0, self.boardCols-1)
        row = randint(0, self.boardRows-1)

        """ If the return is not a spawn, you lose instantly. """
        return spawn_into(col, row);

    def next_move(self):
        """ Warning: May shoot myself. """
        col = randint(0, self.boardCols-1)
        row = randint(0, self.boardRows-1)
        
        """ Alternatives """
        """ return pass() """
        """ return spawn_into(col, row) """
        """ move_from_to(fromCol, fromRow, toCol, toRow) You need to know your current pos!"""
        return fire_at(col, row)

    def moves_in_last_round(self, moveList):
        """
        Example of a moveList (only one row shown):
        [ { actorId : 0, victimId : 1, 
            row : 0, col : 0, 
            boxWidth : 10, boxHeight : 10,
            isHit : true,
            isDestroyed : false } ]
        See the doc for details. Note: the box changes depending on th actual move.
        For misses, you'll get a box of 1, precise position. Everything indicating the
        position of an oponent is blurred. Use row, col as base and box as max.
        """
        pass