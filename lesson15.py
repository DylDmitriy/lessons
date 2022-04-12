def checkio_my(net):
    cash = [str(net[0][0] + net[0][1] + net[0][2]),
            str(net[1][0] + net[1][1] + net[1][2]),
            str(net[2][0] + net[2][1] + net[2][2]),
            str(net[0][0] + net[0][1] + net[0][2]),
            str(net[0][1] + net[1][1] + net[2][1]),
            str(net[0][2] + net[1][2] + net[2][2]),
            str(net[0][0] + net[1][1] + net[1][1]),
            str(net[0][2] + net[1][1] + net[2][0])]
    for i in cash:
        if i == "XXX":
            return "X"
        elif i == "OOO":
            return "O"
        else:
            return "D"
def checkio_best_solution(result):
    rows = result
    cols = map(''.join, zip(*rows))
    diags = map(''.join, zip(*[(r[i], r[2 - i]) for i, r in enumerate(rows)]))
    lines = rows + list(cols) + list(diags)

    return 'X' if ('XXX' in lines) else 'O' if ('OOO' in lines) else 'D'

if __name__ == '__main__':
    assert checkio_my([
        u"X.O",
        u"XX.",
        u"XOO"]) == "X", "Победил X"
    assert checkio_my([
        u"OO.",
        u"XOX",
        u"XOX"]) == "O", "Победил O"
    assert checkio_my([
        u"OOX",
        u"XXO",
        u"OXX"]) == "D", "Ничья"
