# Bibliotecas utilizadas

from time import sleep # Função que executa determinado comando depois de determina tempo.
from os import system, name # Funções para limpar o terminal.
from sys import exit # Função para finalizar código.
from random import choice # Função para escolher um número aleatório (usamos para converte-lo em uma condição).

# Função do jogo
def jogo_jokenpo():

# Escolhendo um valor da lista e o inserindo na variável
    possibilidades = ['pedra','papel','tesoura']
    escolha_computador = choice(possibilidades)

# Capa do jogo
    print('----------------------')
    print('\033[36m   Jogo de Jokenpô\033[m')
    print('----------------------')

# Opções de escolha
    print(''' Qual a sua escolha?

    \033[31m● Pedra
    \033[32m● Papel
    \033[33m● Tesoura\033[m

----------------------''')
# Opção de escolha do usuário
    escolha = str(input('\033[34mEu escolho:\n'))
    escolha = escolha.lower().replace(' ', '') # Deixa as letras em minúsculo e retira os espaços, para minimizar os erros por escrita
# Imprime a escolha do computador
    print('\n\033[35mO computador escolhe... ')
    sleep(2)
    print('{}\n'.format(escolha_computador.capitalize()))
    sleep(2)

# Verifica se houve um empate...
    if escolha == 'pedra' and escolha_computador == 'pedra' or escolha == 'papel' and escolha_computador == 'papel' or escolha == 'tesoura' and escolha_computador == 'tesoura':
        print('\033[34m{}\033[m - \033[35m{}\n\n   \033[0;7mEmpate!\033[m\n'.format(escolha.capitalize(), escolha_computador.capitalize()))

# Verifica se o usuário venceu...
    elif escolha == 'pedra' and escolha_computador == 'tesoura' or escolha == 'papel' and escolha_computador == 'pedra' or escolha == 'tesoura' and escolha_computador == 'papel':
        print('\033[34m{}\033[m - \033[35m{}\033[32m\n\nVocê venceu!\033[m\n'.format(escolha.capitalize(), escolha_computador.capitalize()))

# Verifica se o computador venceu...
    elif escolha == 'pedra' and escolha_computador == 'papel' or escolha == 'papel' and escolha_computador == 'tesoura' or escolha == 'tesoura' and escolha_computador == 'papel':
        print('\033[34m{}\033[m - \033[35m{}\033[31m\n\nVocê perdeu!\033[m\n'.format(escolha.capitalize(), escolha_computador.capitalize()))
    
# Executa-se caso o usuário digite um valor inválido
    else:
        print('\n\033[31mDigite um valor válido!\033[m')
    print('\033[31m----- FIM de JOGO -----\033[35m\n')
    sleep(2)
    print('----- Aguarde -----\033[m')
    sleep(5.5)
    system('cls' if name == 'nt' else 'clear')

# Estrutura de decisão para o jogo recomeçar (dependendo da decisão do usuário)
while True:
    jogo_jokenpo() # Inicia o jogo
    resposta = input('Deseja jogar novamente? (S/N):  ').upper().replace(' ', '')
    print('\033[35m\n----- Recomeçando -----\033[m')
    if resposta != 'S': # Se a variável "resposta" for diferente de "S" ou "SIM", finaliza o programa
        exit()
    sleep(2.3)
    system('cls' if name == 'nt' else 'clear')
