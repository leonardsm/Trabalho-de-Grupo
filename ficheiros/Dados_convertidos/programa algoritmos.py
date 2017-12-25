print("Em desenvolvimento por 2zucase1tuga")
print("Versão 1.0")
print("--------------------------------------------------------------------------------")


def inserir_alunos():
    f = open('Alunos.txt', 'a')
    name = input("Novo Aluno:")
    numero = input("Numero:")
    ano = input("Ano Escolar:")
    datadenascimento = input("Data de Nascimento:")
    email = input("email:")
    contacto = input("telemovel:")
    codigo_postal = input("codigo postal:")

    f.write(name)
    f.write(';')
    f.write(numero)
    f.write(';')
    f.write(ano)
    f.write(';')
    f.write(datadenascimento)
    f.write(';')
    f.write(email)
    f.write(';')
    f.write(contacto)
    f.write(';')
    f.write(codigo_postal)
    f.write('\n')

    f.close()
    print("%s ; %s; %s ; %s ; %s ; %s ; %s" % name % numero % ano % datadenascimento % email % contacto % codigo_postal)
    print("Inserção concluida")



def alterar_alunos():
    aluno_to_search = input("Nome? ")
    f = open("Alunos.txt", "a")
    found = False
    for line in f.readlines():
        line = line.rstrip('\n')
        vetor = line.split(';')
        name = vetor[0]
        naluno = vetor[1]
        short = vetor[2]
        d = vetor[3]
        e = vetor[4]
        t = vetor[5]
        c = vetor[6]
        if (name.find(aluno_to_search) >=0):
            print(naluno, name, short, d, e, t, c)
            r = input("É este? (s/n)")
            if (r=='s'):
                found = True
                break
    if found:
        alterar_aluno = input("O que deseja alterar? ")
        if(alterar_aluno=='nome'):
            novo_nome = input("Novo Aluno? ")
            f.write()
            
        elif(alterar_aluno=='numero'):
            novo_naluno = input("Numero? ")
        elif(alterar_aluno=='ano'):
            novo_short = input("Ano? ")
        elif(alterar_aluno=='data'):
            novo_d = input("Data de Nascimento? ")
        elif(alterar_aluno=='email'):
            novo_e = input("email? ")
        elif(alterar_aluno=='telemovel'):
            novo_t = input("telemovel? ")
        elif(alterar_aluno=='codigo postal'):
            novo_c = input("codigo postal? ")

    else:
        print("Aluno %s not found" % aluno_to_search)


def EliminarAlunos():
    aluno_to_search = input("Name? ")
    f = open("Alunos.txt", "a")
    found = False
    for line in f.readlines():
        line = line.rstrip('\n')
        vetor = line.split(';')
        name = vetor[0]
        naluno = vetor[1]
        short = vetor[2]
        d = vetor[3]
        e = vetor[4]
        t = vetor[5]
        c = vetor[6]
        if (name.find( aluno_to_search)>=0):
            print(name, naluno, short, d, e, t, c)
            r = input("É este? (s/n)")
            if (r=='s'):
                found = True
                break
    if found:
        alterar_aluno = input("O que deseja alterar? ")
        if(alterar_aluno=='nome'):
            novo_nome = input("Novo Nome? ")
            f.write(str)
            name.remove()
            name.insert(novo_nome)
        elif(alterar_aluno=='naluno'):
            novo_naluno = input("Novo Número de Aluno? ")
        elif(alterar_aluno=='ano'):
            novo_short = input("Novo Ano? ")
        elif(alterar_aluno=='data'):
            novo_d = input("Nova Data? ")
        elif(alterar_aluno=='email'):
            novo_e = input("Novo email? ")
        elif(alterar_aluno=='telemovel'):
            novo_t = input("Novo telemovel? ")
        elif(alterar_aluno=='cd'):
            novo_c = input("Novo cd? ")
        
    else:
        print("Aluno %s not found" % aluno_to_search)



def PesquisarAlunos():
    aluno_to_search = input("Nome? ")
    f = open('Alunos.txt', 'r')
    found = False
    for line in f.readlines():
        line = line.rstrip('\n')
        vetor = line.split(';')
        name = vetor[0]
        naluno = vetor[1]
        short = vetor[2]
        d = vetor[3]
        e = vetor[4]
        t = vetor[5]
        c = vetor[6]

        if (name.find(aluno_to_search) >= 0):
            print(name, naluno, short, d, e, t, c)
            r = input("É este? (s/n)")
            if (r == 's'):
                found = True
                break
    f.close()
    if found:
        print("Aluno %s encontrado" % aluno_to_search)
    else:
        print("Aluno %s nao encontrado" % aluno_to_search)


def Repararficheiro():
    f = open('Alunos.txt', "r")
    linhas = f.readlines()
    f.close()
    for a in linhas:
        a = a.rstrip('\n')
        p = a.find(' ')
        a = a[:p] + ';' + a[p + 1:].replace(' ', '')
        colunas = a.split(';')
        colunas[3] = colunas[3][:10] + ' ' + colunas[3][11:]
        for c in colunas:
            print(c, sep=';', end='')
        print()
    return


def ListaProfessores():
    f = open("teachers.txt", "r")
    linhas = f.readlines()
    f.close()
    for a in linhas:
        a = a.rstrip('\n')
        p = a.find(' ')
        a = a[:p] + ';' + a[p + 1:].replace(' ', '')
        colunas = a.split(';')
        colunas[3] = colunas[3][:10] + ' ' + colunas[3][11:]
        for c in colunas:
            print(c, sep=';', end='')
        print()
    return


def PesquisarProfessores():
    teacher_to_search = input("Nome?")
    f = open('teachers.txt', 'r')
    found = False
    for line in f.readlines():
        line = line.rstrip('\n')
        vetor = line.split(';')
        name = vetor[1]
        short = vetor[2]
        naluno = vetor[3]
        if (name.find(teacher_to_search) >= 0):
            print(naluno, name, short)
            r = input("É este? (s/n)")
            if (r == 's'):
                found = True
                break
    f.close()
    if found:
        print("Professor %s encontrado" % teacher_to_search)
    else:
        print("Professor %s nao encontrado" % teacher_to_search)

def MenuGerirProfessores():
    print('1 - Listar Professores')
    print('2 - Pesquisar Professores')
    print('3 - Listar Horario Formato Cartao')
    print('4 - Listar Horario Formato A4')
    print('5 - Qualidade de um Horario')
    print('0 - Voltar')
    op = input('Introduza um numero do Menu')
    if (op == '0'):
        Menu()
    elif (op == '1'):
        ListaProfessores()
    elif (op == '2'):
        PesquisarProfessores()
    elif (op == '3'):
        FicheiroHorarioProfCartao()
    elif (op == '4'):
        FicheiroHorarioProfA4()
    elif (op == '5'):
        QualidadedoHorario()
    else:
        print('Valor nao valido! a recomeçar...')
        Menu()

def MenuGerirAlunos():
    while True:
        print('1 - Inserir Aluno')
        print('2 - Alterar Aluno')
        print('3 - Eliminar Aluno')
        print('4 - Pesquisar Aluno')
        print('5 - Reparar ficheiro (lista todos)')
        print('6 - Listar Horario Formato Cartao')
        print('7 - Listar Horario Formato A4')
        print('0 - Voltar')
        op = input("Insira um Numero disponivel no menu: ")
        if (op == '0'):
            Menu()
        elif (op == '1'):
            InserirAlunos()
        elif (op == '2'):
            AlterarAlunos()
        elif (op == '3'):
            EliminarAlunos()
        elif (op == '4'):
            PesquisarAlunos()
        elif (op == '5'):
            Repararficheiro()
        elif (op == '6'):
            FicheiroHorarioAlunosCartao()
        elif op == '7':
            FicheiroHorarioAlunosA4()
        else:
            print('Numero Numero Nao Contido No Menu')
            Menu()

def Menu():
    while True:
        print('1 - Gerir Alunos')
        print('2 - Professores')

        op = input('Introduza um Numero Do Menu: ')

        if (op == '1'):
            MenuGerirAlunos()
        elif (op == '2'):
            MenuGerirProfessores()
        else:
            print('Numero Numero Nao Contido No Menu')
            Menu()
Menu()
