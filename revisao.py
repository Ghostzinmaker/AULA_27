aluno = []
cont = 0
escolha_user = int(input("Digite quantos alunos você quer cadastrar: "))
while cont < escolha_user:
    nome = input("Digite o nome do aluno: ")
    faltas = int(input(f"Digite quantas faltas o {nome} tem: "))
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    nota3 = float(input("Digite a terceira nota do aluno: "))
    nota4 = float(input("Digite a quarta nota do aluno: "))

    media = (nota1+nota2+nota3+nota4)/4

    if faltas > 30:
        situacao = 'Reprovado por faltas'
    elif media >= 8:
        situacao = 'Aprovado acima da média'
    elif media >= 5:
        rec = float(input(f"O aluno {nome} está de recuperação, digite a nota que o aluno tirou na recuperação: "))
        if rec >= (10 - media):
            situacao = 'Aprovado na recuperação'
        else:
            situacao = 'Reprovado na recuperação'
    else:
        situacao = 'Reprovado'

    aluno.append([nome, faltas, media, situacao])
    cont += 1

print(aluno)