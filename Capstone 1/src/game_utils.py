def add_non_played_rounds(moves):
    if len(moves) == 10:
        return moves

    while len(moves) < 10:
        moves.append(0)

    return moves
