cont = 0
soma_notas = 0
soma_notas_cont = 1
situacao = bool
qnt_alunos = int(input("Quantos alunos? "))

while cont < qnt_alunos:
    nome_aluno = input(f"Digite o nome do {qnt_alunos}º aluno: ")
    faltas = int(input("Digite quantas faltas esse aluno tem: "))
    while soma_notas_cont <= 4:
        nota = float(input(f"Digite a nota do aluno {nome_aluno} do {soma_notas_cont}º bimestre: "))
        soma_notas += nota
        soma_notas_cont += 1
    media = soma_notas / 4 

    if faltas > 31:
        situacao = 'Reprovado'
    elif media >= 8:
        situacao = 'Aprovado'
    elif media >= 5:
        situacao = 'RECUPERAÇÃO'
        rec = float(input(f"O aluno {nome_aluno} está de recuperação, digite a nota da sua prova: "))
        if media - rec == 8:
            situacao = 'APROVADO'
        else:
            situacao = 'REPROVADO'
    else:
        situacao = 'REPROVADP'
    
        
    print(f"A média do aluno {nome_aluno} é: {media}")



    cont += 1