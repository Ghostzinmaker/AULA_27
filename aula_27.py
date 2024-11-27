cont = 0
qnt_alunos = int(input("Quantos alunos? "))

while cont < qnt_alunos:
    nome_aluno = input("Digite o nome do aluno: ")
    faltas = int(input("Digite quantas faltas esse aluno tem: "))
    soma_notas = 0
    soma_notas_cont = 1
    while soma_notas_cont <= 4:
        nota = float(input(f"Digite a nota do aluno {nome_aluno} do {soma_notas_cont}º bimestre: "))
        soma_notas += nota
        soma_notas_cont += 1
    media = soma_notas / 4 
    print(f"A média do aluno {nome_aluno} é: {media}")
    cont += 1