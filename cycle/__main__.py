from game.casting.cast import Cast
from game.casting.player_one_score import Player_one_score
from game.casting.player_two_score import Player_two_score
from game.casting.cycle import Cycle
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
    cast.add_actor( "player_two", Cycle( color = constants.BLUE, position = 355 ) )
    cast.add_actor( "player_one_score", Player_one_score() )
    cast.add_actor( "player_two_score", Player_two_score() )
   
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