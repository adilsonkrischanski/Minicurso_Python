def primo(numero):
    for i in range(2,numero):
        if numero % i == 0:
            return False
    return True

if __name__ == '__main__':
    num = int(input())
    while num != 0:
        print(primo(num))
        num = int(input())
        
    
