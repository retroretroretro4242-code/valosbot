
def calculate_elo(current, opponent, win=True):

    change = 25

    if win:
        return current + change
    else:
        return current - change
