def contador(*num):
    print(num)

    for valor in num:
        print(f'{valor} ', end = ' ')

    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} numeros')


contador(3, 2, 8)
contador(7, 9, 4)
contador(0, 7, 6, 5, 8)