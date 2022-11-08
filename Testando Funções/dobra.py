def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1

valores = [3, 6, 2, 5, 0, 7]
dobra(valores)
print(valores)