from game.scripting.action import Action

class DrawActorsAction( Action ):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service ( VideoService ): An instance of VideoService.
    """

    def __init__( self, video_service ):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service ( VideoService ): An instance of VideoService.
        """
        self._video_service = video_service

    def execute( self, cast, script ):
        """Executes the draw actors action.

        Args:
            cast ( Cast ): The cast of Actors in the game.
            script ( Script ): The script of Actions in the game.
        """
        player_one_score = cast.get_first_actor( "player_one_score" )
        player_two_score = cast.get_first_actor( "player_two_score" )
        player_one = cast.get_first_actor( "player_one" )
        player_two = cast.get_first_actor( "player_two" )
        segments = player_one.get_segments()
        segments2 = player_two.get_segments()
        messages = cast.get_actors( "messages" )

        self._video_service.clear_buffer()
        self._video_service.draw_actors( segments )
        self._video_service.draw_actors( segments2 )
        self._video_service.draw_actor( player_one_score )
        self._video_service.draw_actor( player_two_score )
        self._video_service.draw_actors( messages, True )
        self._video_service.flush_buffer()