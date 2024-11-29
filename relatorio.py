dados_alunos = []  # Array que vai armazenar os dados dos alunos
cont = 0  # Contador
cont_relatorio = 0

selecao = int(input("Digite 1 para cadastrar os alunos\nDigite 2 para para ver o relatório\nDigite 3 para cancelar\n")) #receber uma entrada do user e mostrar uma
alunos = int(input("Digite quantos alunos você quer cadastrar: "))
while selecao == 1: #Enquanto a entrada do user for igual a 1
    while cont < alunos:  # Enquanto o contador for menor que a quantidade de alunos, repita.
        nome_aluno = input(f"Digite o nome do aluno: ")  # Input para o nome do aluno
        faltas = int(input("Digite quantas faltas esse aluno tem: "))  # Input para as faltas do aluno
        soma_notas = 0  # Resetando a soma das notasdsa
        soma_notas_cont = 1  # Resetando o contador de bimestres
        while soma_notas_cont <= 4:  # Enquanto o contador for menor ou igual a 4, repita.
            nota = float(input(f"Digite a nota do aluno {nome_aluno} do {soma_notas_cont}º bimestre: "))  # Input para a nota
            soma_notas += nota  # Soma das variáveis
            soma_notas_cont += 1  # Incrementa o contador de bimestres
        media = soma_notas / 4  # Calcula a média do aluno.

        if faltas > 31:  # Se o aluno tiver mais de 31 faltas
            situacao = 'Reprovado'
        elif media >= 8:  # Se a média for maior ou igual a 8
            situacao = 'Aprovado'
        elif media >= 5:  # Se a média for maior ou igual a 5
            situacao = 'RECUPERAÇÃO'  # Aluno em recuperação
            rec = float(input(f"O aluno {nome_aluno} está de recuperação, digite a nota da sua prova: "))  # Input para a nota da recuperação
            if media + rec >= 8:  # Se a soma da média com a nota de recuperação for maior ou igual a 8
                media = media + rec  # Atualiza a média
                situacao = 'APROVADO'  # Aluno aprovado após a recuperação
            else:  # Se não, aluno reprovado
                situacao = 'REPROVADO'
        else:  # Se a média for menor que 5
            situacao = 'REPROVADO'  # Aluno reprovado

        aluno = {'nome': nome_aluno,'situacao': situacao,'media': media,'faltas': faltas} #Dicionario que vai acessar os dados de um array.
        dados_alunos.append(aluno)  # Adiciona o aluno na lista de dados
        
    if selecao == 2: #Se o usuario digitar o 2
        if len(dados_alunos) == 0:
            print("Nao a nada no banco de dados")
        else:
            print("\n--- Resultados Finais ---") #Mostrar uma mensagem na tela
            while cont_relatorio < len(dados_alunos): #Enquanto o contador do relatorio for menos que as posições do array, repita.
                aluno = dados_alunos[cont_relatorio] #Variavel que vai acessar uma posição do array
                print(f"Aluno: {aluno['nome']}, Situação: {aluno['situacao']}, Média: {aluno['media']:.2f}, Faltas: {aluno['faltas']}") #Vai mostrar na tela uma mensagem e os resultados do array no texto.
                cont_relatorio += 1 #Contador do relatório.
    else: #Senao
        print("Fim")