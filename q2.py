# Questão 2
p = int(input("digite a quantidade de produtos vendidos: "))
cp = p
vt = 0
ac50 = 0
ab50 = 0

while cp >= 1:
    pp = float(input("qual preço do produto: "))
    vt += pp
    if pp >= 50:
        ac50 += 1
    elif pp < 50:
        ab50 += 1
    cp -= 1

print(f"o valor total dos produtos vendidos foi de {vt}")
print(f"{ac50} produtos vendidos por um preço acima ou igual a 50 reais")
print(f"{ab50} produtos vendidos por um preço menor que 50 reais")
