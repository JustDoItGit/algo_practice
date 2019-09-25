def bubble(ls):
    n = len(ls)
    if n <= 1:
        return ls
    flag = False
    for i in range(n):
        for j in range(n - i - 1):
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
                flag = True
        if flag is not True:
            return ls
    return ls


test_ls = [3, 5, 38, 2, 1]
print(bubble(test_ls))
test_ls = [3]
print(bubble(test_ls))
test_ls = [5, 2, 3, 1]
print(bubble(test_ls))
