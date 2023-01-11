class Dice:
    def __init__(turn, num):
        turn.a = num[0]
        turn.b = num[1]
        turn.c = num[2]
        turn.d = num[3]
        turn.e = num[4]
        turn.f = num[5]

    def turn_top(turn):
        turn.a, turn.d, turn.f, turn.c = turn.d, turn.f, turn.c, turn.a

    def turn_back(turn):
        turn.a, turn.b, turn.f, turn.e = turn.e, turn.a, turn.b, turn.f

    def turn_left(turn):
        turn.a, turn.d, turn.f, turn.c = turn.c, turn.a, turn.d, turn.f

    def turn_right(turn):
        turn.a, turn.b, turn.f, turn.e = turn.b, turn.f, turn.e, turn.a

    def show_top(turn):
        return turn.a


saikoro = list(map(int, input().split()))
tend = list(input())

dice = Dice(saikoro)

for i in tend:
    if i == "E":
        dice.turn_top()
    if i == "N":
        dice.turn_right()
    if i == "S":
        dice.turn_back()
    if i == "W":
        dice.turn_left()

print(dice.show_top())