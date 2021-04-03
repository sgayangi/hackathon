def make_list(num, fr):
    ls = [-1] * num
    for person in friends:
        ls[person[0] - 1] = person[1] - 1

    return ls


def invite_num(make, inv):
    num = 0
    for p in inv:
        stop = False
        per = p
        if make[per] == -1:
            num += 1
        else:
            while make[per] != -1 and not stop:
                next_per = make[per]
                make[per] = -1
                if make[next_per] == -1:
                    stop = True
                else:
                    per = next_per
                    num += 1

    return num


def con(s):
    x = int(s)
    x = x - 1
    return x


if __name__ == '__main__':
    friends = []
    n = int(input())
    for i in range(n):
        friends.append(list(map(int, input().split(' '))))
    m = int(input())
    invite = list(map(con, input().split(' ')))

    #print(friends, invite)
    #print(make_list(n, friends))
    print(invite_num(make_list(n, friends), invite))


