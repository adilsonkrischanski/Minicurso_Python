def fibo_interativa(n):
    t0 = 0
    t1 = 1

    if n == 1:
        return t0
    if n == 2:
        return t1
    if n == 3:
        return t0+t1
    t3 = t0+t1
    for i in range(2,n):
        t0 = t1
        t1 = t3
        t3 = t0+t1
    return t3

if __name__ == '__main__':
    n = int(input("Qual termo da sequencia deseja: "))
    print(fibo_interativa(n))