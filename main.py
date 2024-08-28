from utils import initialize as init, menu, moves


def start_game():
    game_end = False
    toggle = True
    menu.start()
    current_move = moves.get_move(toggle)
    if(moves.validate_move(current_move)):
        print("Game Successfully Started")
    
    while(not game_end):
        toggle = not toggle
        current_move = moves.get_move(toggle)
        if(current_move == 'Q'):
            print("Thanks for Playing")
            game_end = True
            return
        if(moves.validate_move(current_move)):
            print("This turn is also valid")
            
def main():
    print("Hello World")
    board = init.setup()
    init.print_board(board)
    start_game()
    print("GGS")

    
main()