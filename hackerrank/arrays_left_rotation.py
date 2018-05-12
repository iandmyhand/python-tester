def array_left_rotation3(a, n, k):
    # 7, 9, 1 2 3 4 5 6 7
    # 9 % 7 = 2, 7-2=5
    idx_0_to = n - (k % n)
    tmp_arr = [None] * n
    idx_to = idx_0_to
    idx_from = 0
    idx_tmp = 0
    idx_tmp2 = 0
    while n > idx_to and idx_from < idx_0_to:
        tmp_arr[idx_tmp] = a[idx_to]
        a[idx_to] = a[idx_from]
        idx_to += 1
        idx_from += 1
        idx_tmp += 1
    if n > idx_to:
        while n > idx_to:
            tmp_arr[idx_tmp] = a[idx_to]
            a[idx_to] = tmp_arr[idx_tmp2]
            idx_to += 1
            idx_tmp += 1
            idx_tmp2 += 1
    print(str(tmp_arr[idx_tmp2]))
    idx_to = 0
    while idx_0_to > idx_to and tmp_arr[idx_tmp2] is not None:
        a[idx_to] = tmp_arr[idx_tmp2]
        idx_to += 1
        idx_tmp2 += 1
    return a


def array_left_rotation2(a, n, k):
    # 7, 9, 1 2 3 4 5 6 7
    # 9 % 7 = 2, 7-2=5
    idx_0_to = n - (k % n)
    tmp_arr = list()
    idx_to = idx_0_to
    idx_from = 0
    while n > idx_to and idx_from < idx_0_to:
        tmp_arr.append(a[idx_to])
        a[idx_to] = a[idx_from]
        idx_to += 1
        idx_from += 1
    if n > idx_to:
        while n > idx_to:
            tmp_arr.append(a[idx_to])
            a[idx_to] = tmp_arr.pop(0)
            idx_to += 1
    idx_to = 0
    while idx_0_to > idx_to and len(tmp_arr):
        a[idx_to] = tmp_arr.pop(0)
        idx_to += 1
    return a


def array_left_rotation(a, n, k):
    idx = 0
    pivot_idx = n - (k % n)  # 1
    pivot_cur_idx = 0
    na = list()
    while n > idx:
        idx_to = n - ((k - idx) % n)  # 1 2 3 4 0
        if idx_to is n:
            idx_to = 0
        tmp = a.pop(0)
        if idx_to < pivot_idx:
            na.insert(pivot_cur_idx, tmp)
            pivot_cur_idx += 1
        else:
            na.append(tmp)
        idx += 1
        # na == [1 2 3 4] 
        print(f'idx_to:{idx_to}')
    return na

    
def main():
    n, k = map(int, input().strip().split(' '))
    a = list(map(int, input().strip().split(' ')))
    answer = array_left_rotation3(a, n, k);
    print(*answer, sep=' ')


def main2():
    with open('arrays-left-rotation-input09.txt') as file:
        line_num = 0
        for line in file:
            if 0 == line_num:
                n, k = map(int, line.strip().split(' '))
            if 1 == line_num:
                a = list(map(int, line.strip().split(' ')))
            line_num += 1
    
    print(n, k)
    import time
    time.sleep(5)
    print(*a, sep=' ')
    time.sleep(5)

    answer = array_left_rotation(a, n, k);
    print(*answer, sep=' ')


if '__main__' == __name__:
    main()