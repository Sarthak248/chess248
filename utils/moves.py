def get_move(white_move):
    if(white_move):
        # print("WHITE:")
        move = input("WHITE:")
        return move
    move = input("BLACK:")
    return move

def validate_move(move):
    print("Validating Move..." + move)
    isValid = True

    return isValid