from time import sleep # Função que executa determinado comando depois de determina tempo.
from os import system, name # Funções para limpar o terminal.
from random import randint # Função para escolher um número aleatório (e converte-lo em uma condição).

def jogo_jokenpo():

    escolha_bot = randint(1, 3)

    if escolha_bot == 1:
        escolha_bot = 'pedra'
    elif escolha_bot == 2:
        escolha_bot = 'papel'
    elif escolha_bot == 3:
        escolha_bot = 'tesoura'

    print('----------------------')
    print('\033[36m   Jogo de Jokenpô\033[m')
    print('----------------------')

    print(''' Qual a sua escolha?

    \033[31m● Pedra
    \033[32m● Papel
    \033[33m● Tesoura\033[m

----------------------''')
    escolha = str(input('\033[34mEu escolho:\n'))
    escolha = escolha.lower().replace(' ', '')
    print('\n\033[35mO computador escolhe... ')
    sleep(2)
    print('{}\n'.format(escolha_bot.capitalize()))
    sleep(2)

    if escolha == 'pedra' and escolha_bot == 'pedra' or escolha == 'papel' and escolha_bot == 'papel' or escolha == 'tesoura' and escolha_bot == 'tesoura':
        print('\033[34m{}\033[m - \033[35m{}\033[0;7m\nEmpate!\033[m\n'.format(escolha.capitalize(), escolha_bot.capitalize()))

    elif escolha == 'pedra' and escolha_bot == 'tesoura' or escolha == 'papel' and escolha_bot == 'pedra' or escolha == 'tesoura' and escolha_bot == 'papel':
        print('\033[34m{}\033[m - \033[35m{}\033[32m\nVocê venceu!\033[m\n'.format(escolha.capitalize(), escolha_bot.capitalize()))

    elif escolha == 'pedra' and escolha_bot == 'papel' or escolha == 'papel' and escolha_bot == 'tesoura' or escolha == 'tesoura' and escolha_bot == 'papel':
        print('\033[34m{}\033[m - \033[35m{}\033[31m\nVocê perdeu!\033[m\n'.format(escolha.capitalize(), escolha_bot.capitalize()))
    
    else:
        print('\n\033[31mDigite um valor válido!\033[m')
    print('\033[31m----- FIM de JOGO -----\033[35m\n')
    sleep(3)
    print('Reiniciando...\n')
    sleep(2)
    print('----- Aguarde -----\033[m')
    sleep(8)
    system('cls' if name == 'nt' else 'clear')


while True:
    jogo_jokenpo()
    resposta = input('Deseja jogar novamente? (S/N):  ').upper().replace(' ', '')
    print('\033[35m\n----- Recomeçando -----\033[m')
    sleep(3)
    system('cls' if name == 'nt' else 'clear')
    if resposta != 'S':
        break
