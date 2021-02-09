import PySimpleGUI as sg

# Each cell in my tic-tac-toe grid has a number, and these are all the winning 
# combinations
winning_comb_list = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(7,5,3)]

# Lists where each player's moves will be recorded
player_1 = []
player_2 =[]

# Initial settings before starting the game. First player will start with an X
current_player = 'X'
current_text = 'Player1 turn'
game_counter = 1 # Needed to count the moves in order to catch the draw scenario
game_stopped = False
p1_win = 'Player1 Win'
p2_win = 'Player2 Win'

layout = [
    [sg.Text("Tic Tac Toe Game by Greg")], 
    [sg.Text(f'{current_text}', key='player')],
    [sg.Button(' ', size=(4, 2), key=(a), pad=(0, 0))
     for a in range(1,4)],
    [sg.Button(' ', size=(4, 2), key=(b), pad=(0, 0))
     for b in range(4,7)],
    [sg.Button(' ', size=(4, 2), key=(c), pad=(0, 0))
     for c in range(7,10)],
    [sg.Button("EXIT")],
    [sg.Button("RESTART")]
        
    ]

# Create the window
window = sg.Window("Tic Tac Toe by Greg", layout, margins=(100, 50))

# This function does most of the work:
# Switches players after each move
# Checks for winning sequences and announces the winner (if there is one)
def switch_players(number):
    global current_player
    global current_text
    global game_stopped

    if (current_player == 'X'):
        player_1.append(number) # Adds the current move to the player's record
        for item in winning_comb_list:  # checks for winning sequence
            if item[0] in player_1 and item[1] in player_1 and item[2] in player_1:
                window.Element(key='player').update(p1_win)
                game_stopped = True
        current_player = 'O'
        current_text = 'Player2 turn'
    else:
        current_player = 'X'
        player_2.append(number)  
        for item in winning_comb_list: 
            if item[0] in player_2 and item[1] in player_2 and item[2] in player_2:
                window.Element(key='player').update(p2_win)
                game_stopped = True
        current_text = 'Player1 turn'

# Create an event loop
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'EXIT'): # End program if user closes window or
        break                            # presses the EXIT button
       
    if event in range(1,10):
        window[event].update(current_player)
        switch_players(event)
        game_counter += 1
        if game_stopped == False:
            if game_counter < 10:
                window.Element(key='player').update(current_text)
            else:
                window.Element(key='player').update('It\'s a draw')
        else:
            for number in range(1,10):
                window.Element(key=number).update(disabled=True)
        window.Element(key=event).update(disabled=True) #dissables the pressed button so it can't be pressed the second time (e.g. players can't use the same cell twice)

    if event == 'RESTART':
        for i in range(1,10):
            window.Element(key=i).update('', disabled=False)
        current_player = 'X'
        current_text = 'Player 1 turn'
        game_stopped = False
        window.Element(key='player').update(current_text)
        player_1 = []
        player_2 = []
        game_counter = 1

    # print(window[event].Key)   

window.close()

