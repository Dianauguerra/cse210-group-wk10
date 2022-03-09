from game.casting.player_one_score import Player_one_score
from game.shared.point import Point

class Player_two_score( Player_one_score ):
    """
    A record of points made or lost for player two. 
    
    The responsibility of Score is to keep track of the points the player has earned by moving.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points ( int ): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        self._position = Point( 800, 0 )


    def add_points( self, points ):
        """Adds the given points to the score's total points.
        
        Args:
            points ( int ): The points to add.
        """
        self._points += points
        self.set_text( f"Player Two: {self._points}" )