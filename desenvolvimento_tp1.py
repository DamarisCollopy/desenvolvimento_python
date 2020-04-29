import math
import os
import psutil
import errno
import time
import stat
import webbrowser
import subprocess

# fiz um switch para gerenciar melhor os pedidos
def meu_switch():
    validacao = True

    while validacao:
        z = int(input("Menu : "
                      "\n 1 : Nome do Usurio "
                      "\n 2 : Variaveis locais "
                      "\n 3 : PID"
                      "\n 4 : Diretorio Existentes"
                      "\n 5 : Imprime apenas arquivo relativo ou absoluto"
                      "\n 6 : Tamanho do Arquivo"
                      "\n 7 : Abrir Notepad"
                      "\n 8 : Processo Externo"
                      "\n 9 : PID"
                      "\n 10 : Nucleos CPU segundos" 
                      "\n 11 : CPUs segundos" 
                      "\n 12 : Memoria Paginada"
                      "\n 13 : Armazenamento Participação do Sistema"
                      "\n 14 : Informação Particão do Sistema"
                      "\n 15 : Sair \n"))
        if z == 1:
            nome_usuario()
        elif z == 2:
            variaveis_ambiente()
        elif z == 3:
            pid()
        elif z == 4:
            arquivo_vc_existe()
        elif z == 5:
            imprime_relativo_absoluto()
        elif z == 6:
            bytes_kb()
        elif z == 7:
            abrir_arquivo()
        elif z == 8:
            processo_externo()
        elif z == 9:
            processo_psutil()
        elif z == 10:
            uso_cpu_nucleo()
        elif z == 11:
            uso_cpu()
        elif z == 12:
            swap()
        elif z == 13:
            armazenamento_particao()
        elif z == 14:
            particao_sistema()
        elif z == 15:
            print("Programa encerrado")
            break
        else:
            print("opcao inválida")


def nome_usuario():
    print("Nome do Usuario :", os.getlogin())

def variaveis_ambiente():
    # Print todas as variaveis de ambiente
    print(os.environ)
    # Para imprimir variáveis específicas, basta acessá-la através da chave.
    # Por exemplo, para obter o drive e o caminho do diretório do usuário (home)
    print(os.environ['APPDATA'])
    print(os.environ['HOMEDRIVE'])
    print(os.environ['HOMEPATH'])
    # 4 Questao : Que função do módulo ‘os’ de Python é usada para obter o caminho absoluto de um diretório com caminho relativo? Dê um exemplo.
    # Para saber o caminho absoluto (completo) do diretório em que você se encontra, use ('.'):
    print("Caminho completo do diretorio absoluto usado pelo programa atual : ", os.listdir('.'))
    # Diretorio Relativo ('..').
    print("Diretorio Relativo :", os.listdir('..'))

# 3 Questao: Escreva um programa usando o módulo ‘os’ de Python que imprima o PID do próprio processo
def pid ():
    # Achar PID
    pid = os.getpid()
    print("Nome do processo ", psutil.Process(pid).name(), "PID", pid)

# 5 Questão : Escreva um programa que indique se um arquivo existe ou não. Caso exista, indique se é realmente um arquivo ou não.
def arquivo_vc_existe():
    # Verifica se o diretorio existe ou não.
    nome = input("Nome do diretorio")
    if os.path.exists(nome):
        print(nome, 'existe!')
        # 6 Questao Escreva um programa que indique a extensão de um arquivo usando função do módulo os.path.
        print("Tamanho em Bytes :", os.path.getsize(nome), "Bytes")
    else:
        print(nome, 'não existe!')

    # Identifica se ele é um arquivo ou txt.
    if os.path.isfile(nome):
        print(nome, 'é um arquivo!')
    else:
        print(nome, 'não é um arquivo!')

def crie_diretorio():
    # Cria um diretorio no qual você se encontra.

    nome = input("Nome do diretorio")
    try:
        os.mkdir(nome)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass
    print("Diretorio já existe, não é possivel criar um diretorio ja existente (%s)!" % (nome))

# 7 Questao :Escreva um programa que imprima apenas o caminho absoluto de um arquivo com nome relativo.
# A impressão não deve conter o nome do arquivo, apenas o caminho.
def imprime_relativo_absoluto():
    print("Arquivo Relativo : ", os.path.basename("C:\\Users\\Damaris-PC\\PycharmProjects\\desenvolvimento_python\\diretorio_exemplo"))

    print("Arquivo Absoluto", os.path.dirname("C:\\Users\\Damaris-PC\\PycharmProjects\\desenvolvimento_python\\diretorio_exemplo"))

# 8 Questao : Escreva um programa que mostre a quantidade de bytes (em KB) de cada arquivo em um diretório.
def bytes_kb():
    nome = "C:\\Users\\Damaris-PC\\PycharmProjects"
    n = os.path.getsize(nome)
    print("Tamanho em Bytes :", n, "Bytes")
    print(converte_tamanho(n))

    # 9 Questao Escreva um programa que mostre as datas de criação e modificação de cada arquivo em um diretório.
    caminho_path = r"C:\\Users\\Damaris-PC\\PycharmProjects"
    # esse r junto do caminho é uma formatacao para tornar visivel indeferente como o caminho esta inscrito para a bibloteca, pq na hora da leitura a biblioteca pode nao conseguir visualizar o nome
    nome_os = os.stat(caminho_path)
    formatar_hora = time.ctime(nome_os[stat.ST_MTIME])
    formatar_criacao = time.ctime(nome_os[stat.ST_CTIME])

    # O "ctime", conforme relatado pelo sistema operacional. Em alguns sistemas (como Unix), é a hora da última alteração de metadados e,
    # em outros (como Windows), é a hora de criação (consulte a documentação da plataforma para obter detalhes).
    print("Data da Criação:", formatar_criacao)
    # biblioteca os stat.St_MTIME funcao que mostra a ultima modificacao, usando a biblioteca time eu consigo formatar o numero apresentado em hora,dia,ano,dia da semana e mes por isso chamei de formatar a hora
    print("Data da modificação :", (formatar_hora))

# 10 Questao Escreva um programa que obtenha um nome de um arquivo texto do usuário e crie um processo, usando o módulo ‘os’, de bloco de notas (notepad) para abri-lo.
def abrir_arquivo():
    print(os.system("notepad arq_texto.txt"))

# 12 Questao Indique uma maneira de criar um processo externo ao seu programa usando o módulo ‘os’ e usando o módulo ‘subprocess’ de Python. Dê um exemplo de cada.
def processo_externo():
    # Chama a calculadora usando o pid
    # O exemplo, assim que o processo é criado, ele já retorna para o programa que o criou.
    # Logo, o programa criador pode manipular o processo criado ainda em execução!
    p = subprocess.Popen("calc")
    # 13 Questao Usando o módulo ‘subprocess’ de Python, crie um processo externo e imprima o PID dele.
    print("PID do processo criado:", p.pid)

# 14 Questao Explique a principal semelhança e a principal diferença entre os comandos psutil.pids e psutil.process_iter.
# A diferença está na forma como é implementada, de modo que seja mais eficiente quando executado repetidamente (em iterações).

# 15 Questao Escreva uma função em Python que, dado um número PID,
# imprima o nome do usuário proprietário, o tempo de criação e o uso de memória em KB.
def processo_psutil():
    # Achar PID
    pid = os.getpid()
    print("Nome do processo ", psutil.Process(pid).name(), "PID", pid)
    p = psutil.Process(pid)
    # Nome do executável
    print("Nome do Executavel: ", p.exe())
    # Usuario Proprietario
    print("Usuario Proprietario: ", p.username())
    # Data da Criacao
    print("Data da Criação: ", time.ctime(p.create_time()))
    # Informação de uso de memória do processo:
    processo = psutil.Process(os.getpid())
    memoria = processo.memory_info()[0]
    print("Informação de uso de memória do processo: ", memoria/1024, "KB")

# 16 Questao escreva um programa em Python, usando o módulo ‘psutil’, que imprima o tempo de CPU em segundos por núcleo.
def uso_cpu_nucleo():
    lista_cpu_times = []
    x = ['0','1','2','3','4','5','6','7','8','9']
    # Obter os tempos por núcleo do processador em porcentual
    for i in range(0, 10):
        cpu = psutil.cpu_times_percent()
        lista_cpu_times.append(cpu)
        time.sleep(1)

    text = ''
    for n, a in zip(x,lista_cpu_times):
        text += '\n Processador {} segundos  Numero de Nucleos {}'.format(n, a)
    print(text)

# 17 Questao Escreva um programa em Python, usando o módulo ‘psutil’, que imprima 20 vezes, de segundo a segundo, o percentual do uso de CPU do computador.
def uso_cpu():
    lista_cpu_percent = []
    x = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']
    # cpu_percent representa a utilização atual da CPU em todo o sistema como uma porcentagem.
    for i in range(0, 20):
        cpu = psutil.cpu_percent()
        lista_cpu_percent.append(cpu)
        time.sleep(1)

    text = ''
    for n, a in zip(x, lista_cpu_percent):
        text += '\n Processador {} segundos  Numero de Nucleos {} %'.format(n, a)
    print(text)

# 18 Questao Escreva um programa em Python, usando o módulo ‘psutil’, que imprima em GB, quanto de memória principal e
# quanto de memória de paginação (swap) existem no computador
def swap():
    # Memoria principal
    memoria_principal_total = psutil.virtual_memory().total
    memoria_principal_used = psutil.virtual_memory().used
    memoria_principal_free = psutil.virtual_memory().free
    # Memoria paginada
    memoria_used = psutil.swap_memory().used
    memoria_total = psutil.swap_memory().total
    memoria_free = psutil.swap_memory().free

    print("Memoria Principal Total :",converte_tamanho(memoria_principal_total)," ", "Memoria Principal em Uso: ",
          converte_tamanho(memoria_principal_used), " ", "Memoria Principal Livre:", converte_tamanho(memoria_principal_free))
    print("Memoria Paginada Total :",converte_tamanho(memoria_total), " ", "Memoria Paginada  em Uso: ",
          converte_tamanho(memoria_used), " ", "Memoria Paginada  Livre:", converte_tamanho(memoria_free))

# 19 Questao Escreva um programa em Python, usando o módulo ‘psutil’, que imprima em GB, quanto de armazenamento disponível há na partição do sistema (onde o sistema está instalado).
def armazenamento_particao():
    # Armazenamento disponível há na partição do sistema
    participacao_sistema = psutil.disk_usage('/').free

    print("Total de armazenamento disponivel há na partição do sistema : ", converte_tamanho(participacao_sistema))

# 20 Questao Escreva um programa em Python usando o módulo ‘psutil’, que imprima para a partição corrente:
def particao_sistema():
    particao = psutil.disk_partitions()
    lista = []
    for n in range(len(particao)):
        lista.append(particao[0][2])
        lista.extend(particao[0][0])

    # Nome do dispositivo
    nome_dispositivo = psutil.disk_partitions()
    # O tipo de sistema de arquivos que ela possui (FAT, NTFS, EXT, ...),
    tipo_arquivos = psutil.disk_partitions()
    # o total de armazenamento em GB
    total = psutil.disk_usage("C:\\Users\\Damaris-PC\\PycharmProjects").total
    # o armazenamento disponível em GB.
    livre = psutil.disk_usage("C:\\Users\\Damaris-PC\\PycharmProjects").free

    print("Nome do dispositivo :", lista[1], " ", " O tipo de sistema de arquivos que ela possui :", lista[0], " ", "Total de armazenamento em GB: ", converte_tamanho(total),
          " ", "Armazenamento Livre: ", converte_tamanho(livre))

def converte_tamanho(n):
   if n == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(n, 1024)))
   p = math.pow(1024, i)
   s = round(n / p, 2)
   return "%s %s" % (s, size_name[i])

if __name__ == "__main__":
    print(meu_switch())