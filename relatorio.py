dados_alunos = []                                                                                                                #Array.

def cadastrar_alunos():                                                                                                          #Declarando funcao para cadastrar os alunos.
    alunos = int(input("Digite quantos alunos voce quer cadastrar: "))                                                           #Variavel que vai receber uma entrada do user e mostrar uma mensagem na tela.
    cont = 0                                                                                                                     #Contador para o numero de alunos.
    while cont < alunos: 
        nome_aluno = input("Digite o nome do aluno: ")                                                                           #Input para o nome do aluno.
        faltas = int(input("Digite quantas faltas esse aluno tem: "))                                                            #Input para as faltas do aluno.
        soma_notas = 0                                                                                                           #Resetando a soma das notas.
        soma_notas_cont = 1                                                                                                      #Resetando o contador de bimestres.
        while soma_notas_cont <= 4:                                                                                              #Enquanto o contador for menor ou igual a 4, repita.
            nota = float(input(f"Digite a nota do aluno {nome_aluno} do {soma_notas_cont}º bimestre: "))                         #receber uma entrada do user, mostrar uma mensagem na tela e acessar valores de uma variavel.
            soma_notas += nota                                                                                                   #Soma dos valores.
            soma_notas_cont += 1                                                                                                 #variavel + 1.
        media = soma_notas / 4                                                                                                   #Calcula a media do aluno.
        situacao_aluno(faltas, nome_aluno, media)
        cont += 1

def situacao_aluno(faltas, nome_aluno, media):
    if faltas > 31:                                                                                                          #Se o aluno tiver mais de 31 faltas
        situacao = 'Reprovado por faltas'                                                                                               #Variavel que vai receber uma palavra.
    elif media >= 8:                                                                                                         #Se a média for maior ou igual a 8
        situacao = 'Aprovado acima da média'                                                                                                #Variavel que vai receber uma palavra.
    elif media >= 5:                                                                                                         #Se a média for maior ou igual a 5
        rec = float(input(f"O aluno {nome_aluno} está de recuperação, digite a nota da sua prova: "))                        #Input para a nota da recuperação
        media = 10 - media                                                                                                   #Atualiza a media.
        if media + rec >= 8:                                                                                                 #Se a soma da media com a nota de recuperaçao for maior ou igual a 8.
            situacao = 'Aprovado na recuperação'                                                                                            #Variavel que vai receber uma palavra.
        else:                                                                                                                #Senao.
            situacao = 'Reprovado na recuperação'                                                                                           #Variavel que vai receber uma palavra.
    else:                                                                                                                    #Senao.
        situacao = 'Reprovado abaixo da média'                                                                                               #Variavel que vai receber uma palavra.

    adicionar_aluno(nome_aluno, situacao, media, faltas)

def adicionar_aluno(nome_aluno, situacao, media, faltas):
    aluno = {'nome': nome_aluno, 'situacao': situacao, 'media': media, 'faltas': faltas}
    dados_alunos.append(aluno)

def relatorio():
    if len(dados_alunos) == 0:  
        print("Não há dados no banco de dados.")  
    else:
        print("\n--- Resultados Finais ---")
        for aluno in dados_alunos:
            print(f"Nome: {aluno['nome']}\nSituação: {aluno['situacao']}\nMédia: {aluno['media']}\nFaltas: {aluno['faltas']}")
            print("----------------------")

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