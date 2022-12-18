def filter1(x: int):
    if x % 17 == 0:
        return True
    else:
        return False

def filter2(x: int):
    if '2' in str(x):
        return True
    else:
        return False

def filter3(x: int):
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False

def filter4(x: str):
    if x == ' ':
        return True
    else:
        return False

def filter5(x: str):
    if x.lower() not in ['a', 'e', 'y', 'u', 'i', 'o']:
        return True
    else:
        return False

def filter6(x: str):
    if len(x) <= 5:
        return True
    else:
        return False

def filter8(x: str):
    if x.isalpha() == True:
        return True
    else:
        return False

def filter10(pair):
    x, y = pair
    if 5 * x - 2 == y:
        return True
    else:
        return False

def filter11(x: int):
    if x % 2 == 0:
        return True
    else:
        return False

def filter12(pair):
    x, y = pair
    if x >= 0 and y >= 0:
        return True
    else:
        return False

def filter14(x: str):
    if int(x) % 2 == 0:
        return True
    else:
        return False

def main():
    string = "A simple sentence has the most basic elements that make it a sentence: \
         a subject a verb and a completed thought"

    # 1
    res1 = list(filter(filter1, range(1001)))
    
    # 2
    res2 = list(filter(filter2, range(1001)))

    # 3
    res3 = list(filter(filter3, range(10001)))
    
    # 4
    res4 = len(list(filter(filter4, string)))
    
    # 5
    res5 = ''.join(list(filter(filter5, string)))

    # 6
    res6 = list(filter(filter6, string.split(' ')))

    # 7
    res7 = dict(zip(string.split(' '), map(len, string.split(' '))))

    # 8
    res8 = list(set(filter(filter8, string)))

    # 9
    res9 = list(map(lambda x: x**2, range(101)))
    
    # 10
    coords = [(1, 1), (1, 3), (-1, -7)]
    res10 = list(map(lambda x: (x[0] ** 2 + x[1] ** 2) ** 0.5, filter(filter10, coords)))

    # 11
    res11 = list(map(lambda x: x**2, filter(filter11, range(2, 28))))
    
    # 12
    coords = [(1, 1), (1, 3), (-1, -7), (10, 20)]
    res12 = sorted(map(lambda x: (x[0] ** 2 + x[1] ** 2) ** 0.5, filter(filter12, coords)))[-1]

    # 13
    nums_first = [1, 2, 3, 5, 8]
    nums_second = [2, 4, 8, 16, 32]
    _ = list(zip(nums_first, nums_second))
    res13 = list(zip(map(lambda x: x[0] - x[1], _), map(lambda x: x[0] + x[1], _)))

    # 14
    strings = ['43141', '32441', '431', '4154', '43121', '1234']
    res14 = list(map(lambda x: str(int(x) ** 2), filter(filter14, strings)))

    # 15
    input_str = """name,Petya,Vasya,Masha,Vova grade,5,5,8,3 subject,math,language,physics,math year,1999,2000,1995,1998"""
    res15 = [dict(zip(list([row.split(',')[0] for row in input_str.split(' ')]),\
         list([row.split(',')[i + 1] for row in input_str.split(' ')]))) for i, _ in enumerate(input_str.split(' ')[0].split(',')[1:])]

    # 16
    a = [[11.9, 12.2, 12.9],
        [15.3, 15.1, 15.1], 
        [16.3, 16.5, 16.5],
        [17.7, 17.5, 18.1]]
    res16 = [sum(row[i] for row in a) for i in range(len(a[0]))]

if __name__ == "__main__":
    main()