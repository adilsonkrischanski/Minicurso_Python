n = int(input('entre com o numero a analizer: '))
verificacao = True
for i in range(2,n):
    if n % i == 0:
        print('N e primo')
        verificacao = False
        break
if verificacao:
    print('E primo')