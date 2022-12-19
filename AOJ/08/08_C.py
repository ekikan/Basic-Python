count = [0 for i in range(26)]

while True:
    try:
        x = input().lower()
        for i in x:
            if ord("a") <= ord(i) <= ord("z"):
                count[ord(i) - ord("a")] += 1

    except EOFError:
        break

for j in range(ord("z") - ord("a") + 1):
    print(chr(j + ord("a")) + " : " + str(count[j]))
