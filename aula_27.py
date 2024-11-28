cont = 0 #Contador
soma_notas = 0 #Contador
soma_notas_cont = 1 #Contador
qnt_alunos = int(input("Quantos alunos? ")) #Input que vai receber uma ertrada do user e mostrar uma mensagem na tela

while cont < qnt_alunos: #Enquanto o contador for menor que a quantidades de alunos, repita.
    nome_aluno = input(f"Digite o nome do aluno: ") #Input que vai receber uma ertrada do user e mostrar uma mensagem na tela
    faltas = int(input("Digite quantas faltas esse aluno tem: ")) #Input que vai receber uma ertrada do user e mostrar uma mensagem na tela
    while soma_notas_cont <= 4: #Enquanto o contador for menor que ou igual a 4, repita.
        nota = float(input(f"Digite a nota do aluno {nome_aluno} do {soma_notas_cont}º bimestre: "))  #Input que vai receber uma ertrada do user e mostrar uma mensagem na tela
        soma_notas += nota #Soma das variaveis.
        soma_notas_cont += 1 #Soma das variaveis.
    media = soma_notas / 4 #Variavel que vai receber um calculo.

    if faltas > 31: #Se um valor de uma variavel for menor que 31.
        situacao = 'Reprovado' #Variavel que vai receber um texto.
    elif media >= 8: #Senaose o valor de uma variavel for maior ou igual a um valor.
        situacao = 'Aprovado' #Variavel que vai receber um texto.
    elif media >= 5: #Senaose o valor de uma variavel for maior ou igual a um valor.
        situacao = 'RECUPERAÇÃO' #Variavel que vai receber um texto.
        rec = float(input(f"O aluno {nome_aluno} está de recuperação, digite a nota da sua prova: ")) #Input que vai receber uma ertrada do user e mostrar uma mensagem na tela
        if media + rec >= 8: #Se o calculo de duas variaveis for maior ou igual a 8.
            media = media + rec #Media vai receber o calculo de duas variaveis.
            situacao = 'APROVADO' #Variavel que vai receber um texto.
        else: #Senao.
            situacao = 'REPROVADO' #Variavel que vai receber um texto.
    else: #Senao
        situacao = 'REPROVADO' #Variavel que vai receber um texto.

    print("O aluno:", nome_aluno, "foi", situacao, "com a média:", media, "e com", faltas, "faltas.") #vai mostrar uma mensagem na tela e os resultados de uma variavel

    cont += 1 #Variavel + ela mesmo mais 1