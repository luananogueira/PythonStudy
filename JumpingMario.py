t = int(input())

for i in range(t): #quantidade de testes
    n = int(input())
    l = input().split() #cria lista por separaçao
    l = [int(elem) for elem in l] #transforma lista em inteiro

    lj = hj = 0
    p = 0

    for j in range(n): #quantidade de muros

        if p > l[j]:
            lj += 1
        elif 0 < p < l[j]:
            hj += 1

        p = l[j]  #muda a posição para o proximo muro

    print("Case {0}: {1} {2}".format(i + 1, hj, lj))
