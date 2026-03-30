from random import shuffle

nomes = []

while True:
    nome = input("Digite um nome (ou 'sair' para finalizar): ")
    
    if nome.lower() == 'sair':
        break
    
    if nome.strip() == "":
        print("Nome inválido!")
        continue
    
    nomes.append(nome)

if len(nomes) == 0:
    print("Nenhum nome foi adicionado.")
else:
    shuffle(nomes)
    print(f"\n🎉 Ordem sorteada: {nomes}")
