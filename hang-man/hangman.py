from random import choice

# 1, create user interface
# program set search words or sayings from predefined array
# 2, game start
# get value from user arg
# evaluate character by searching word for character inserted by user
# if value is in the word build final word
# if not in the word process render sequence to draw hangman
# handle end action for winner or looser

word_store = {
    'continents': ('America', 'Africa', 'Europe', 'Australia', 'Asia')
}

game_state = {'collection': '', 'secret': '', 'user_string': {}, 'round': 0, 'status': False}


def resolve(character, state):
    i = 0
    game_state['status'] = False

    for val in game_state['secret']:
        if val.lower() == character.lower():
            game_state['user_string'][i] = character.upper()
            game_state['status'] = True
        i += 1

    if not game_state['status']:
        game_state['round'] += 1

    return game_state


def init_game():
    print('Initiating state')
    game_state.__setitem__('collection', 'continents')
    game_state.__setitem__('secret', choice(word_store.get('continents')))
    game_state.__setitem__('user_string', {i: '' for i in range(len(game_state.get('secret')))})
    game_state.__setitem__('round', -1)


def guess_character(char):
    if isinstance(char, str) & len(char) == 1:
        print('input ok')
        return resolve(char, game_state)


def get_state():
    return game_state
