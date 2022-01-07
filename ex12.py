def primo(numero):
    for i in range(2,numero):
        if numero % i == 0:
            return False
    return True

if __name__ == '__main__':
    num = int(input())
    print(primo(num))