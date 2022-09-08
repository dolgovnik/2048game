from game2048 import Game

def run2048():
    '''
    Function to run 2048 game in console.
    Usage: python3 run2048.py
    '''
    game = Game()
    game.push_value()
    game.push_value()
    win_banner = False #win banner shown? 
    slides = {'L': game.slide_left, 'l': game.slide_left, 'R': game.slide_right, 'r': game.slide_right,
              'U': game.slide_up, 'u': game.slide_up, 'D': game.slide_down, 'd': game.slide_down}

    game_state = game.game_state()

    while not game_state['game_over']:
        print(f'Your score is {game_state["score"]}')
        print('#################################')
        print('#################################')
        print('\n'.join([''.join(['{:8}'.format(str(x)) for x in y]) for y in game_state['field']]))
        slide = input('slide left(L, l), right(R, r), up(U, u) or down(D, d): ')
        print('#################################\n\n')
        print('\n\n')

        next_turn = slides[slide]() if slide in ('L', 'l', 'R', 'r', 'U', 'u', 'D', 'd') else None
       
        if next_turn:
            game_state = game.game_state()

            if not game_state['win']:
                #there is next turn and no win value
                game.push_value()
            elif game_state['win'] and win_banner:
                #there is next turn, win value and win banner was shown
                game.push_value()
            elif not next_turn and not game_state['win']:
                #there is no next turn and no win value
                pass
            elif game_state['win'] and not win_banner:
                #there is win value and banner not shown
                #show banner
                print('#################')
                print('#CONGRATULATION!#')
                print('#####YOU WIN!####')
                print('#################')
                print(f'YOUR SCORE IS: {game_state["score"]}')
                print('\n\n')
                #switch flag to show banner only once
                win_banner = True
                #continue the game
                game.push_value()

            #update game state before new iteration
            game_state = game.game_state()
        else:
            continue

    #show game state and game over banner
    print(f'Your score is {game_state["score"]}')
    print('#################################')
    print('#################################')
    print('\n'.join([''.join(['{:8}'.format(str(x)) for x in y]) for y in game_state['field']]))
    print('#################################\n\n')
    print('\n\n')

    print('#################')
    print('####GAME OVER####')
    print('#################')
    print(f'YOUR SCORE IS: {game_state["score"]}')
    print('\n\n')

if __name__ == '__main__':
    run2048()
