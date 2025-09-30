lc = []
for i in range(5):
    lc.append(input("nome do convidado:"))

nv = input("verificação de convidado:")
for i in lc:
    if i == nv:
        print("convidado confirmado!")
    else:
        print("convidado não encontrado!")