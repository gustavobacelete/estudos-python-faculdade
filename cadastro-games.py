#Programa que cadastra o nome do jogo e o video game utilizado em um bloco de notas.



def valida(pergunta, min, max):
    x = int(input(pergunta))
    while x < min or x > max:
        x = int(input(pergunta))
    return x


def criaArquivo(nomeArquivo):  # Cria o arquivo
    try:
        # W de escrita, e T de arquivo de texto e + para criar o arquivo se não existir
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print('Arquivo {} foi criado com sucesso!\n'.format(nomeArquivo))


def existeArquivo(nomeArquivo):  # Verifica se o arquivo existe
    try:
        # R = para abrir o arquivo para leitura, e o T verificar se o arquivo é txt
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:  # Se não abrir vai aparecer esse erro
        return False
    else:  # Se abrir retorna true
        return True


def listarArquivo(nomeArquivo):
    try:
        # Letra R somente para leitura, e T de arquivo text
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        # read função de ler o arquivo e mostrar na tela e vai mostrar todos os dados do arquivo
        print(a.read())
    finally:   # Independente se der erro ou não, vai fechar o arquivo
        a.close()


def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        # letra A para abrir o arquivo e manter oq estiver salvo, e T de arquivo text
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo')  # Se deu erro vai pra ca
    else:
        # Se deu certo vai pra ca
        a.write('{};{}\n'.format(nomeJogo, nomeVideogame))
    finally:  # Isso executa de qualquer maneira
        a.close()


# Programa Principal
arquivo = 'games.txt'  # Cria um arquivo txt com esse nome
if existeArquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo inexistente')
    criaArquivo(arquivo)  # Cria o arquivo se não existir


while True:  # Looping infinito porque não sei quantos cadastros irá ser feito
    print('MENU')
    print('1 - Cadastrar novo item')
    print('2 - Listar cadastros')
    print('3 - Sair')

    # Usar a função pra definir limite de numeros pro operador
    op = valida('Escolha a opção desejada:', 1, 3)
    if op == 1:
        print('Opção de cadastrar novo item selecionada...\n')
        nomeJogo = input('Nome do jogo:')
        nomeVideogame = input('Nome do videogame:')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)
    elif op == 2:
        print('Opção de listar selecionada...\n')
        listarArquivo(arquivo)
    elif op == 3:
        print('Encerrando programa...')
        break