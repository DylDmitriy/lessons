def checkio(game_result):
    return "D" or "X" or "O"


if __name__ == "__main__":
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "победил X"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "победил O"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "победил D"
