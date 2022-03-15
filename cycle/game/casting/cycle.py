import constants
from game.casting.actor import Actor
from game.shared.point import Point

class Cycle( Actor ):
    """
    A cycle used for player one.
    
    The responsibility of Player_one is to move itself.

    Attributes:
        _segments ( list ): The quantity of segments.
    """
    def __init__( self, color, position ):
        super().__init__()
        self._segments = []
        self._color = color
        self._start_position = position
        self._prepare_body()

    def get_segments( self ):
        """Gets the player_one's segments.
        
        Returns:
            _segments: The player_one's segments.
        """
        return self._segments

    def move_next( self ):
        """Moves the cycle to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        """
        # Move all segments.
        for segment in self._segments:
            segment.move_next()

        # Update velocities.
        for i in range( len( self._segments ) - 1, 0, -1 ):
            trailing = self._segments[ i ]
            previous = self._segments[ i - 1 ]
            velocity = previous.get_velocity()
            trailing.set_velocity( velocity )

    def get_head( self ):
        """Gets the player_one's head.
        
        Returns:
            Head: The player_one's head.
        """
        return self._segments[0]

    def turn_head( self, velocity ):
        """Move the player_one's head.
        
        Args:
            velocity ( int ): The new velocity to set for head.
        """
        self._segments[ 0 ].set_velocity( velocity )
    
    def _prepare_body( self ):
        """ Constructs the player_one's body. """
        x = int(constants.MAX_Y / 2)
        y = self._start_position

        for i in range( constants.PLAYERS_LENGTH ):
            position = Point( y, x + i * constants.CELL_SIZE )
            velocity = Point( 0, 1 * -constants.CELL_SIZE )
            text = "@" if i == 0 else "#"
            color = constants.YELLOW if i == 0 else self._color
            
            segment = Actor()
            segment.set_position( position )
            segment.set_velocity( velocity )
            segment.set_text( text )
            segment.set_color( color )
            self._segments.append( segment )