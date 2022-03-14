import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction( Action ):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the player_one collides
    with player_two, or the players collide with they segments, or the game is over.

    Attributes:
        _is_game_over ( boolean ): Whether or not the game is over.
    """

    def __init__( self ):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._players = [ "player_one", "player_two" ]

    def execute( self, cast, script ):
        """Executes the handle collisions action.

        Args:
            cast ( Cast ): The cast of Actors in the game.
            script ( Script ): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_players_collision( cast )
            self._handle_segment_collision( cast )
            self._handle_game_over( cast )

    def _handle_players_collision( self, cast ):
        """Sets the game over flag if the players collides with each other.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        actor_one = cast.get_first_actor( "player_one" )
        actor_two = cast.get_first_actor( "player_two" )
        head_one= actor_one.get_segments()[ 0 ]
        head_two= actor_two.get_segments()[ 0 ]
        segments_one = actor_one.get_segments()[ 1: ]
        segments_two = actor_two.get_segments()[ 1: ]
    
        for segment in segments_one:
            if head_two.get_position().equals( segment.get_position() ):
                self._is_game_over = True
        
        for segment in segments_two:
            if head_one.get_position().equals( segment.get_position() ):
                self._is_game_over = True
    
    def _handle_segment_collision( self, cast ):
        """Sets the game over flag if the players collides with one of its segments.
        
        Args:
            cast ( Cast ): The cast of Actors in the game.
        """
        for player in self._players:
            actor = cast.get_first_actor( player )
            head = actor.get_segments()[ 0 ]
            segments = actor.get_segments()[ 1: ]
        
            for segment in segments:
                if head.get_position().equals( segment.get_position() ):
                    self._is_game_over = True
        
    def _handle_game_over( self, cast ):
        """Shows the 'game over' message and turns the players white if the game is over.
        
        Args:
            cast ( Cast ): The cast of Actors in the game.
        """
        if self._is_game_over:
            player_one = cast.get_first_actor( "player_one" )
            player_two = cast.get_first_actor( "player_two" )
            player_one.set_color( constants.WHITE )
            player_two.set_color( constants.WHITE )
            segments = player_one.get_segments()
            segments2 = player_two.get_segments()

            x = int( constants.MAX_X / 2 )
            y = int( constants.MAX_Y / 2 )
            position = Point( x, y )

            message = Actor()
            message.set_text( "Game Over! Thank you for playing!" )
            message.set_position( position )
            cast.add_actor( "messages", message )

            # Player one.
            for segment in segments:
                segment.set_color( constants.WHITE )

            # Player two.
            for segment in segments2:
                segment.set_color( constants.WHITE )