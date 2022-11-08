def soma(n1, n2):
    soma = n1 + n2
    print(soma)
    return(soma)

def contador(*num):
    print(num)
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')


contador(1, 9)
contador(1, 9, 2, 8)
contador(1, 9, 2)

numero1 = int(input('Digite o primeiro número. '))
numero2 = int(input('Digite o segundo número. '))
print(soma(numero1, numero2))