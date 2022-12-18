# Задача 4. Малашенко Борис

def compress(elems):
    res = ''
    l, i = 0, 0
    for i in range(1, len(elems)):
        if elems[i] != elems[l]:
            res += str(elems[l])
            if i - l > 1:
                res += str(i - l)
            l = i

    i += 1
    res += str(elems[l])
    if i - l > 1:
        res += str(i - l)

    return res
