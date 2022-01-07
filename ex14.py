def primo(numero):
    for i in range(2,numero):
        if numero % i == 0:
            return False
    return True

if __name__ == '__main__':
    num1 = int(input('Entre com o primeiro numero: '))
    num2 =int(input('Entre com o segundo numero: '))
    for i in range(num1,num2):
        if primo(i):
            print(i)        
    
