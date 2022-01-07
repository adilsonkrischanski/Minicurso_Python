def conta_elementos(lista):
    if lista == []:
        return 0
    lista.pop(0)
    return 1 + conta_elementos(lista)


if __name__ == '__main__':
    a = [1,2,3,4,5]
    print(conta_elementos(a))