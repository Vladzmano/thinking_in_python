def get_score(score):
    if score == 0:
        return "Love"
    elif score == 1:
        return "15"
    elif score == 2:
        return "30"
    elif score == 3:
        return "40"
    else:
        return "Deuce"

def play_tennis_game(sequence):
    score_p1 = 0
    score_p2 = 0

    for player in sequence:
        if player == "P1":
            score_p1 += 1
        elif player == "P2":
            score_p2 += 1

        if score_p1 >= 3 and score_p2 >= 3:
            if score_p1 == score_p2:
                score_p1 = score_p2 = 3
            elif score_p1 == score_p2 + 1:
                return "Ha ganado el P1"
            elif score_p2 == score_p1 + 1:
                return "Ha ganado el P2"
            elif score_p1 == score_p2 + 2:
                return "Ha ganado el P1"
            elif score_p2 == score_p1 + 2:
                return "Ha ganado el P2"
        elif score_p1 == 4:
            return "Ha ganado el P1"
        elif score_p2 == 4:
            return "Ha ganado el P2"

        print(get_score(score_p1), "-", get_score(score_p2))

    return "El juego no ha terminado"

# Ejemplo de uso
sequence = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
result = play_tennis_game(sequence)
print(result)