dados_alunos = []                                                                                                                #Array.

def cadastrar_alunos():                                                                                                          #Declarando funcao para cadastrar os alunos.
    alunos = int(input("Digite quantos alunos voce quer cadastrar: "))                                                           #Variavel que vai receber uma entrada do user e mostrar uma mensagem na tela.
    cont = 0                                                                                                                     #Contador para o numero de alunos.
    while cont < alunos:                                                                                                         #Enquanto o contador for menor que a quantidade de alunos, repita.
        nome_aluno = input(f"Digite o nome do aluno: ")                                                                          #Input para o nome do aluno.
        faltas = int(input("Digite quantas faltas esse aluno tem: "))                                                            #Input para as faltas do aluno.
        soma_notas = 0                                                                                                           #Resetando a soma das notas.
        soma_notas_cont = 1                                                                                                      #Resetando o contador de bimestres.
        while soma_notas_cont <= 4:                                                                                              #Enquanto o contador for menor ou igual a 4, repita.
            nota = float(input(f"Digite a nota do aluno {nome_aluno} do {soma_notas_cont}º bimestre: "))                         #receber uma entrada do user, mostrar uma mensagem na tela e acessar valores de uma variavel.
            soma_notas += nota                                                                                                   #Soma dos valores.
            soma_notas_cont += 1                                                                                                 #variavel + 1.
        media = soma_notas / 4                                                                                                   #Calcula a media do aluno.

        if faltas > 31:                                                                                                          #Se o aluno tiver mais de 31 faltas
            situacao = 'Reprovado'                                                                                               #Variavel que vai receber uma palavra.
        elif media >= 8:                                                                                                         #Se a média for maior ou igual a 8
            situacao = 'Aprovado'                                                                                                #Variavel que vai receber uma palavra.
        elif media >= 5:                                                                                                         #Se a média for maior ou igual a 5
            situacao = 'RECUPERAÇÃO'                                                                                             #Variavel que vai receber uma palavra.
            rec = float(input(f"O aluno {nome_aluno} está de recuperação, digite a nota da sua prova: "))                        #Input para a nota da recuperação
            if media + rec >= 8:                                                                                                 #Se a soma da media com a nota de recuperaçao for maior ou igual a 8.
                media = media + rec                                                                                              #Atualiza a media.
                situacao = 'APROVADO'                                                                                            #Variavel que vai receber uma palavra.
            else:                                                                                                                #Senao.
                situacao = 'REPROVADO'                                                                                           #Variavel que vai receber uma palavra.
        else:                                                                                                                    #Senao.
            situacao = 'REPROVADO'                                                                                               #Variavel que vai receber uma palavra.

        aluno = {'nome': nome_aluno,'situacao': situacao,'media': media,'faltas': faltas}                                        #Dicionario com os dados do aluno
        dados_alunos.append(aluno)                                                                                               #Adiciona o aluno na lista de dados.
        cont += 1                                                                                                                #contador mais 1.

def relatorio():                                                                                                                 #Função que vai receber o relatorio.
    if len(dados_alunos) == 0:                                                                                                   #Se todas as posições do array for ugual a 0.
        print("Não há dados no banco de dados.")                                                                                 #Mostrar uma mensagem na tela.
    else:                                                                                                                        #Senao
        print("\n--- Resultados Finais ---")                                                                                     #Mostrar uma mensagem na tela.
        for aluno in dados_alunos:                                                                                               #Para cada aluno na lista.
            print(f"Aluno: {aluno['nome']}, Situação: {aluno['situacao']}, Média: {aluno['media']:.2f}, Faltas: {aluno['faltas']}")#Mostra os dados do aluno.

while True:                                                                                                                      #Enquanto for verdadeiro, repita.
    selecao = int(input("\n1 - cadastrar os alunos\n2 - Ver o relatório\n3 - Cancelar\n"))                                       #Receber entrada do user e mostrar uma mensagem na tela
    if selecao == 1:                                                                                                             #se o valor de uma variavel for igual a 1.
        cadastrar_alunos()                                                                                                       #Chamar funçao.
    elif selecao == 2:                                                                                                           #Senaose o valor de uma variavel for igual a 2.
        relatorio()                                                                                                              #Chama a funçao.
    elif selecao == 3:                                                                                                           #Senaose um valor de uma variavel for igual a 3.
        print("Fim")                                                                                                             #Mostrar uma mensagem na tela.
        break                                                                                                                    #Finalizar o loop.
    else:                                                                                                                        #Senao
        print("Opção inválida! Tente novamente.")                                                                                #Mostrar uma mensagem na tela.