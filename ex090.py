aluno = {}
n = str(input('Digite o nome: '))
aluno['nome'] = n
med = float(input('Digite sua média: '))
aluno['média'] = med
if med <= 4.9:
    aluno['situação'] = 'REPROVADO...'
elif 5 <= med <= 6.9:
    aluno['situação'] = 'RECUPERAÇÃO'
elif med <= 10:
    aluno['situação'] = 'APROVADO!'
for c, v in aluno.items():
    print(f'{c} corresponde a  {v}')

#consegui sozinha