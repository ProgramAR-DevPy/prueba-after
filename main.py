numeros = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

pares = []
impares = []

for i in numeros:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print("Pares", pares)
print("Impares", impares)


print(pares + impares)

print("Aprendimos ahi astilla de github")
