test_case = int(input())
for i in range(test_case):
    N, M = list(map(int, input().split(' ')))
    lst = lst(map(int, input().split(' ')))
    idx = lst(range(len(lst)))
    importer = 0

    while True:
        if lst[0] == max(lst):
            importer += 1

            if idx[0] == M:
                print(importer)
                break
            else:
                lst.pop(0)
                idx.pop(0)

        else:
            lst.append(lst.pop(0))
            idx.append(idx.pop(0))
