# Questão 1
n = int(input("digite um numero: "))
if n == 0:
    print("esse numero é zero")
elif n %2 == 0:
    print(f"{n} é par")
else:
    print(f"{n} é impar")
if n >= 1:
    print(f"{n} é positivo")
elif n < 0:
    print(f"{n} é negativo")
elif n == 0:
    print(f"{n} é nulo")