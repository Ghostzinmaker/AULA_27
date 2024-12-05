dados_alunos = []                                                                                                                #Array.

def cadastrar_alunos():                                                                                                          #Declarando funcao para cadastrar os alunos.
    alunos = validar_int("\nDigite quantos alunos voce quer cadastrar: ")                                                        #Variavel que vai receber uma entrada do user e mostrar uma mensagem na tela.
    cont = 0                                                                                                                     #Contador para o numero de alunos.
    while cont < alunos:                                                                                                         #Enquanto contador for menor que alunos, repita
        nome_aluno = input("\nDigite o nome do aluno: ").strip()                                                                 #Input para o nome do aluno.
        faltas = validar_int(f"\nDigite quantas faltas o aluno(a) {nome_aluno} tem: ")                                           #Input para as faltas do aluno.
        n1 = validar_float(f"\nDigite a nota do {nome_aluno} no 1° bimestre: ")                                                  #Variavel que esta verificando se a entrada e float e mostrando uma mensagem na tela
        n2 = validar_float(f"Digite a nota do {nome_aluno} no 2° bimestre: ")                                                    #Variavel que esta verificando se a entrada e float e mostrando uma mensagem na tela
        n3 = validar_float(f"Digite a nota do {nome_aluno} no 3° bimestre: ")                                                    #Variavel que esta verificando se a entrada e float e mostrando uma mensagem na tela
        n4 = validar_float(f"Digite a nota do {nome_aluno} no 4° bimestre: ")                                                    #Variavel que esta verificando se a entrada e float e mostrando uma mensagem na tela   
        media = (n1 + n2 + n3 + n4) / 4                                                                                          #Calcula a media do aluno.
        situacao_aluno(faltas, nome_aluno, media, n1, n2, n3, n4)                                                                #Declarando variaveis para uma outra função.
        cont += 1                                                                                                                #Contador mais 1.

def situacao_aluno(faltas, nome_aluno, media, n1, n2, n3, n4):                                                                   #Funçãs que esta recebendo variaves dentro de outra função.
    if faltas > 31:                                                                                                              #Se o aluno tiver mais de 31 faltas
        situacao = 'Reprovado por faltas.'                                                                                       #Variavel que vai receber uma palavra.
    elif media >= 8:                                                                                                             #Se a média for maior ou igual a 8
        situacao = 'Aprovado acima da média.'                                                                                    #Variavel que vai receber uma palavra.
    elif media >= 5:                                                                                                             #Se a média for maior ou igual a 5
        rec = validar_float(f"\nO aluno {nome_aluno} está na recuperação, digite a nota da sua prova: ")                         #Input para a nota da recuperação
        media = 10 - media                                                                                                       #Atualiza a media.
        if rec >= media:                                                                                                         #Se a soma da media com a nota de recuperaçao for maior ou igual a 8.
            situacao = 'Aprovado na recuperação.'                                                                                #Variavel que vai receber uma palavra.
        else:                                                                                                                    #Senao.
            situacao = 'Reprovado na recuperação.'                                                                               #Variavel que vai receber uma palavra.
    else:                                                                                                                        #Senao.
        situacao = 'Reprovado abaixo da média.'                                                                                  #Variavel que vai receber uma palavra.
    adicionar_aluno(nome_aluno, situacao, media, faltas, n1, n2, n3, n4)                                                         #Declarando variaveis para uma outra função.

def adicionar_aluno(nome_aluno, situacao, media, faltas, n1, n2, n3, n4):                                                        #Funçãs que esta recebendo variaves dentro de outra função.
    aluno = {'nome': nome_aluno, 'situacao': situacao, 'media': media, 'notas': [n1, n2, n3, n4], 'faltas': faltas}              #Variavel que esta recebendo os valores da variavel.
    dados_alunos.append(aluno)                                                                                                   #Adicionando os valores da variavel acima no array.

def validar_int(texto):                                                                                                          #Funçãs que esta recebendo variaves dentro de outra função.
    while True:                                                                                                                  #Enquanto for verdadeiro.
        try:                                                                                                                     #Encolver o codigo e tratar para ver se há erros
            valor = int(input(texto))                                                                                            #Variavel que esta recebendo um valor inteiro e recebendo o texto de variaveis expecíficas.
            return valor                                                                                                         #Retorna valor
        except ValueError:                                                                                                       #se der tal erro
            print("\nOpa! Digite um numero inteiro válido.")                                                                     #Mostrar uma mensagem na tela

def validar_float(texto):                                                                                                        #Funçãs que esta recebendo variaves dentro de outra função.
    while True:                                                                                                                  #Enquanto for verdadeiro
        try:                                                                                                                     #Encolver o codigo e tratar para ver se há erros
            valor = float(input(texto))                                                                                          #Variavel que esta recebendo um valor quebrado e recebendo o texto de variaveis expecíficas.
            return valor                                                                                                         #Retorna valor
        except ValueError:                                                                                                       #se der tal erro
            print("\nOpa! Digite um numero decimal válido.")                                                                     #Mostrar uma mensagem na tela

def relatorio():                                                                                                                 #função.
    if len(dados_alunos) == 0:                                                                                                   #Se todas as posisões do array nao tiver nada.
        print("\nNão há dados no banco de dados.")                                                                               #Mostrar mensagem na tela.
    else:                                                                                                                        #Senao.
        print("\n--- Resultados Finais ---")                                                                                     #Mostrar mensagem na tela.
        for aluno in dados_alunos:                                                                                               #Acessando a variavel aluno e o array.
            print(f"\nAluno: {aluno['nome']}\nSituação: {aluno['situacao']}\nNotas: {", ".join(map(str, aluno['notas']))}\nMédia: {aluno['media']}\nFaltas: {aluno['faltas']}") #Mostrando na tela os valores da variavel e formatando o relatório.
            print("-"*15)                                                                                                        #Mostrar mensagem na tela.

while True:                                                                                                                      #Enquanto for verdadeiro, repita.
    try:                                                                                                                         #Encolver o codigo e tratar para ver se há erros
        selecao = int(input("\n1 - cadastrar os alunos\n2 - Ver o relatório\n3 - Cancelar\nSelecione: "))                        #Receber entrada do user e mostrar uma mensagem na tela
        if selecao == 1:                                                                                                         #se o valor de uma variavel for igual a 1.
            cadastrar_alunos()                                                                                                   #Chamar funçao.
        elif selecao == 2:                                                                                                       #Senaose o valor de uma variavel for igual a 2.
            relatorio()                                                                                                          #Chama a funçao.
        elif selecao == 3:                                                                                                       #Senaose um valor de uma variavel for igual a 3.
            print("\nFim")                                                                                                       #Mostrar uma mensagem na tela.
            break                                                                                                                #Finalizar o loop.
        else:                                                                                                                    #Senao
            print("\nOpção inválida! Tente novamente.")                                                                          #Mostrar uma mensagem na tela.
    except ValueError:                                                                                                           #se der tal erro
        print("\nOpção inválida! Tente novamente.")                                                                              #Mostrar uma mensagem na tela   