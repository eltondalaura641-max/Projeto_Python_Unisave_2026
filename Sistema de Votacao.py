import json

candidatos = {}
votaram = []  # lista de quem já votou

while True:
    print("--- CHEFE DA TURMA ---")
    print("1. Adicionar candidato")
    print("2. Ver candidatos")
    print("3. Votar")
    print("4. Ver resultado")
    print("5. Eliminar candidato")
    print("0. Sair")
    op = input("Escolhe: ")

    if op == "1":
        nome = input("Nome: ")
        # Ver se o candidato já existe, sem repetir
        repetido = False
        for n in candidatos:
            if candidatos[n][0].lower() == nome.lower():
                repetido = True
        if repetido:
            print("Esse candidato ja existe!")
        else:
            num = str(len(candidatos) + 1)
            candidatos[num] = [nome, 0]
            print("Adicionado!")

    elif op == "2":
        if len(candidatos) == 0:
            print("Ainda nao ha candidatos.")
        else:
            for n in candidatos:
                print(n, "-", candidatos[n][0], "-", candidatos[n][1])

    elif op == "3":
        if len(candidatos) == 0:
            print("Ainda nao ha candidatos para votar.")
        else:
            eleitor = input("Teu nome (eleitor): ")
            # Se já votou, bloqueia
            if eleitor.lower() in votaram:
                print("Ja votaste! So podes votar uma vez.")
            else:
                for n in candidatos:
                    print(n, "-", candidatos[n][0])
                v = input("Vota em quem? ")
                if v in candidatos:
                    candidatos[v][1] += 1
                    votaram.append(eleitor.lower())
                    print("Voto registado!")
                else:
                    print("Numero invalido!")

    elif op == "4":
        if len(candidatos) == 0:
            print("Ainda nao ha candidatos.")
        else:
            total = 0
            maior = 0
            for n in candidatos:
                total += candidatos[n][1]
                if candidatos[n][1] > maior:
                    maior = candidatos[n][1]
            print("Total:", total)
            empatados = []
            for n in candidatos:
                print(candidatos[n][0], "-", candidatos[n][1])
                if candidatos[n][1] == maior:
                    empatados.append(candidatos[n][0])
            if len(empatados) > 1:
                print("EMPATE entre:", empatados)
            else:
                print("VENCEDOR:", empatados[0])

    elif op == "5":
        if len(candidatos) == 0:
            print("Ainda nao ha candidatos para eliminar.")
        else:
            for n in candidatos:
                print(n, "-", candidatos[n][0])
            v = input("Qual queres eliminar? ")
            if v in candidatos:
                print("Eliminado:", candidatos[v][0])
                del candidatos[v]
            else:
                print("Numero invalido!")

    elif op == "0":
        f = open("dados.json", "w")
        json.dump(candidatos, f)
        f.close()
        print("Fim!")
        break
    else:
        print("Opcao invalida!")