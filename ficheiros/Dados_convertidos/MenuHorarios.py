def Msg(opcao):
    print(opcao)
    print('Em desenvolvimento por Carlos')
    input('Prima uma "Enter" para continuar ...')

def AlterarAlunos():
    Msg(__name__)

def InserirAlunos():
    Msg(__name__)

def Repararficheiro():
    f = open('Alunos.txt',"rt")
    linhas = f.readlines()
    f.close()
    for a in linhas:
        a = a.rstrip('\n')
        p = a.find(' ')
        a = a[:p] + ';'+ a[p+1:].replace(' ', '')
        colunas = a.split(';')
        colunas[3]= colunas[3][:10] + ' ' + colunas[3][11:]
        for c in colunas:
            print(c, sep=';', end='')
        print()
    return



    #print(linhas)   # todas as linhas
    #for i in range (0, len(linhas)):
    #    print(linhas[i])
    n = input('Numero aluno?')
    for a in linhas:
        a = a.rstrip('\n')
        p = a.find(' ')
        a = a[:p] +';' + a[p+1:].replace(' ', '')
        colunas = a.split(';')
        if (colunas[1].find(n) >= 0):
            print(a)

def MenuGerirAlunos():
    while True:
        print('1 - inserir')
        print('2 - alterar')
        print('3 - eliminar')
        print('4 - pesquisar por nome (lista todos)')
        print('5 - Reparar ficheiro')
        print('0 - voltar')
        op = input("?")
        if (op == '0'):
            break
        elif (op == '1'):
            InserirAlunos()
        elif (op == '2'):
            AlterarAlunos()
        elif (op == '5'):
            Repararficheiro()

def Menu():
    print(__name__)
    while True:
        print('1 - Gerir Alunos')
        print('2 - Gerir Disciplinas-Alunos')
        print('3 - Gerir Disciplinas-Horários')
        print('4 - Litar horário Formato Cartão  de crédito')
        print('5 - Litar horário A4')
        print('6 - Qualidade de um horário')
        print('0 - Terminar')
        op = input("?")

        if (op == '0'):
            break
        elif (op == '1'):
            MenuGerirAlunos()


Menu()




#(a) Pesquisar (nome) e listar docente
#(b) Listar horário de docente
#(c) Pesquisar (nome, curso) e listar disciplina
#(d) Listar horário disciplina

#necessários)
#(f) Gerir Disciplinas-Alunos (inserir, alterar, eliminar, pesquisar) (Devem ser denidos

#os dados necessários)
#(g) Gerir Disciplinas-Horários (inserir, alterar, eliminar, pesquisar) (Os dados já exitem)
#(h) Listar horário aluno (Texto, HTLM Markup Language (table, tr, th, td) 1)
#i. Formato Cartão de crédito
#ii. Formato A4