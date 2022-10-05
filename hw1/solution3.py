# Задача 3. Малашенко Борис

#def squares(s):
#    return sorted([item ** 2 for item in s])

def squares(s):
    i = 0
    while s[i] < 0:
        i += 1

    pos_s = [item ** 2 for item in s[i:]]
    neg_s = [item ** 2 for item in s[:i]]
    neg_s.reverse()

    return merge(pos_s, neg_s)

