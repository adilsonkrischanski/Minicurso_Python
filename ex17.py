
def fibo_recursiva(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibo_recursiva(n-1) + fibo_recursiva(n-2)

if __name__ == '__main__':
    n = int(input("Qual termo da sequencia deseja: "))
    print(fibo_recursiva(n))
