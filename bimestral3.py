def par(n):
    if n %2 == 0:
        return(f"{n} é par")
    else:
        return(f"{n} é impar")

n = int(input("digite um número:"))
print(par(n))