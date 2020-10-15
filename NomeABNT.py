#Luana Nogueira da Silva
#N1 Linguagem de Programação Parte 2

def reference(name):
    renamed = name[-1] + ', ' #pega o ultimo nome e concatena com ', '
    for i in range(len(name) - 1):
        name2 = name[i]
        if name2 not in ['DA', 'DE', 'DO', 'DAS', 'DOS']: #validação para remoção de conectivos
            renamed += name2[0] + ". " #concatena com as iniciais
        i += 1
    return renamed


name = input("Digite o nome a ser convertido:").upper().split()

referencia = reference(name)
print(referencia)
