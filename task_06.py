class WrongNumberOfPlayersError(Exception):
    pass


class NoSuchStrategyError(Exception):
    pass


def rps_game_winner(players):
    if len(players) != 2:
        raise WrongNumberOfPlayersError

    winner_rules = {
        ("R", "R"): 0,
        ("R", "S"): 0,
        ("R", "P"): 1,
        ("P", "P"): 0,
        ("P", "R"): 0,
        ("P", "S"): 1,
        ("S", "S"): 0,
        ("S", "P"): 0,
        ("S", "R"): 1,
    }

    winner_index = winner_rules.get((players[0][1], players[1][1]))
    if winner_index is None:
        raise NoSuchStrategyError
    return f"{players[winner_index][0]} {players[winner_index][1]}"


rps_game_winner([["player1", "P"], ["player2", "S"]])
rps_game_winner([["player1", "P"], ["player2", "P"]])
