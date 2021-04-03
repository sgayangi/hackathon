def can_fly(px, py, string):
    l = 0
    r = 0
    u = 0
    d = 0
    for i in string:
        if i == "L":
            l += 1
        elif i == "R":
            r += 1
        elif i == "U":
            u += 1
        else:
            d += 1

    print(l, r, u, d)
    can_x = False
    can_y = False
    if px > 0:
        if r >= px:
            can_x = True

    elif px == 0:
        can_x = True

    else:
        if l >= -px:
            can_x = True

    if py > 0:
        if u >= py:
            can_y = True
    elif py == 0:
        can_y = True
    else:
        if d >= -py:
            can_y = True

    if can_y and can_x:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    t = int(input())
    inputs = []
    for i in range(t):
        [px, py] = list(map(int, input().split(' ')))
        string = input()
        inputs.append([px, py, string])

    for i in inputs:
        print(can_fly(i[0], i[1], i[2]))
