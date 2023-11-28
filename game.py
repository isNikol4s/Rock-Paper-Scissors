import random, os
cpu = random.randint(1, 3)

papel = 'Papel' 
tesoura = 'Tesoura'
pedra ='Pedra'

os.system('cls')
player = int(input('(1) Papel (2) Tesoura (3) Pedra\nDigite: '))

if (player == 3 and cpu == 2) or (player == 2 and cpu == 1) or (player == 1 and cpu == 3):
        print(f'Você Venceu!\nCPU: {cpu} V.s Player:{player}')
elif player == cpu:
        print(f'Empatou!')
else:
    print(f'Você Perdeu tente Novamente!\n CPU: {cpu} V.s Player:{player}')