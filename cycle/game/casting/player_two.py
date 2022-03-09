import constants
from game.casting.player_one import Player_one
from game.casting.actor import Actor
from game.shared.point import Point

class Player_two( Player_one ):
    """
    A cycle used for player two.
    
    The responsibility of Player_two is to move itself.

    Attributes:
        _segments ( list ): The quantity of segments.
    """
    def __init__( self ):
        super().__init__()
        self._segments = []
        self._prepare_body()
    
    def grow_tail( self, number_of_segments ):
        """Updates the segments for the player.
        
        Args:
            number_of_segments ( int ): The quantity of segments to add.
        """
        for i in range( number_of_segments ):
            tail = self._segments[ -1 ]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add( offset )
            
            segment = Actor()
            segment.set_position( position )
            segment.set_velocity( velocity )
            segment.set_text( "#" )
            segment.set_color( constants.BLUE )
            self._segments.append( segment )

    def _prepare_body( self ):
        """ Constructs the player_one's body. """
        x = int( constants.MAX_X / 4 )
        y = int( constants.MAX_Y / 4 )

        for i in range( constants.PLAYERS_LENGTH ):
            position = Point( x - i * constants.CELL_SIZE, y )
            velocity = Point( 1 * constants.CELL_SIZE, 0 )
            text = "@" if i == 0 else "#"
            color = constants.YELLOW if i == 0 else constants.BLUE
            
            segment = Actor()
            segment.set_position( position )
            segment.set_velocity( velocity )
            segment.set_text( text )
            segment.set_color( color )
            self._segments.append( segment )