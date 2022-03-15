import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction( Action ):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service ( KeyboardService ): An instance of KeyboardService.
    """

    def __init__( self, keyboard_service ):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service ( KeyboardService ): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point( 0, -constants.CELL_SIZE )
        self._direction2 = Point( 0, -constants.CELL_SIZE )

    def execute( self, cast, script ):
        """Executes the control actors action.

        Args:
            cast ( Cast ): The cast of Actors in the game.
            script ( Script ): The script of Actions in the game.
        """
        game_over_flag = cast.get_actors( "messages" )
        player_one = cast.get_first_actor( "player_one" )
        player_one_tail = cast.get_first_actor( "player_one_tail" )
        player_two = cast.get_first_actor( "player_two" )
        player_two_tail = cast.get_first_actor( "player_two_tail" )
        player_one_score = cast.get_first_actor( "player_one_score" )
        player_two_score = cast.get_first_actor( "player_two_score" )

        # Left.
        if self._keyboard_service.is_key_down( "a" ):
            self._direction = Point( -constants.CELL_SIZE, 0 )
            player_one.move_next()
            player_one_tail.grow_tail( 1 )
            if not game_over_flag:
                player_one_score.add_points( 1 )

        if self._keyboard_service.is_key_down( "j" ):
            self._direction2 = Point( -constants.CELL_SIZE, 0 )
            player_two.move_next()
            player_two_tail.grow_tail( 1 )
            if not game_over_flag:
                player_two_score.add_points( 1 )
        
        # Right.
        if self._keyboard_service.is_key_down( "d" ):
            self._direction = Point( constants.CELL_SIZE, 0 )
            player_one.move_next()
            player_one_tail.grow_tail( 1 )
            if not game_over_flag:
                player_one_score.add_points( 1 )
        
        if self._keyboard_service.is_key_down( "l" ):
            self._direction2 = Point( constants.CELL_SIZE, 0 )
            player_two.move_next()
            player_two_tail.grow_tail( 1 )
            if not game_over_flag:
                player_two_score.add_points( 1 )
        
        # Up.
        if self._keyboard_service.is_key_down( "w" ):
            self._direction = Point( 0, -constants.CELL_SIZE )
            player_one.move_next()
            player_one_tail.grow_tail( 1 )
            if not game_over_flag:
                player_one_score.add_points( 1 )
        
        if self._keyboard_service.is_key_down( "i" ):
            self._direction2 = Point( 0, -constants.CELL_SIZE )
            player_two.move_next()
            player_two_tail.grow_tail( 1 )
            if not game_over_flag:
                player_two_score.add_points( 1 )
        
        # Down.
        if self._keyboard_service.is_key_down( "s" ):
            self._direction = Point( 0, constants.CELL_SIZE )
            player_one.move_next()
            player_one_tail.grow_tail( 1 )
            if not game_over_flag:
                player_one_score.add_points( 1 )
        
        if self._keyboard_service.is_key_down( "k" ):
            self._direction2 = Point( 0, constants.CELL_SIZE )
            player_two.move_next()
            player_two_tail.grow_tail( 1 )
            if not game_over_flag:
                player_two_score.add_points( 1 )
        
        player_one.turn_head( self._direction )
        player_two.turn_head( self._direction2 )