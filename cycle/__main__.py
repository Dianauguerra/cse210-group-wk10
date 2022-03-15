from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.cycle import Cycle
from game.casting.tail import Tail
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
import constants

def main():
    
    # Create the cast.
    cast = Cast()
    cast.add_actor( "player_one", Cycle( color = constants.GREEN, position = 550 ) )
    player_one = cast.get_first_actor( "player_one" )
    tail_one = player_one.get_segments()
    cast.add_actor( "player_one_tail", Tail( color = constants.GREEN, player_segments = tail_one ) )
    cast.add_actor( "player_two", Cycle( color = constants.BLUE, position = 355 ) )
    player_two = cast.get_first_actor( "player_two" )
    tail_two = player_two.get_segments()
    cast.add_actor( "player_two_tail", Tail( color = constants.BLUE, player_segments = tail_two ) )
    cast.add_actor( "player_one_score", Score( y = 0, name = "Player One" ) )
    cast.add_actor( "player_two_score", Score( y = 800, name = "Player Two" ) )
   
    # Start the game.
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action( "input", ControlActorsAction( keyboard_service ) )
    script.add_action( "update", MoveActorsAction() )
    script.add_action( "update", HandleCollisionsAction() )
    script.add_action( "output", DrawActorsAction( video_service ) )
    
    director = Director( video_service )
    director.start_game( cast, script )

if __name__ == "__main__":
    main()