# Bibliotecas utilizadas

from time import sleep # Função que executa determinado comando depois de determina tempo.
from os import system, name # Funções para limpar o terminal.
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
    escolha = str(input('\033[34mEu escolho:\n')).lower().replace(' ', '')
    if escolha not in ['pedra', 'papel', 'tesoura']:
        print('\n\033[31mDigite um valor válido!\033[m\n')
        return
    print('\n\033[35mO computador escolhe... ')
    sleep(2)
    print('{}\n'.format(escolha_computador.capitalize()))
    sleep(2)
    match (escolha, escolha_computador):
# Verifica se houve um empate...
        case ('pedra', 'pedra') | ('papel', 'papel') | ('tesoura', 'tesoura'):
            print('\033[34m{}\033[m - \033[35m{}\n\n   \033[0;7mEmpate!\033[m\n'.format(escolha.capitalize(), escolha_computador.capitalize()))

# Verifica se o usuário venceu...
        case ('pedra', 'tesoura') | ('papel', 'pedra') | ('tesoura', 'papel'):
            print('\033[34m{}\033[m - \033[35m{}\033[32m\n\nVocê venceu!\033[m\n'.format(escolha.capitalize(), escolha_computador.capitalize()))

# Verifica se o computador venceu...
        case ('pedra', 'papel') | ('papel', 'tesoura') | ('tesoura', 'papel'):
            print('\033[34m{}\033[m - \033[35m{}\033[31m\n\nVocê perdeu!\033[m\n'.format(escolha.capitalize(), escolha_computador.capitalize()))
    
    print('\033[31m----- FIM de JOGO -----\033[35m\n')
    sleep(2.2)
    print('----- Aguarde -----\033[m')
    sleep(3.5)
    system('cls' if name == 'nt' else 'clear')

# Estrutura de decisão para o jogo recomeçar (dependendo da decisão do usuário)
while True:
    jogo_jokenpo() # Inicia o jogo
    resposta = input('\033[33mDeseja jogar novamente? \033[m(\033[32mS\033[m\033[m/\033[31mN\033[m):  ').upper().replace(' ', '')
    match resposta:
        case 'S' | 'SIM': # Caso resposta for "S" ou "SIM" recomeça o programa.
            print('\033[35m\n----- Recomeçando -----\033[m')
            sleep(1.7)
            system('cls' if name == 'nt' else 'clear')
        case _: # Caso não, finaliza a repetição.
            print('\n\033[36m--- Até mais! ---\033[m\n')
            break
