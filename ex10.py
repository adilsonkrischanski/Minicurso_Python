n = int(input())
soma= n
quant =1
maior = n
menor =n
while n != 0:
    n = int(input())
    soma +=n
    quant+=1
    if maior < n:
        maior = n
    if menor >n:
        menor = n
print(f'Maior = {maior} menor = {menor}\nsoma = {soma} media = {soma/quant} ')