from game.casting.actor import Actor

class Tail( Actor ):
    """
    A cycle used for player one.
    
    The responsibility of Player_one is to move itself.

    Attributes:
        _segments ( list ): The quantity of segments.
    """
    def __init__( self, color, player_segments ):
        super().__init__()
        self._segments = player_segments
        self._color = color

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
            segment.set_color( self._color )
            self._segments.append( segment )