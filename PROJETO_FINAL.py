titulo = '\nPROJETO FINAL DO CURSO DE INTRODUÇÃO Á PROGRAMAÇÃO PYTHON\n'
print(titulo.rjust(20,"*"))

novo = input('Deseja iniciar o cadastro das notas do aluno (S/N)? ').upper()
while (novo != 'S' and novo != 'N'):
    print('Opção Invalida')
    novo = input('Informe "S" para Sim e "N" para Não: ').upper()

totalAlunos = 0
totalAprovados = 0
totalExame = 0
totalReprovados = 0
totalAlunos_Feminino = 0
totalAlunos_Masculino = 0


while (novo == 'S'):
    totalAlunos += 1
    nome_aluno = input('\nInforme o nome do aluno: ')

    sexo_aluno = input('Informe o sexo do aluno (F/M): ').upper()
    while (sexo_aluno != 'F' and sexo_aluno != 'M'):
        print('Opção Invalida')
        sexo_aluno = input('Informe "F" para o sexo Feminino e "M" para o sexo Masculino: ').upper()

    #alunos por sexo
    if (sexo_aluno == 'F'):
        totalAlunos_Feminino += 1
    else:
        totalAlunos_Masculino += 1

    nota1 = int(input('\nInforme a primeira nota: '))
    while (nota1 <0 or nota1 >10):
        print('Opção Invalida')
        nota1 = input('O valor da nota deve estar entre "0" e "10", digite novamente: ')

    nota2 = int(input('Informe a segunda nota: '))
    while (nota2 < 0 or nota2 > 10):
        print('Opção Invalida')
        nota2 = input('O valor da nota deve estar entre "0" e "10", digite novamente: ')

    nota3 = int(input('Informe a terceira nota: '))
        print('Opção Invalida')
        nota3 = input('O valor da nota deve estar entre "0" e "10", digite novamente: ')

    media = nota1 + nota2 + nota3 / 3

    #teste de notas

    if (media >= 7):
        totalAprovados +=1
    elif (media >= 4 and 7):
        totalExame +=1
    else: (media <4)
    totalReprovados +=1



    novo = input('\nDeseja continuar o cadastro das notas do aluno (S/N)? ').upper()
    while (novo != 'S' and novo != 'N'):
        print('Opção Invalida')
        novo = input('Informe "S" para Sim e "N" para Não: ').upper()
else:
    resultados = '\n\nApesentar os resultados finais\n\n'
    print(resultados.center(20,"*"))

print('Percentual de alunos Aprovados: ', (totalAprovados*100)/totalAlunos, '%')
print('Percentual de alunos de Exame: ', (totalExame*100)/totalAlunos, '%')
print('Percentual de alunos Reprovados: ', (totalReprovados*100)/totalAlunos, '%')

print('Total de alunos do sexo Feminino: ', totalAlunos_Feminino)
print('Total de alunos do sexo Masculino: ', totalAlunos_Masculino)
print('Total de alunos do sexo Feminino Aprovados: ' )
print('Total de alunos do sexo Masculino Aprovados: ')
print('Total de alunos do sexo Feminino de Exame: ')
print('Total de alunos do sexo Masculino de Exame: ')
print('Total de alunos do sexo Feminino Reprovados: ')
print('Total de alunos do sexo Masculino Reprovados: ')


