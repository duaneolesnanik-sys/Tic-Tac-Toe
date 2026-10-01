def get_input(board, player): 
    """Prompts the user for a valid location for play"""
    while True: 
        spot = input(f"Where will you play your piece, player {player}: ").strip() 
        if board.count(spot) == 1 and spot.isdigit(): 
            break 
        print("Invalid Location") 
    return spot

def board_print(board): 
    """Print the Board"""
    print(f"{board[0]}  | {board[1]} | {board[2]}") 
    print("-----------") 
    print(f"{board[3]}  | {board[4]} | {board[5]}") 
    print("-----------") 
    print(f"{board[6]}  | {board[7]} | {board[8]}")

def turn_player(player): 
    """Changes the Player"""
    return player.replace("X","T").replace("O","X").replace("T","O")

def take_turn(player, board):
    """Gets input and changes board"""
    spot = get_input(board, player) 
    for i in range(len(board)):
        if board[i] == spot:
            board[i] = player
    return board

def check_tie(board): 
    """Checksfor a tie"""
    tie = True 
    for spot in board: 
        if spot.isdigit(): 
            tie = False 
    return tie

def check_win(board, player): 
    """Checks if a player won"""
    win = False 
    locations = [ [ ] , [ ] , [ ] ] 
    lo2 = [] 
    for spot in range(len(board)): 
        if board[spot] == player: 
            locations[spot//3].append(spot) 
            lo2.append(spot) 
    for row in locations: 
        if len(row) == 3: 
            win = True 
    for column in range(3): 
        keep_track = [] 
        for i in range(3): 
            if locations[i].count(3*i+column) == 1: 
                keep_track.append(3*i+column) 
        if len(keep_track) == 3: 
            win = True 
    if lo2.count(4) == 1 and ((lo2.count(0)==1 and lo2.count(8)==1) or (lo2.count(2)==1 and lo2.count(6)==1)): 
        win = True 
    return win

while True:
    board = ["1","2","3","4","5","6","7","8","9"]
    player = "O"
    board_print(board)
    while True:
        player = turn_player(player)
        board = take_turn(player, board)
        board_print(board)
        if check_win(board, player):
            result = f"The Winner is player {player}!"
            break
        elif check_tie(board):
            result = "Tie Game"
            break
    print(result)
    if not input("Enter 'p' to play again: ").strip().lower() == "p":
        print("Have a good day.")
        break

