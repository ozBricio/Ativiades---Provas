# Programa para operações matemáticas básicas em Python

# Entrada de dados: solicitamos ao usuário dois números e convertemos para tipo float
numero1 = float(input("Digite o primeiro número: "))  # input() sempre retorna uma string, então usamos float() para converter
numero2 = float(input("Digite o segundo número: "))

# Exibindo os resultados diretamente na função print()
print("Soma:", numero1 + numero2)  # Podemos realizar cálculos diretamente dentro do print()
print("Subtração:", numero1 - numero2)
print("Multiplicação:", numero1 * numero2)
print("Divisão:", numero1 / numero2)  # Atenção: divisão sempre retorna um número do tipo float

# Outra forma: armazenar os cálculos em variáveis antes de imprimir
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

# Exibindo os resultados usando variáveis
print("\nResultados armazenados em variáveis:")
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)

# ----------------------
# 🔍 Detalhes sobre a função print()
# ----------------------
# 1. Pode receber múltiplos argumentos separados por vírgula:
print("\nExemplo de múltiplos argumentos:", numero1, "+", numero2, "=", soma)
# Isso automaticamente adiciona espaços entre os valores, então a saída será algo como: 10 + 5 = 15

# 2. Pode formatar valores usando f-strings (Python 3.6+):
print(f"Usando f-strings: {numero1} + {numero2} = {soma}")
# O f antes da string permite incluir variáveis diretamente entre chaves {}

# 3. O separador padrão entre os argumentos é um espaço, mas podemos alterar:
print("Alterando o separador:", numero1, numero2, soma, sep=" | ")
# Aqui, os valores serão separados pelo caractere "|"

# 4. O print adiciona uma quebra de linha automática no final, mas podemos modificar isso:
print("Sem quebra de linha", end=" ")  # Define o final da linha como um espaço em branco
print("- Segunda parte na mesma linha")

# ----------------------
# 🔍 Limitações ao calcular diretamente no print()
# ----------------------
# Podemos calcular diretamente no print(), mas há casos onde armazenar o resultado antes é melhor:
# - Quando precisamos reutilizar o valor várias vezes no código.
# - Quando a operação envolve múltiplos passos, como raiz quadrada ou exponenciação complexa.
# - Para melhorar a legibilidade do código.

# Exemplo de cálculo que pode ser confuso se feito diretamente no print():
print("Exemplo mais complexo:", (numero1 + numero2) * (numero1 - numero2) / 2)

# Melhor alternativa: armazenar o valor antes
resultado = (numero1 + numero2) * (numero1 - numero2) / 2
print("Resultado armazenado:", resultado)

#  ⛔ =========  Próximo código:  =========  ⛔ 

'''num = int(input("Digite um número: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")'''

#VISAULG
#para i de 1 ate 5 faca
#   escreva(i)
#fimpara


for i in range(1, 6):  # range(1, 6) gera números de 1 a 5
    print(i)

# Desafio criar um programa que some os números de 1 a 100.







#Percorrendo uma Lista
#Podemos usar for para percorrer elementos de uma lista diretamente, sem precisar do range().
#Não precisamos usar índices, o próprio for percorre os elementos da lista.

frutas = ["Maçã", "Banana", "Laranja", "Uva"] #lista
for fruta in frutas:
    print(fruta)

#Percorrendo uma String
#Podemos usar for para percorrer cada letra de uma palavra.
palavra = "Python"

for letra in palavra:
    print(letra)

#Percorrendo um Dicionário
#Podemos usar for para percorrer chaves e valores de um dicionário.
notas = {"João": 8.5, "Maria": 9.0, "Carlos": 7.2}

for aluno, nota in notas.items():
    print(f"{aluno} tirou {nota}")




'''import os

print("Caminho do script:", os.getcwd())  # Mostra o diretório atual
print("Arquivos na pasta:", os.listdir())  # Lista os arquivos no diretório '
'''







#Percorrendo um Arquivo Texto
#Podemos usar for para ler um arquivo linha por linha.
with open("arquivo.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())  # Remove espaços extras



#Criar a Tabuada de um Número
#Peça ao aluno para digitar um número e exibir a tabuada desse número de 1 a 10.
numero = int(input("Digite um número para ver a tabuada: "))

print(f"Tabuada do {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")




#Jogo de Adivinhação
#O programa escolhe um número aleatório entre 1 e 100, e o usuário deve tentar adivinhar.

import random

numero_secreto = random.randint(1, 100)  # Gera um número entre 1 e 100
tentativas = 0

print("Tente adivinhar o número entre 1 e 100!")

for i in range(10):  # O usuário tem 10 tentativas
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
    elif palpite < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")

if palpite != numero_secreto:
    print(f"Fim de jogo! O número era {numero_secreto}.")


#  ⛔ =========  Próximo código:  =========  ⛔ 

produtos = {}

# Cadastro de produtos
while True:
    nome = input("Digite o nome do produto (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break
    preco = float(input(f"Digite o preço de {nome}: "))
    produtos[nome] = preco  # Inserção

# Consulta
consulta = input("Digite o nome do produto para consultar o preço: ")
if consulta in produtos:
    print(f"{consulta} custa R$ {produtos[consulta]:.2f}")
else:
    print("Produto não encontrado.")


#  ⛔ =========  Próximo código:  =========  ⛔ 

alunos = {
    "joao": {"idade": 15, "nota": 8.5},
    "maria": {"idade": 14, "nota": 9.0}
}

print(alunos["joao"]["nota"])     # 8.5
print(alunos["maria"]["idade"])   # 14

nome = input('Nome: ')
idade = int(input('Idade: '))
nota = float(input('Nota: '))
alunos[nome] = {'idade': idade, 'nota': nota}
print(alunos)

for nome, dados in alunos.items():
    print(f'Aluno: {nome}')
    for chave, valor in dados.items():
        print(f'{chave}: {valor}')


#  ⛔ =========  Próximo código:  =========  ⛔ 

alunos = {}

def cadastrar(nome, idade, nota):
    alunos[nome] = {"idade": idade, "nota": nota}
    print(f"Aluno {nome} cadastrado.")

def consultar(nome):
    if nome in alunos:
        return alunos[nome]
    else:
        return None

def listar():
    return alunos

if __name__ == "__main__":
    print("Executando módulo diretamente")
    cadastrar("Maria", 15, 8.5)
    print(listar())


#  ⛔ =========  Próximo código:  =========  ⛔ 

import json
import os
print("\nCaminho do script:", os.getcwd())  # Mostra o diretório atual
print("\nArquivos na pasta:", os.listdir())  # Lista os arquivos no diretório
# Tenta carregar o arquivo existente
if os.path.exists("alunos.json"):
    with open("alunos.json", "r") as arq:
        alunos = json.load(arq)
else:
    alunos = {}

def salvar_dados():
    with open("alunos.json", "w") as arq:
        json.dump(alunos, arq, indent=4)

def cadastrar_aluno():
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    nota = float(input("Nota: "))
    alunos[nome] = {"idade": idade, "nota": nota}
    salvar_dados()
    print("Aluno cadastrado.")

def consultar_aluno():
    nome = input("Nome: ")
    if nome in alunos:
        print(f"Idade: {alunos[nome]['idade']}, Nota: {alunos[nome]['nota']}")
    else:
        print("Aluno não encontrado.")

def listar_alunos():
    for nome, dados in alunos.items():
        print(f"{nome}: {dados}")

def menu():
    while True:
        print("\n1. Cadastrar\n2. Consultar\n3. Listar\n4. Sair")
        op = input("Escolha: ")
        if op == "1":
            cadastrar_aluno()
        elif op == "2":
            consultar_aluno()
        elif op == "3":
            listar_alunos()
        elif op == "4":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()


#  ⛔ =========  Próximo código:  =========  ⛔ 

import json

alunos = {}

def cadastrar_aluno():
    cpf = input("CPF do aluno: ")
    nome = input("Nome do aluno: ")
    idade = int(input("Idade: "))
    serie = input("Série: ")
    alunos[cpf] = {
        "nome": nome,
        "idade": idade,
        "serie": serie,
        "disciplinas": {}
    }

def adicionar_disciplina():
    cpf = input("CPF do aluno: ")
    if cpf in alunos:
        disciplina = input("Nome da disciplina: ")
        alunos[cpf]["disciplinas"][disciplina] = []
    else:
        print("CPF não encontrado.")

def adicionar_nota():
    cpf = input("CPF do aluno: ")
    if cpf in alunos:
        disciplina = input("Nome da disciplina: ")
        if disciplina in alunos[cpf]["disciplinas"]:
            nota = float(input("Nota: "))
            alunos[cpf]["disciplinas"][disciplina].append(nota)

def consultar_boletim():
    cpf = input("CPF do aluno: ")
    if cpf in alunos:
        aluno = alunos[cpf]
        print(f"Boletim de {aluno['nome']} - {aluno['serie']}:")
        for d, notas in aluno["disciplinas"].items():
            media = sum(notas) / len(notas) if notas else 0
            print(f"{d}: notas = {notas}, média = {media:.2f}")

def salvar_dados():
    with open("alunos.json", "w", encoding="utf-8") as arq:
        json.dump(alunos, arq, indent=4)

def carregar_dados():
    global alunos
    try:
        with open("alunos.json", "r", encoding="utf-8") as arq:
            alunos = json.load(arq)
    except FileNotFoundError:
        print("Arquivo não encontrado.")

def menu():
    carregar_dados()
    while True:
        print("1 - Cadastrar aluno")
        print("2 - Adicionar disciplina")
        print("3 - Adicionar nota")
        print("4 - Consultar boletim")
        print("5 - Salvar e sair")
        opcao = input("Escolha: ")
        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            adicionar_disciplina()
        elif opcao == "3":
            adicionar_nota()
        elif opcao == "4":
            consultar_boletim()
        elif opcao == "5":
            salvar_dados()
            break

if __name__ == "__main__":
    menu()

#  ⛔ =========  Próximo código:  =========  ⛔ 

import tkinter as tk
from tkinter import messagebox

# Função para calcular o coeficiente angular e a equação da reta
def calcular_coeficiente():
    try:
        # Obtém os valores digitados pelo usuário nas caixas de entrada
        y1 = float(entrada_y1.get())
        y2 = float(entrada_y2.get())
        x1 = float(entrada_x1.get())
        x2 = float(entrada_x2.get())
       

        # Verifica se a reta é vertical (x1 == x2), pois nesse caso o coeficiente angular é indefinido
        if x2 - x1 == 0:
            resultado.set("A reta é vertical, coeficiente indefinido.")
        else:
            # Calcula o coeficiente angular (m) usando a fórmula: m = (y2 - y1) / (x2 - x1)
            m = (y2 - y1) / (x2 - x1)
            
            # Calcula o coeficiente linear (b) usando a fórmula: b = y1 - m * x1
            b = y1 - (m * x1)
            
            # Formata a equação da reta no formato y = mx + b
            equacao = f"y = {m:.2f}x + {b:.2f}"
            
            # Exibe o resultado na interface gráfica
            resultado.set(f"Coeficiente angular: {m:.2f}\nIntercepto b: {b:.2f}\nEquação: {equacao}")
    
    except ValueError:
        # Se o usuário digitar algo inválido, exibe uma mensagem de erro
        messagebox.showerror("Erro", "Digite valores numéricos válidos!")

# Criando a janela principal da interface gráfica
janela = tk.Tk()
janela.title("Calculadora de Equação da Reta")  # Define o título da janela
janela.geometry("300x350")  # Define o tamanho da janela

# Labels e caixas de entrada para x1, y1, x2, y2
# Cada label exibe um texto e cada Entry permite a digitação de valores

tk.Label(janela, text="x1:").pack()
entrada_x1 = tk.Entry(janela)
entrada_x1.pack()

tk.Label(janela, text="x2:").pack()
entrada_x2 = tk.Entry(janela)
entrada_x2.pack()

tk.Label(janela, text="y1:").pack()
entrada_y1 = tk.Entry(janela)
entrada_y1.pack()

tk.Label(janela, text="y2:").pack()
entrada_y2 = tk.Entry(janela)
entrada_y2.pack()

# Botão que chama a função calcular_coeficiente ao ser pressionado
tk.Button(janela, text="Calcular", command=calcular_coeficiente).pack()

# Variável para armazenar e exibir o resultado na interface gráfica
resultado = tk.StringVar()
tk.Label(janela, textvariable=resultado, fg="blue").pack()

# Inicia o loop principal da interface gráfica
janela.mainloop()


#  ⛔ =========  Próximo código:  =========  ⛔ 

#  Regras para Nomes de Variáveis
#  Devem começar com uma letra ou um _ (underline).
#  Podem conter letras, números e _ mas não podem começar com números.
#  São case-sensitive (nome é diferente de Nome).
#  Não podem ser palavras reservadas do Python (ex.: if, for, while).
#  Em Python, declarar variáveis é simples e não requer especificação de tipo,
#  pois a linguagem é dinamicamente tipada.  Basta atribuir um valor a um nome de variável.
#  Aqui estão alguns exemplos:
'''
x = 10        # Inteiro
nome = "João" # String
preco = 99.99 # Float
ativo = True  # Booleano

# Declaração multipla
a, b, c = 1, 2, 3
nome, idade, cidade = "Maria", 25, "São Paulo"


print("A variável 'x' é do tipo:", type(x))
print("Seu valor é:", x)

print("A variável 'nome' é do tipo:",type(nome))
print("Seu valor é:",nome)

print("A variável 'preco' é do tipo:",type(preco))
print("Seu valor é:",preco)

print("A variável 'ativo' é do tipo:",type(ativo))
print("Seu valor é:",ativo)

#  Comentarios
"""
Este é um comentário de várias linhas.
Geralmente, é usado para documentação,
mas também pode servir como comentário.
"""

nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")
'''

# Solicita os dados do usuário
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura (em metros): "))

# Exibe os dados informados
print(f"\nOlá, {nome}! Você tem {idade} anos e {altura:.2f}m de altura.")

# Calcula a idade futura
idade_futura = idade + 10
print(f"Em 10 anos, você terá {idade_futura} anos.")



#  ⛔ =========  Próximo código:  =========  ⛔ 


# Sistema de Análise de Vendas com verificação de preços (Mini-BI)

frutas = ["banana", "maçã","abacaxi", "melancia"]
cereais = ["aveia", "granola", "milho", "trigo", "linhaça"]

precos = {
    "banana": 2.00, "maçã": 2.50, "melancia": 7.00, "abacaxi": 5.50,
    "aveia": 4.00, "granola": 5.50, "milho": 3.80, "trigo": 4.50, "linhaça": 6.00
}

vendas = [
    ["banana", 5, 2.00],      # R$ 10.00
    ["maçã", 8, 2.50],        # R$ 20.00
    ["melancia", 4, 7.00],    # R$ 28.00
    ["abacaxi", 4, 5.50],     # R$ 22.00
    ["aveia", 6, 4.00],       # R$ 24.00
    ["granola", 8, 5.50],     # R$ 44.00
    ["milho", 4, 3.80],       # R$ 15.20
    ["trigo", 7, 4.50],       # R$ 31.50
    ["linhaça", 5, 6.00],     # R$ 30.00
    ["maçã", 1, 2.00],        # ⚠️ abaixo do preço
    ["milho", 1, 4.50]        # ⚠️ acima do preço
]


resumo = {}

# Construção do relatório consolidado
for item, qtd, valor_vendido in vendas:
    total_item = qtd * valor_vendido

    if item not in resumo:
        resumo[item] = {
            "quantidade": 0,
            "total_vendido": 0,
            "valor_real": precos[item],
            "valor_vendido": valor_vendido
        }

    resumo[item]["quantidade"] += qtd
    resumo[item]["total_vendido"] += total_item

# Impressão do relatório
print("=== RELATÓRIO DE VENDAS ===")
total_geral = 0
for item, dados in resumo.items():
    print(f"\nItem: {item}")
    print(f"  Quantidade: {dados['quantidade']}")
    print(f"  Valor oficial: R$ {dados['valor_real']:.2f}")
    print(f"  Valor vendido: R$ {dados['valor_vendido']:.2f}")
    print(f"  Total vendido: R$ {dados['total_vendido']:.2f}")

    if dados["valor_vendido"] < dados["valor_real"]:
        print("  ⚠️ Vendido abaixo do preço!")
    elif dados["valor_vendido"] > dados["valor_real"]:
        print("  ⚠️ Vendido acima do preço!")

    total_geral += dados["total_vendido"]

print(f"\n💰 Total geral das vendas: R$ {total_geral:.2f}")

# Totais por categoria
total_frutas = sum(d["total_vendido"] for i, d in resumo.items() if i in frutas)
total_cereais = sum(d["total_vendido"] for i, d in resumo.items() if i in cereais)

print("\n=== TOTAL POR CATEGORIA ===")
print(f"🍎 Frutas: R$ {total_frutas:.2f}")
print(f"🌾 Cereais: R$ {total_cereais:.2f}")

# Análise de desempenho
mais_vendido = max(resumo.items(), key=lambda x: x[1]["quantidade"])
menos_vendido = min(resumo.items(), key=lambda x: x[1]["quantidade"])
mais_lucrativo = max(resumo.items(), key=lambda x: x[1]["total_vendido"])

print("\n=== DESEMPENHO ===")
print(f"📈 Mais vendido: {mais_vendido[0]} ({mais_vendido[1]['quantidade']} unidades)")
print(f"📉 Menos vendido: {menos_vendido[0]} ({menos_vendido[1]['quantidade']} unidades)")
print(f"💵 Mais lucrativo: {mais_lucrativo[0]} (R$ {mais_lucrativo[1]['total_vendido']:.2f})")


#  ⛔ =========  Próximo código:  =========  ⛔ 

import sqlite3

# Conecta (ou cria) o banco de dados
conn = sqlite3.connect("alunos.db")
cursor = conn.cursor()

# Cria a tabela se ainda não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    cpf TEXT PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    idade INTEGER NOT NULL,
    serie INTEGER NOT NULL
)
""")
conn.commit()

# Função para cadastrar aluno
def cadastrar_aluno():
    cpf = input("CPF (somente números): ").strip()
    cursor.execute("SELECT cpf FROM alunos WHERE cpf = ?", (cpf,))
    if cursor.fetchone():
        print(" CPF já cadastrado.")
        return

    nome = input("Nome: ").strip()
    email = input("Email: ").strip()
    idade = int(input("Idade: "))
    serie = int(input("Série: "))

    cursor.execute("INSERT INTO alunos VALUES (?, ?, ?, ?, ?)", (cpf, nome, email, idade, serie))
    conn.commit()
    print(" Aluno cadastrado com sucesso.")

# Função para listar todos os alunos
def listar_alunos():
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    print("\n Lista de alunos:")
    for a in alunos:
        print(f"CPF: {a[0]}, Nome: {a[1]}, Email: {a[2]}, Idade: {a[3]}, Série: {a[4]}")

# Menu simples para testar
if __name__ == "__main__":
    while True:
        print("\n1. Cadastrar aluno\n2. Listar alunos\n3. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            break
        else:
            print(" Opção inválida.")

# Fecha a conexão ao sair
conn.close()



#  ⛔ =========  Próximo código:  =========  ⛔ 



import json

alunos = {}

def cadastrar_aluno():
    cpf = input("CPF do aluno: ")
    nome = input("Nome do aluno: ")
    idade = int(input("Idade: "))
    serie = input("Série: ")
    alunos[cpf] = {
        "nome": nome,
        "idade": idade,
        "serie": serie,
        "disciplinas": {}
    }
    salvar_dados()
    
def adicionar_disciplina():
    cpf = input("CPF do aluno: ")
    if cpf in alunos:
        disciplina = input("Nome da disciplina: ")
        alunos[cpf]["disciplinas"][disciplina] = []
    else:
        print("CPF não encontrado.")

def adicionar_nota():
    cpf = input("CPF do aluno: ")
    if cpf in alunos:
        disciplina = input("Nome da disciplina: ")
        if disciplina in alunos[cpf]["disciplinas"]:
            nota = float(input("Nota: "))
            alunos[cpf]["disciplinas"][disciplina].append(nota)

def consultar_boletim():
    cpf = input("CPF do aluno: ")
    if cpf in alunos:
        aluno = alunos[cpf]
        print(f"Boletim de {aluno['nome']} - {aluno['serie']}:")
        for d, notas in aluno["disciplinas"].items():
            media = sum(notas) / len(notas) if notas else 0
            print(f"{d}: notas = {notas}, média = {media:.2f}")

def salvar_dados():
    with open("alunos.json", "w") as arq:
        json.dump(alunos, arq, indent=4)

def carregar_dados():
    global alunos
    try:
        with open("alunos.json", "r") as arq:
            alunos = json.load(arq)
    except FileNotFoundError:
        print("Arquivo não encontrado.")



#  ⛔ =========  Próximo código:  =========  ⛔ 


import json
from datetime import datetime

alunos = {}

# Função simples para validar CPF
def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

# Função para ler CPF válido
def ler_cpf():
    while True:
        cpf = input("Digite o CPF (somente números): ").strip()
        if validar_cpf(cpf):
            return cpf
        print(" CPF inválido. Digite exatamente 11 números.")

# Função para validar e-mail simples
def validar_email(email):
    if "@" in email and "." in email:
        if not email.startswith("@") and not email.endswith("@"):
            return True
    return False

# Função para ler e-mail válido
def ler_email():
    while True:
        email = input("Digite o e-mail do aluno: ").strip()
        if validar_email(email):
            return email
        print(" E-mail inválido. Digite novamente.")

# Função que calcula idade com base na data de nascimento
def calcular_idade(data_str):
    try:
        nascimento = datetime.strptime(data_str, "%d/%m/%Y")
        hoje = datetime.today()
        idade = hoje.year - nascimento.year
        if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
            idade -= 1
        return idade
    except:
        return None

# Função para ler data de nascimento e validar idade
def ler_idade():
    while True:
        data = input("Digite a data de nascimento (dd/mm/aaaa): ").strip()
        idade = calcular_idade(data)
        if idade and 6 <= idade <= 60:
            return idade
        print("Data inválida ou idade fora do intervalo (6 a 60 anos).")

# Função para ler a série do aluno (1 a 9, 10, 20, 30)
def ler_serie():
    while True:
        serie = input("Digite a série (1 a 9 para fundamental ou 10, 20, 30 para médio): ").strip()
        if serie.isdigit():
            s = int(serie)
            if 1 <= s <= 9 or s in (10, 20, 30):
                return s
        print("❌ Série inválida. Tente novamente.")

def cadastrar_aluno():
    cpf = ler_cpf()
    if cpf in alunos:
        print(" CPF já cadastrado. Não é possível duplicar.")
        return

    nome = input("Nome do aluno: ")
    email = ler_email()
    idade = ler_idade()
    serie = ler_serie()

    alunos[cpf] = {
        "nome": nome,
        "email": email,
        "idade": idade,
        "serie": serie,
        "disciplinas": {}
    }
    salvar_dados()
    print(" Aluno cadastrado com sucesso.")

def adicionar_disciplina():
    cpf = input("CPF do aluno: ")
    if cpf in alunos:
        disciplina = input("Nome da disciplina: ")
        alunos[cpf]["disciplinas"][disciplina] = []
        salvar_dados()
        print(" Disciplina adicionada.")
    else:
        print(" CPF não encontrado.")

def adicionar_nota():
    cpf = input("CPF do aluno: ")
    if cpf in alunos:
        disciplina = input("Nome da disciplina: ")
        if disciplina in alunos[cpf]["disciplinas"]:
            try:
                nota = float(input("Nota: "))
                if 0 <= nota <= 10:
                    alunos[cpf]["disciplinas"][disciplina].append(nota)
                    salvar_dados()
                    print(" Nota registrada.")
                else:
                    print(" Nota inválida. Digite entre 0 e 10.")
            except ValueError:
                print(" Entrada inválida. Digite um número.")
        else:
            print(" Disciplina não encontrada.")
    else:
        print(" CPF não encontrado.")

def consultar_boletim():
    cpf = input("CPF do aluno: ")
    if cpf in alunos:
        aluno = alunos[cpf]
        print(f"Boletim de {aluno['nome']} - Série: {aluno['serie']} - E-mail: {aluno['email']}")
        for d, notas in aluno["disciplinas"].items():
            media = sum(notas) / len(notas) if notas else 0
            print(f"{d}: notas = {notas}, média = {media:.2f}")
    else:
        print(" Aluno não encontrado.")

def salvar_dados():
    with open("alunos.json", "w", encoding="utf-8") as arq:
        json.dump(alunos, arq, indent=4)

def carregar_dados():
    global alunos
    try:
        with open("alunos.json", "r", encoding="utf-8") as arq:
            alunos = json.load(arq)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Arquivo de alunos não encontrado ou corrompido. Iniciando com base vazia.")

def excluir_aluno():
    cpf = input("Digite o CPF do aluno que deseja excluir: ").strip()
    if cpf in alunos:
        del alunos[cpf]
        salvar_dados()
        print(" Aluno excluído com sucesso.")
    else:
        print(" Aluno não encontrado.")

def excluir_disciplina():
    cpf = input("Digite o CPF do aluno: ")
    if cpf in alunos:
        disciplina = input("Digite o nome da disciplina a ser removida: ").strip()
        if disciplina in alunos[cpf]["disciplinas"]:
            del alunos[cpf]["disciplinas"][disciplina]
            salvar_dados()
            print(" Disciplina removida com sucesso.")
        else:
            print(" Disciplina não encontrada.")
    else:
        print(" Aluno não encontrado.")

def consultar_por_nome():
    nome = input("Digite o nome do aluno: ").strip().lower()
    encontrados = []

    for cpf, aluno in alunos.items():
        if nome in aluno["nome"].strip().lower():
            encontrados.append((cpf, aluno))

    if encontrados:
        print(f"\n🔎 {len(encontrados)} aluno(s) encontrado(s) com o nome '{nome}':\n")
        for cpf, aluno in encontrados:
            print(f"CPF: {cpf} | Nome: {aluno['nome']} | Série: {aluno['serie']} | Email: {aluno['email']}")
            for disciplina, notas in aluno["disciplinas"].items():
                media = sum(notas) / len(notas) if notas else 0
                print(f"  {disciplina}: notas = {notas}, média = {media:.2f}")
            print("-" * 40)
    else:
        print(" Nenhum aluno encontrado com esse nome.")

def editar_aluno():
    cpf = input("Digite o CPF do aluno que deseja editar: ").strip()
    if cpf in alunos:
        aluno = alunos[cpf]
        print(f"Editando aluno: {aluno['nome']}")
        novo_nome = input(f"Novo nome (ou ENTER para manter '{aluno['nome']}'): ").strip()
        novo_email = input(f"Novo e-mail (ou ENTER para manter '{aluno['email']}'): ").strip()
        nova_serie = input(f"Nova série (ou ENTER para manter '{aluno['serie']}'): ").strip()

        if novo_nome:
            aluno['nome'] = novo_nome
        if novo_email and validar_email(novo_email):
            aluno['email'] = novo_email
        if nova_serie.isdigit():
            s = int(nova_serie)
            if 1 <= s <= 9 or s in (10, 20, 30):
                aluno['serie'] = s

        salvar_dados()
        print(" Dados do aluno atualizados com sucesso.")
    else:
        print(" Aluno não encontrado.")


#  ⛔ =========  Próximo código:  =========  ⛔ 


import tkinter as tk

# Função para atualizar o conteúdo do visor
def digitar(valor):
    atual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, atual + valor)

# Função para calcular o resultado
def calcular():
    try:
        resultado = eval(entrada.get())  # CUIDADO: eval() executa código!
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")

# Função para limpar o visor
def limpar():
    entrada.delete(0, tk.END)

# Criar janela
janela = tk.Tk()
janela.title("Calculadora Simples")
janela.geometry("300x350")

# Campo de entrada
entrada = tk.Entry(janela, width=20, font=("Arial", 18), bd=5, relief=tk.GROOVE, justify="right")
entrada.pack(pady=10)

# Botões
botoes = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "=", "+")
]

for linha in botoes:
    frame = tk.Frame(janela)
    frame.pack()
    for texto in linha:
        if texto == "=":
            botao = tk.Button(frame, text=texto, width=5, height=2, font=("Arial", 14), command=calcular)
        else:
            botao = tk.Button(frame, text=texto, width=5, height=2, font=("Arial", 14), command=lambda t=texto: digitar(t))
        botao.pack(side=tk.LEFT, padx=5, pady=5)

# Botão de limpar
tk.Button(janela, text="Limpar", width=22, height=2, font=("Arial", 12), command=limpar).pack(pady=10)

# Iniciar janela
janela.mainloop()


#  ⛔ =========  Próximo código:  =========  ⛔ 


# Função simples para validar CPF
def validar_cpf_basico(cpf):
    return cpf.isdigit() and len(cpf) == 11

#Função para ler CPF válido e já retornar armazenado
def ler_cpf_valido():
    while True:
        cpf = input("Digite o CPF (somente números): ").strip()
        if validar_cpf_basico(cpf):
            return cpf
        print(" CPF inválido. Digite novamente (11 dígitos numéricos).")

# Função de cadastro com validação de CPF
def cadastrar_aluno():
    cpf = ler_cpf_valido()  # valida CPF antes de cadastrar
    nome = input("Nome do aluno: ")
    idade = int(input("Idade: "))
    serie = input("Série: ")
    
    alunos[cpf] = {
        "nome": nome,
        "idade": idade,
        "serie": serie,
        "disciplinas": {}
    }
    salvar_dados()
    print(" Aluno cadastrado com sucesso.")



#  ⛔ =========  Próximo código:  =========  ⛔ 


# Aula prática com dicionários e dicionários aninhados em Python
#\\srvaua07\publico\lg > endereço rede
# Criamos um dicionário vazio que vai armazenar os dados dos alunos
alunos = {}

print("=== Cadastro de Alunos ===")
quantidade = int(input("Quantos alunos deseja cadastrar? "))

# Parte 1: Cadastrando alunos
for i in range(quantidade):
    print(f"\nCadastro do aluno {i + 1}")

    cpf = input("Digite o CPF do aluno (somente números): ").strip()
    nome = input("Nome do aluno: ").strip()
    idade = int(input("Idade: "))

    # Verifica se o aluno é maior de idade
    maioridade = "Sim" if idade >= 18 else "Não"

    # Coleta 4 notas com validação simples
    notas = []
    for j in range(1, 5):
        nota = float(input(f"Digite a nota {j}: "))
        while nota < 0 or nota > 10:
            print("Nota inválida. Digite uma nota entre 0 e 10.")
            nota = float(input(f"Digite a nota {j}: "))
        notas.append(nota)

    # Calcula a média
    media = sum(notas) / len(notas)

    # Verifica se está aprovado
    status = "Aprovado" if media >= 7 else "Reprovado"

    # Armazena tudo no dicionário
    alunos[cpf] = {
        "nome": nome,
        "idade": idade,
        "maioridade": maioridade,
        "notas": notas,
        "media": media,
        "status": status
    }

# Parte 2: Exibindo todos os alunos
print("\n=== Lista de Alunos Cadastrados ===")

# Aqui usamos o comando "for" para percorrer o dicionário de alunos
# Um dicionário possui pares chave:valor, por isso usamos duas variáveis após o 'for'
# - cpf será a chave (o número do CPF)
# - dados será o valor (um dicionário com as informações do aluno)
# O método .items() retorna uma lista com tuplas (chave, valor), permitindo essa separação
for cpf, dados in alunos.items():
    print(f"\nCPF: {cpf}")
    print(f"  Nome: {dados['nome']}")
    print(f"  Idade: {dados['idade']} - Maior de idade? {dados['maioridade']}")
    print(f"  Notas: {dados['notas']} - Média: {dados['media']:.2f}")
    print(f"  Situação: {dados['status']}")

# Parte 3: Atualizando ou excluindo dados
print("\n=== Edição de Dados ===")
acao = input("Deseja atualizar (A), excluir (E) ou sair (S)? ").upper()

while acao != "S":
    cpf = input("Digite o CPF do aluno: ")
    if cpf in alunos:
        if acao == "A":
            print(f"Atualizando dados do aluno: {alunos[cpf]['nome']}")
            nova_idade = int(input("Nova idade: "))
            alunos[cpf]['idade'] = nova_idade
            alunos[cpf]['maioridade'] = "Sim" if nova_idade >= 18 else "Não"

            nova_nota1 = float(input("Nova nota 1: "))
            nova_nota2 = float(input("Nova nota 2: "))
            alunos[cpf]['notas'] = [nova_nota1, nova_nota2]
            nova_media = sum(alunos[cpf]['notas']) / 2
            alunos[cpf]['media'] = nova_media
            alunos[cpf]['status'] = "Aprovado" if nova_media >= 7 else "Reprovado"
            print("Dados atualizados com sucesso!")

        elif acao == "E":
            confirmar = input("Tem certeza que deseja excluir este aluno? (S/N) ").upper()
            if confirmar == "S":
                del alunos[cpf]
                print("Aluno removido com sucesso!")
        else:
            print("Opção inválida.")
    else:
        print("CPF não encontrado.")

    print("\n--- Alunos Atualizados ---")

    # Mesmo conceito de iteração explicado acima, aplicado aqui novamente
    for cpf, dados in alunos.items():
        print(f"CPF: {cpf} | Nome: {dados['nome']} | Média: {dados['media']} | Status: {dados['status']}")

    print()
    acao = input("Deseja atualizar (A), excluir (E) ou sair (S)? ").upper()

print("\nPrograma encerrado.")


#  ⛔ =========  Próximo código:  =========  ⛔ 


# Dicionário principal para armazenar os alunos
alunos = {}

while True:
    print("\n--- MENU ---")
    print("1. Cadastrar novo aluno")
    print("2. Consultar aluno")
    print("3. Mostrar todos os alunos")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do aluno: ")
        idade = int(input("Idade: "))
        nota = float(input("Nota final: "))

        # Adiciona ao dicionário principal
        alunos[nome] = {
            "idade": idade,
            "nota": nota
        }
        print(f"Aluno {nome} cadastrado com sucesso!")

    elif opcao == "2":
        busca = input("Digite o nome do aluno para consulta: ")
        if busca in alunos:
            print(f"\nNome: {busca}")
            print(f"Idade: {alunos[busca]['idade']}")
            print(f"Nota: {alunos[busca]['nota']}")
        else:
            print("Aluno não encontrado.")

    elif opcao == "3":
        print("\n--- TODOS OS ALUNOS ---")
        for nome, dados in alunos.items():
            print(f"\nAluno: {nome}")
            for chave, valor in dados.items():
                print(f"{chave}: {valor}")

    elif opcao == "4":
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")


#  ⛔ =========  Próximo código:  =========  ⛔ 

alunos = {}

def cadastrar(nome, idade, nota):
    alunos[nome] = {"idade": idade, "nota": nota}
    print(f"Aluno {nome} cadastrado.")

def consultar(nome):
    if nome in alunos:
        return alunos[nome]
    else:
        return None

def listar():
    return alunos

if __name__ == "__main__":
    while True:
        print("\n--- MENU ---")
        print("1. Cadastrar novo aluno")
        print("2. Consultar aluno")
        print("3. Listar todos os alunos")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do aluno: ")
            idade = int(input("Idade: "))
            nota = float(input("Nota: "))
            cadastrar(nome, idade, nota)

        elif opcao == "2":
            nome = input("Nome para consulta: ")
            dados = consultar(nome)
            if dados:
                print(f"Idade: {dados['idade']}, Nota: {dados['nota']}")
            else:
                print("Aluno não encontrado.")

        elif opcao == "3":
            print("\n--- LISTA DE ALUNOS ---")
            for nome, dados in listar().items():
                print(f"{nome} - Idade: {dados['idade']}, Nota: {dados['nota']}")

        elif opcao == "4":
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")



#  ⛔ =========  Próximo código:  =========  ⛔ 


import sqlite3
import re

# Criação da tabela
def criar_tabela():
    con = sqlite3.connect("alunos.db")
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            cpf TEXT PRIMARY KEY,
            nome TEXT NOT NULL,
            data_nasc TEXT NOT NULL,
            serie INTEGER NOT NULL,
            email TEXT
        )
    """)
    con.commit()
    con.close()

# Validação simples de CPF (somente numérico e 11 dígitos)
def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

# Validação simples de e-mail
def validar_email(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao, email)

# Inserção de aluno
def inserir_aluno(cpf, nome, data_nasc, serie, email):
    try:
        con = sqlite3.connect("alunos.db")
        cur = con.cursor()
        cur.execute("INSERT INTO alunos (cpf, nome, data_nasc, serie, email) VALUES (?, ?, ?, ?, ?)",
                    (cpf, nome, data_nasc, serie, email))
        con.commit()
        con.close()
        return True
    except sqlite3.IntegrityError:
        return False

# Consulta aluno por CPF
def consultar_aluno(cpf):
    con = sqlite3.connect("alunos.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM alunos WHERE cpf = ?", (cpf,))
    aluno = cur.fetchone()
    con.close()
    return aluno

# Listar todos os alunos
def listar_todos():
    con = sqlite3.connect("alunos.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM alunos")
    lista = cur.fetchall()
    con.close()
    return lista


#  ⛔ =========  Próximo código:  =========  ⛔ 


import sqlite3

# Cria a tabela no banco de dados se ainda não existir
def criar_tabela():
    con = sqlite3.connect("alunos.db")
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            cpf TEXT PRIMARY KEY,
            nome TEXT NOT NULL,
            data_nasc TEXT NOT NULL,
            serie INTEGER NOT NULL,
            email TEXT
        )
    """)
    con.commit()
    con.close()

# Insere um novo aluno no banco
def inserir_aluno(cpf, nome, data_nasc, serie, email):
    try:
        con = sqlite3.connect("alunos.db")
        cur = con.cursor()
        cur.execute("INSERT INTO alunos (cpf, nome, data_nasc, serie, email) VALUES (?, ?, ?, ?, ?)",
                    (cpf, nome, data_nasc, serie, email))
        con.commit()
        con.close()
        return True
    except sqlite3.IntegrityError:
        return False



#  ⛔ =========  Próximo código:  =========  ⛔ 

import sqlite3
from datetime import datetime, date

# ==============================
# Conexão com o Banco
# ==============================

def conectar_banco():
    con = sqlite3.connect("escola.db")
    return con, con.cursor()

# ==============================
# Funções de Validação
# ==============================

def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

def validar_email(email):
    return "@" in email and "." in email

def validar_data_nascimento(data_nasc):
    try:
        datetime.strptime(data_nasc, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def calcular_idade(data_nasc):
    nascimento = datetime.strptime(data_nasc, "%d/%m/%Y")
    hoje = date.today()
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
    return idade

def validar_serie(serie):
    return serie in list(range(1, 10)) + [10, 20, 30]

def validar_bimestre(bimestre):
    return bimestre in [1, 2, 3, 4]

# ==============================
# Inicialização do Banco
# ==============================

def inicializar_banco():
    con, cur = conectar_banco()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        cpf TEXT PRIMARY KEY,
        nome TEXT NOT NULL,
        email TEXT,
        data_nascimento TEXT,
        serie INTEGER
    )""")
    cur.execute("""
    CREATE TABLE IF NOT EXISTS disciplinas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cpf_aluno TEXT,
        nome_disciplina TEXT,
        FOREIGN KEY (cpf_aluno) REFERENCES alunos(cpf)
    )""")
    cur.execute("""
    CREATE TABLE IF NOT EXISTS notas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        disciplina_id INTEGER,
        bimestre INTEGER,
        nota REAL,
        FOREIGN KEY (disciplina_id) REFERENCES disciplinas(id)
    )""")
    con.commit()
    con.close()

# ==============================
# Cadastro de Aluno
# ==============================

def cadastrar_aluno():
    cpf = input("CPF do aluno (somente números): ").strip()
    if not validar_cpf(cpf):
        print("CPF inválido. Deve conter 11 dígitos numéricos.")
        return

    nome = input("Nome do aluno: ").strip()
    email = input("Email: ").strip()
    if not validar_email(email):
        print("Email inválido.")
        return

    data_nasc = input("Data de nascimento (dd/mm/aaaa): ").strip()
    if not validar_data_nascimento(data_nasc):
        print("Data inválida. Use o formato dd/mm/aaaa.")
        return

    idade = calcular_idade(data_nasc)
    if idade < 6 or idade > 60:
        print("Idade fora da faixa permitida (6 a 60 anos).")
        return

    serie = int(input("Série (1 a 9 ou 10, 20, 30): "))
    if not validar_serie(serie):
        print("Série inválida.")
        return

    con, cur = conectar_banco()
    cur.execute("INSERT OR REPLACE INTO alunos (cpf, nome, email, data_nascimento, serie) VALUES (?, ?, ?, ?, ?)",
                (cpf, nome, email, data_nasc, serie))
    con.commit()
    con.close()
    print("Aluno cadastrado com sucesso.")

# ==============================
# Cadastro de Disciplina
# ==============================

def adicionar_disciplina():
    cpf = input("CPF do aluno: ").strip()
    disciplina = input("Nome da disciplina: ").strip()

    con, cur = conectar_banco()
    cur.execute("INSERT INTO disciplinas (cpf_aluno, nome_disciplina) VALUES (?, ?)", (cpf, disciplina))
    con.commit()
    con.close()
    print("Disciplina adicionada com sucesso.")

# ==============================
# Lançamento de Nota
# ==============================

def adicionar_nota():
    cpf = input("CPF do aluno: ").strip()
    disciplina = input("Nome da disciplina: ").strip()
    bimestre = int(input("Número do bimestre (1 a 4): "))
    if not validar_bimestre(bimestre):
        print("Bimestre inválido. Deve ser 1, 2, 3 ou 4.")
        return

    nota = float(input("Nota: "))

    con, cur = conectar_banco()
    cur.execute("SELECT id FROM disciplinas WHERE cpf_aluno = ? AND nome_disciplina = ?", (cpf, disciplina))
    resultado = cur.fetchone()
    if resultado:
        disciplina_id = resultado[0]
        cur.execute("INSERT INTO notas (disciplina_id, bimestre, nota) VALUES (?, ?, ?)",
                    (disciplina_id, bimestre, nota))
        con.commit()
        print("Nota registrada com sucesso.")
    else:
        print("Disciplina não encontrada.")
    con.close()

# ==============================
# Consultar Boletim
# ==============================

def consultar_boletim():
    cpf = input("CPF do aluno: ").strip()

    con, cur = conectar_banco()
    cur.execute("SELECT nome, email, data_nascimento, serie FROM alunos WHERE cpf = ?", (cpf,))
    aluno = cur.fetchone()

    if aluno:
        nome, email, data_nasc, serie = aluno
        idade = calcular_idade(data_nasc)

        print(f"\nBoletim de {nome} - Série: {serie}º ano")
        print(f"Email: {email}")
        print(f"Data de nascimento: {data_nasc} - Idade: {idade} anos")

        cur.execute("SELECT id, nome_disciplina FROM disciplinas WHERE cpf_aluno = ?", (cpf,))
        disciplinas = cur.fetchall()
        for disciplina_id, nome_disciplina in disciplinas:
            print(f"\nDisciplina: {nome_disciplina}")
            cur.execute("SELECT bimestre, nota FROM notas WHERE disciplina_id = ? ORDER BY bimestre", (disciplina_id,))
            notas = cur.fetchall()
            total = 0
            for bimestre, nota in notas:
                print(f"  {bimestre}º Bimestre: {nota}")
                total += nota
            if notas:
                media = total / len(notas)
                print(f"  Média: {media:.2f}")
            else:
                print("  Nenhuma nota registrada.")
    else:
        print("Aluno não encontrado.")
    con.close()



#  ⛔ =========  Próximo código:  =========  ⛔ 

import sqlite3
from datetime import datetime, date

# ==============================
# Funções de Validação
# ==============================

def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

def validar_email(email):
    return "@" in email and "." in email

def validar_data_nascimento(data_nasc):
    try:
        datetime.strptime(data_nasc, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def calcular_idade(data_nasc):
    nascimento = datetime.strptime(data_nasc, "%d/%m/%Y")
    hoje = date.today()
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
    return idade

def validar_serie(serie):
    return serie in list(range(1, 10)) + [10, 20, 30]

def validar_bimestre(bimestre):
    return bimestre in [1, 2, 3, 4]

# ==============================
# Inicialização do Banco
# ==============================

def inicializar_banco():
    con = sqlite3.connect("escola.db")
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        cpf TEXT PRIMARY KEY,
        nome TEXT NOT NULL,
        email TEXT,
        data_nascimento TEXT,
        serie INTEGER
    )""")
    cur.execute("""
    CREATE TABLE IF NOT EXISTS disciplinas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cpf_aluno TEXT,
        nome_disciplina TEXT,
        FOREIGN KEY (cpf_aluno) REFERENCES alunos(cpf)
    )""")
    cur.execute("""
    CREATE TABLE IF NOT EXISTS notas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        disciplina_id INTEGER,
        bimestre INTEGER,
        nota REAL,
        FOREIGN KEY (disciplina_id) REFERENCES disciplinas(id)
    )""")
    con.commit()
    con.close()

# ==============================
# Cadastro de Aluno
# ==============================

def cadastrar_aluno():
    cpf = input("CPF do aluno (somente números): ").strip()
    if not validar_cpf(cpf):
        print("CPF inválido. Deve conter 11 dígitos numéricos.")
        return

    nome = input("Nome do aluno: ").strip()
    email = input("Email: ").strip()
    if not validar_email(email):
        print("Email inválido.")
        return

    data_nasc = input("Data de nascimento (dd/mm/aaaa): ").strip()
    if not validar_data_nascimento(data_nasc):
        print("Data inválida. Use o formato dd/mm/aaaa.")
        return

    idade = calcular_idade(data_nasc)
    if idade < 6 or idade > 60:
        print("Idade fora da faixa permitida (6 a 60 anos).")
        return

    serie = int(input("Série (1 a 9 ou 10, 20, 30): "))
    if not validar_serie(serie):
        print("Série inválida.")
        return

    con = sqlite3.connect("escola.db")
    cur = con.cursor()
    cur.execute("INSERT OR REPLACE INTO alunos (cpf, nome, email, data_nascimento, serie) VALUES (?, ?, ?, ?, ?)",
                (cpf, nome, email, data_nasc, serie))
    con.commit()
    con.close()
    print("Aluno cadastrado com sucesso.")

# ==============================
# Cadastro de Disciplina
# ==============================

def adicionar_disciplina():
    cpf = input("CPF do aluno: ").strip()
    disciplina = input("Nome da disciplina: ").strip()

    con = sqlite3.connect("escola.db")
    cur = con.cursor()
    cur.execute("INSERT INTO disciplinas (cpf_aluno, nome_disciplina) VALUES (?, ?)", (cpf, disciplina))
    con.commit()
    con.close()
    print("Disciplina adicionada com sucesso.")

# ==============================
# Lançamento de Nota
# ==============================

def adicionar_nota():
    cpf = input("CPF do aluno: ").strip()
    disciplina = input("Nome da disciplina: ").strip()
    bimestre = int(input("Número do bimestre (1 a 4): "))
    if not validar_bimestre(bimestre):
        print("Bimestre inválido. Deve ser 1, 2, 3 ou 4.")
        return

    nota = float(input("Nota: "))

    con = sqlite3.connect("escola.db")
    cur = con.cursor()
    cur.execute("SELECT id FROM disciplinas WHERE cpf_aluno = ? AND nome_disciplina = ?", (cpf, disciplina))
    resultado = cur.fetchone()
    if resultado:
        disciplina_id = resultado[0]
        cur.execute("INSERT INTO notas (disciplina_id, bimestre, nota) VALUES (?, ?, ?)",
                    (disciplina_id, bimestre, nota))
        con.commit()
        print("Nota registrada com sucesso.")
    else:
        print("Disciplina não encontrada.")
    con.close()

# ==============================
# Consultar Boletim
# ==============================

def consultar_boletim():
    cpf = input("CPF do aluno: ").strip()

    con = sqlite3.connect("escola.db")
    cur = con.cursor()
    cur.execute("SELECT nome, email, data_nascimento, serie FROM alunos WHERE cpf = ?", (cpf,))
    aluno = cur.fetchone()

    if aluno:
        nome, email, data_nasc, serie = aluno
        idade = calcular_idade(data_nasc)

        print(f"\nBoletim de {nome} - Série: {serie}º ano")
        print(f"Email: {email}")
        print(f"Data de nascimento: {data_nasc} - Idade: {idade} anos")

        cur.execute("SELECT id, nome_disciplina FROM disciplinas WHERE cpf_aluno = ?", (cpf,))
        disciplinas = cur.fetchall()
        for disciplina_id, nome_disciplina in disciplinas:
            print(f"\nDisciplina: {nome_disciplina}")
            cur.execute("SELECT bimestre, nota FROM notas WHERE disciplina_id = ? ORDER BY bimestre", (disciplina_id,))
            notas = cur.fetchall()
            total = 0
            for bimestre, nota in notas:
                print(f"  {bimestre}º Bimestre: {nota}")
                total += nota
            if notas:
                media = total / len(notas)
                print(f"  Média: {media:.2f}")
            else:
                print("  Nenhuma nota registrada.")
    else:
        print("Aluno não encontrado.")
    con.close()


#  ⛔ =========  Próximo código:  =========  ⛔ 




from cadastro import *

def menu():
    carregar_dados()
    while True:
        print("\n===== MENU =====")
        print("1 - Cadastrar aluno")
        print("2 - Adicionar disciplina")
        print("3 - Adicionar nota")
        print("4 - Consultar boletim")
        print("5 - Consultar aluno por nome")
        print("6 - Editar dados do aluno")
        print("7 - Excluir aluno")
        print("8 - Excluir disciplina")
        print("9 - Sair")

        opcao = input("Escolha: ")
        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            adicionar_disciplina()
        elif opcao == "3":
            adicionar_nota()
        elif opcao == "4":
            consultar_boletim()
        
        elif opcao == "7":
            excluir_aluno()
        elif opcao == "8":
            excluir_disciplina()

        elif opcao == "5":
            consultar_por_nome()
        elif opcao == "6":
            editar_aluno()
            #consultar_por_nome()
        elif opcao == "9":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()


#  ⛔ =========  Próximo código:  =========  ⛔ 


import tkinter as tk

# Função que será chamada ao clicar no botão
def dobrar_valor():
    try:
        numero = float(entrada.get())  # Tenta converter o valor digitado
        resultado.set(f"Dobro: {numero * 2:.2f}")  # Atualiza o texto com o dobro
    except ValueError:
        resultado.set("Digite um número válido!")

# Criando a janela principal
janela = tk.Tk()
janela.title("Dobrar Número")
janela.geometry("300x200")  # Define tamanho da janela (largura x altura)

# Label explicativo
tk.Label(janela, text="Digite um número:").pack()

# Campo de entrada
entrada = tk.Entry(janela)
entrada.pack()

# Botão que executa a função
tk.Button(janela, text="Dobrar", command=dobrar_valor).pack()

# Área onde o resultado será exibido
resultado = tk.StringVar()  # Variável dinâmica para o resultado
tk.Label(janela, textvariable=resultado, fg="blue").pack()

# Inicia o loop da interface
janela.mainloop()


#  ⛔ =========  Próximo código:  =========  ⛔ 

import tkinter as tk
from tkinter import messagebox
from funcoes_alunos_1 import criar_tabela, inserir_aluno, consultar_aluno, listar_todos, validar_cpf, validar_email
from datetime import datetime

# Função principal para cadastrar aluno com validações
def cadastrar():
    cpf = cpf_entry.get()
    nome = nome_entry.get()
    data_nasc = nasc_entry.get()
    serie = serie_entry.get()
    email = email_entry.get()

    if not cpf or not nome or not data_nasc or not serie:
        messagebox.showwarning("Atenção", "Preencha todos os campos obrigatórios.")
        return

    if not validar_cpf(cpf):
        messagebox.showerror("Erro", "CPF inválido! Deve conter 11 dígitos numéricos.")
        return

    if email and not validar_email(email):
        messagebox.showerror("Erro", "E-mail inválido!")
        return

    try:
        datetime.strptime(data_nasc, "%d/%m/%Y")
        serie_int = int(serie)
    except:
        messagebox.showerror("Erro", "Data deve estar no formato DD/MM/AAAA e Série deve ser número.")
        return

    sucesso = inserir_aluno(cpf, nome, data_nasc, serie_int, email)
    if sucesso:
        messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
        limpar_campos()
    else:
        messagebox.showerror("Erro", "CPF já cadastrado!")

def consultar():
    cpf = cpf_entry.get()
    if not validar_cpf(cpf):
        messagebox.showerror("Erro", "Digite um CPF válido para consultar.")
        return
    aluno = consultar_aluno(cpf)
    if aluno:
        nome_entry.delete(0, tk.END)
        nome_entry.insert(0, aluno[1])
        nasc_entry.delete(0, tk.END)
        nasc_entry.insert(0, aluno[2])
        serie_entry.delete(0, tk.END)
        serie_entry.insert(0, aluno[3])
        email_entry.delete(0, tk.END)
        email_entry.insert(0, aluno[4])
    else:
        messagebox.showinfo("Consulta", "Aluno não encontrado.")

def listar():
    alunos = listar_todos()
    janela_lista = tk.Toplevel(janela)
    janela_lista.title("Lista de Alunos")
    texto = tk.Text(janela_lista, width=70, height=20)
    texto.pack()
    for a in alunos:
        texto.insert(tk.END, f"""CPF: {a[0]}, Nome: {a[1]}, Nasc: {a[2]}, Série: {a[3]}, Email: {a[4]}
""")

# Função para limpar os campos
def limpar_campos():
    cpf_entry.delete(0, tk.END)
    nome_entry.delete(0, tk.END)
    nasc_entry.delete(0, tk.END)
    serie_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# Interface
janela = tk.Tk()
janela.title("Cadastro de Alunos")
janela.geometry("520x350")

tk.Label(janela, text="CPF*").grid(row=0, column=0, sticky="e", padx=5, pady=5)
cpf_entry = tk.Entry(janela, width=30)
cpf_entry.grid(row=0, column=1)

tk.Label(janela, text="Nome*").grid(row=1, column=0, sticky="e", padx=5, pady=5)
nome_entry = tk.Entry(janela, width=30)
nome_entry.grid(row=1, column=1)

tk.Label(janela, text="Dt_Nasc.* (DD/MM/AAAA)").grid(row=2, column=0, sticky="e", padx=5, pady=5)
nasc_entry = tk.Entry(janela, width=30)
nasc_entry.grid(row=2, column=1)

tk.Label(janela, text="Série*").grid(row=3, column=0, sticky="e", padx=5, pady=5)
serie_entry = tk.Entry(janela, width=30)
serie_entry.grid(row=3, column=1)

tk.Label(janela, text="E-mail").grid(row=4, column=0, sticky="e", padx=5, pady=5)
email_entry = tk.Entry(janela, width=30)
email_entry.grid(row=4, column=1)

# Botões com espaçamento
tk.Button(janela, text="Cadastrar", command=cadastrar, width=15).grid(row=5, column=0, pady=10)
tk.Button(janela, text="Consultar", command=consultar, width=15).grid(row=5, column=1)
tk.Button(janela, text="Listar Todos", command=listar, width=15).grid(row=6, column=0, columnspan=2, pady=5)

criar_tabela()
janela.mainloop()



#  ⛔ =========  Próximo código:  =========  ⛔ 

import tkinter as tk
from tkinter import messagebox
from funcoes_alunos import criar_tabela, inserir_aluno
from datetime import datetime

# Função de validação e cadastro
def cadastrar():
    cpf = cpf_entry.get()
    nome = nome_entry.get()
    data_nasc = nasc_entry.get()
    serie = serie_entry.get()
    email = email_entry.get()

    # Verifica se os campos obrigatórios foram preenchidos
    if not cpf or not nome or not data_nasc or not serie:
        messagebox.showwarning("Atenção", "Preencha todos os campos obrigatórios.")
        return

    try:
        # Valida o formato da data e da série
        datetime.strptime(data_nasc, "%d/%m/%Y")
        serie_int = int(serie)
    except:
        messagebox.showerror("Erro", "Data deve estar no formato DD/MM/AAAA e Série deve ser número.")
        return

    # Tenta inserir o aluno
    sucesso = inserir_aluno(cpf, nome, data_nasc, serie_int, email)
    if sucesso:
        messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
        limpar_campos()
    else:
        messagebox.showerror("Erro", "CPF já cadastrado ou erro na inserção.")

# Função para limpar os campos da interface
def limpar_campos():
    cpf_entry.delete(0, tk.END)
    nome_entry.delete(0, tk.END)
    nasc_entry.delete(0, tk.END)
    serie_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# Cria a janela principal
janela = tk.Tk()
janela.title("Cadastro de Alunos")
janela.geometry("500x300")

# Cria a grade de widgets
tk.Label(janela, text="CPF*").grid(row=0, column=0, sticky="e", padx=5, pady=5)
cpf_entry = tk.Entry(janela, width=30)
cpf_entry.grid(row=0, column=1)

tk.Label(janela, text="Nome*").grid(row=1, column=0, sticky="e", padx=5, pady=5)
nome_entry = tk.Entry(janela, width=30)
nome_entry.grid(row=1, column=1)

tk.Label(janela, text="Data de Nascimento* (DD/MM/AAAA)").grid(row=2, column=0, sticky="e", padx=5, pady=5)
nasc_entry = tk.Entry(janela, width=30)
nasc_entry.grid(row=2, column=1)

tk.Label(janela, text="Série*").grid(row=3, column=0, sticky="e", padx=5, pady=5)
serie_entry = tk.Entry(janela, width=30)
serie_entry.grid(row=3, column=1)

tk.Label(janela, text="E-mail").grid(row=4, column=0, sticky="e", padx=5, pady=5)
email_entry = tk.Entry(janela, width=30)
email_entry.grid(row=4, column=1)

# Botão para cadastrar
tk.Button(janela, text="Cadastrar", command=cadastrar, width=20).grid(row=5, column=0, columnspan=2, pady=20)

# Inicializa banco de dados
criar_tabela()

# Executa a janela
janela.mainloop()


#  ⛔ =========  Próximo código:  =========  ⛔ 


import sqlite3
from tkinter import *
from tkinter import messagebox

# Conectar e criar o banco SQLite
conn = sqlite3.connect('alunos_1.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS alunos_1
               (cpf TEXT PRIMARY KEY, nome TEXT, idade INTEGER, serie TEXT)''')

# Função para limpar campos
def limpar_campos():
    entry_cpf.delete(0, END)
    entry_nome.delete(0, END)
    entry_idade.delete(0, END)
    entry_serie.delete(0, END)

# Função para inserir alunos_1
def inserir_aluno():
    cpf = entry_cpf.get()
    nome = entry_nome.get()
    idade = entry_idade.get()
    serie = entry_serie.get()

    try:
        cursor.execute("INSERT INTO alunos_1 VALUES (?, ?, ?, ?)", (cpf, nome, idade, serie))
        conn.commit()
        messagebox.showinfo("Sucesso", "Aluno cadastrado!")
        limpar_campos()
    except sqlite3.IntegrityError:
        messagebox.showerror("Erro", "CPF já cadastrado!")

# Função para consultar alunos_1 por CPF
def consultar_aluno():
    cpf = entry_cpf.get()
    cursor.execute("SELECT * FROM alunos_1 WHERE cpf=?", (cpf,))
    aluno = cursor.fetchone()

    if aluno:
        entry_nome.delete(0, END)
        entry_nome.insert(0, aluno[1])

        entry_idade.delete(0, END)
        entry_idade.insert(0, aluno[2])

        entry_serie.delete(0, END)
        entry_serie.insert(0, aluno[3])
    else:
        messagebox.showinfo("Aviso", "Aluno não encontrado.")

# Função para atualizar dados do aluno
def atualizar_aluno():
    cpf = entry_cpf.get()
    nome = entry_nome.get()
    idade = entry_idade.get()
    serie = entry_serie.get()

    cursor.execute("UPDATE alunos_1 SET nome=?, idade=?, serie=? WHERE cpf=?",
                   (nome, idade, serie, cpf))
    conn.commit()
    messagebox.showinfo("Sucesso", "Aluno atualizado!")
    limpar_campos()
    texto_lista.grid_remove()

# Função para excluir aluno
def excluir_aluno():
    cpf = entry_cpf.get()

    cursor.execute("DELETE FROM alunos_1 WHERE cpf=?", (cpf,))
    conn.commit()
    messagebox.showinfo("Sucesso", "Aluno excluído!")
    limpar_campos()
    texto_lista.grid_remove()

# Função para listar todos os alunos_1
def listar_alunos_1():
    cursor.execute("SELECT * FROM alunos_1")
    registros = cursor.fetchall()
    texto_lista.delete(1.0, END)
    for aluno in registros:
        texto_lista.insert(END, f"CPF: {aluno[0]}, Nome: {aluno[1]}, Idade: {aluno[2]}, Série: {aluno[3]}\n")
    texto_lista.grid(row=7, column=0, columnspan=2, pady=10)

# Interface gráfica Tkinter
janela = Tk()
janela.title("Cadastro de alunos_1")

Label(janela, text="CPF:").grid(row=0, column=0)
entry_cpf = Entry(janela)
entry_cpf.grid(row=0, column=1)

Label(janela, text="Nome:").grid(row=1, column=0)
entry_nome = Entry(janela)
entry_nome.grid(row=1, column=1)

Label(janela, text="Idade:").grid(row=2, column=0)
entry_idade = Entry(janela)
entry_idade.grid(row=2, column=1)

Label(janela, text="Série:").grid(row=3, column=0)
entry_serie = Entry(janela)
entry_serie.grid(row=3, column=1)

Button(janela, text="Inserir", command=inserir_aluno).grid(row=4, column=0, pady=5)
Button(janela, text="Consultar", command=consultar_aluno).grid(row=4, column=1, pady=5)
Button(janela, text="Atualizar", command=atualizar_aluno).grid(row=5, column=0, pady=5)
Button(janela, text="Excluir", command=excluir_aluno).grid(row=5, column=1, pady=5)
Button(janela, text="Listar Todos", command=listar_alunos_1).grid(row=6, column=0, columnspan=2, pady=5)

# Caixa de texto para listar todos os alunos_1 (inicialmente oculta)
texto_lista = Text(janela, width=50, height=10)

janela.mainloop()

# Fechar a conexão quando o programa encerra
conn.close()


#  ⛔ =========  Próximo código:  =========  ⛔ 

import sqlite3
#aluno=[]
#aluno.append(("Maria", 14, 9.0))
#print(aluno)
#aluno.append(("Jose", 17, 8.0))
#print(aluno)
#aluno.append(("João", 13, 7.0))
#print(aluno)

alunos=[('silvio',50,8.5),('ema',25,9.0),('eric',12,7.5),('marcelo',24,7.0)]
#desempacotando os itens da lista - 4 indíces c/ 3 objetos
#for nome,idade,nota in alunos:
#    #print("iterando listas")
#   print(f"{nome} você tem  {idade}anos e sua nota é {nota}")

con = sqlite3.connect("alunos_db.db")
cur = con.cursor()
cur.execute(""" 
CREATE TABLE IF NOT EXISTS alunos_db (
    nome TEXT NOT NULL,
    idade INTEGER,
    nota REAL
)""")
#con.commit()

#cur.execute("INSERT INTO alunos_db (nome,idade,nota) VALUES('silvio', 50, '8.5')")
#con.commit()
#cur.execute("INSERT INTO alunos_db (nome,idade,nota) VALUES('ema', 25, '9.0')")
#con.commit()
# Inserção múltipla com executemany
cur.executemany("INSERT INTO alunos_db (nome, idade, nota) VALUES (?, ?, ?)", alunos,)
con.commit

# Executa a consulta para recuperar todos os alunos
#cur.execute("SELECT nome, idade, nota FROM alunos_db")

# Recupera todos os resultados como uma lista de tuplas
#alunos = cur.fetchall()

# Itera sobre os dados e imprime cada aluno
#for nome, idade, nota in alunos:
#    print("Dados do banco.")
#    print(f"{nome} tem {idade} anos e tirou nota {nota}")


cur.execute("UPDATE alunos_db SET idade = ? WHERE nome = ?", (23, "ema"))
con.commit()

cur.execute("DELETE FROM alunos_db WHERE nome = ?", ("silvio",))
con.commit()

# Fecha a conexão com o banco
con.close()



#  ⛔ =========  Próximo código:  =========  ⛔ 

# Solução – Análise de Vendas com Verificação de Preço + Mais/Menos Vendido (Corrigido)

frutas = ["banana", "maçã", "melancia", "abacaxi"]
cereais = ["aveia", "granola", "milho", "trigo", "linhaça"]

precos = {
    "banana": 2.00, "maçã": 2.50, "melancia": 7.00, "abacaxi": 5.50,
    "aveia": 4.00, "granola": 5.50, "milho": 3.80, "trigo": 4.50, "linhaça": 6.00
}

vendas = [
    ["banana", 5, 2.00],
    ["maçã", 8, 2.50],
    ["melancia", 4, 7.00],
    ["abacaxi", 4, 5.50],
    ["aveia", 6, 4.00],
    ["granola", 8, 5.50],
    ["milho", 4, 3.80],
    ["trigo", 7, 4.50],
    ["linhaça", 5, 6.00],
    ["maçã", 1, 2.00],        # abaixo do preço
    ["milho", 1, 4.50]        # acima do preço
]

resumo = {}
total_geral = 0
total_frutas = 0
total_cereais = 0

# Consolidar dados
for produto, qtd, valor_vendido in vendas:
    total_item = qtd * valor_vendido
    valor_real = precos[produto]

    if produto not in resumo:
        resumo[produto] = {
            "quantidade": 0,
            "total_vendido": 0
        }

    resumo[produto]["quantidade"] += qtd
    resumo[produto]["total_vendido"] += total_item

    total_geral += total_item

    if produto in frutas:
        total_frutas += total_item
    elif produto in cereais:
        total_cereais += total_item

# Determinar mais e menos vendidos corretamente
maior_qtd = max(d["quantidade"] for d in resumo.values())
menor_qtd = min(d["quantidade"] for d in resumo.values())

mais_vendidos = [p for p, d in resumo.items() if d["quantidade"] == maior_qtd]
menos_vendidos = [p for p, d in resumo.items() if d["quantidade"] == menor_qtd]

# Relatório
print("=== RELATÓRIO DE VENDAS ===")
for produto, dados in resumo.items():
    print(f"\nProduto: {produto}")
    print(f"  Quantidade vendida: {dados['quantidade']}")
    
# Totais finais
print("\n=== RESUMO FINAL ===")
print(f"💰 Total geral: R$ {total_geral:.2f}")
print(f"🍎 Total em frutas: R$ {total_frutas:.2f}")
print(f"🌾 Total em cereais: R$ {total_cereais:.2f}")
print(f"📈 Mais vendido(s): {', '.join(mais_vendidos)} ({maior_qtd} unidades)")
print(f"📉 Menos vendido(s): {', '.join(menos_vendidos)} ({menor_qtd} unidades)")


#  ⛔ =========  Próximo código:  =========  ⛔ 


import gestao_alunos_db_ref as sistema

def menu():
    sistema.inicializar_banco()
    while True:
        print("\nMenu do Sistema Escolar:")
        print("1 - Cadastrar aluno")
        print("2 - Adicionar disciplina")
        print("3 - Adicionar nota")
        print("4 - Consultar boletim")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            sistema.cadastrar_aluno()
        elif opcao == "2":
            sistema.adicionar_disciplina()
        elif opcao == "3":
            sistema.adicionar_nota()
        elif opcao == "4":
            sistema.consultar_boletim()
        elif opcao == "5":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()



#  ⛔ =========  Próximo código:  =========  ⛔ 


# Solução – Análise de Vendas com Verificação de Preço + Mais/Menos Vendido (sem usar min/max)

frutas = ["banana", "maçã", "melancia", "abacaxi"]
cereais = ["aveia", "granola", "milho", "trigo", "linhaça"]

precos = {
    "banana": 2.00, "maçã": 2.50, "melancia": 7.00, "abacaxi": 5.50,
    "aveia": 4.00, "granola": 5.50, "milho": 3.80, "trigo": 4.50, "linhaça": 6.00
}

vendas = [
    ["banana", 5, 2.00],
    ["maçã", 8, 2.50],
    ["melancia", 4, 7.00],
    ["abacaxi", 4, 5.50],
    ["aveia", 6, 4.00],
    ["granola", 8, 5.50],
    ["milho", 4, 3.80],
    ["trigo", 7, 4.50],
    ["linhaça", 5, 6.00],
    ["maçã", 1, 2.00],
    ["milho", 1, 4.50]
]

resumo = {}
total_geral = 0
total_frutas = 0
total_cereais = 0

# Consolidar os dados por produto
for produto, qtd, valor_vendido in vendas:
    total_item = qtd * valor_vendido
    if produto not in resumo:
        resumo[produto] = {"quantidade": 0, "total_vendido": 0}

    resumo[produto]["quantidade"] += qtd
    resumo[produto]["total_vendido"] += total_item

    total_geral += total_item

    if produto in frutas:
        total_frutas += total_item
    elif produto in cereais:
        total_cereais += total_item

# Encontrar manualmente o maior e menor vendidos
maior_qtd = -1
menor_qtd = float("inf")
mais_vendidos = []
menos_vendidos = []

for produto, dados in resumo.items():
    qtd = dados["quantidade"]

    # Verificando o maior vendido
    if qtd > maior_qtd:
        maior_qtd = qtd
        mais_vendidos = [produto]
    elif qtd == maior_qtd:
        mais_vendidos.append(produto)

    # Verificando o menor vendido
    if qtd < menor_qtd:
        menor_qtd = qtd
        menos_vendidos = [produto]
    elif qtd == menor_qtd:
        menos_vendidos.append(produto)

# Impressão do relatório
print("=== RELATÓRIO DE VENDAS ===")
for produto, dados in resumo.items():
    print(f"\nProduto: {produto}")
    print(f"  Quantidade vendida: {dados['quantidade']}")
    print(f"  Total vendido: R$ {dados['total_vendido']:.2f}")

print("\n=== RESUMO FINAL ===")
print(f"💰 Total geral: R$ {total_geral:.2f}")
print(f"🍎 Total em frutas: R$ {total_frutas:.2f}")
print(f"🌾 Total em cereais: R$ {total_cereais:.2f}")
print(f"📈 Mais vendido(s): {', '.join(mais_vendidos)} ({maior_qtd} unidades)")
print(f"📉 Menos vendido(s): {', '.join(menos_vendidos)} ({menor_qtd} unidades)")


