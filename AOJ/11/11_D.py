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

    def same_saikoro(turn, ary):
        if turn.a == ary[0] and turn.b == ary[1] and turn.c == ary[2] and turn.d == ary[3] and turn.e == ary[4] and turn.f == ary[5]:
            return True

    def sameOne (turn, ary):
        for _ in range(2):
            for _ in range(3):
                for _ in range(4):
                    if turn.same_saikoro(ary):
                        return True
                    turn.turn_top()
                turn.turn_back()
            turn.turn_left()
            turn.turn_right()
        return False
n = int(input())
saikoro = []
for i in range(n):
    saikoro.append(list(map(int, input().split())))

for i in range(n-1):
    for j in range(i+1, n):
        dice = Dice(saikoro[i])
        if dice.sameOne(saikoro[j]):
            print('No')
            break
    else:
        continue
    break
else:
    print('Yes')