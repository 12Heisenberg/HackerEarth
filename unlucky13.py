def expo(n):

    if n == 0:
        return 1

    if n == 1:
        return 10

    if n % 2:
        return expo(n // 2) * expo(n // 2) * 10
    else:
        return expo(n // 2) * expo(n // 2)


def unlucky(n):

    if n == 0:
        return 1

    if n == 1:
        return 10

    return expo(n) - (n - 1) * expo(n - 2)


t = int(input())
for i in range(t):
    n = int(input())

    print(unlucky(n))