print('Olá, eu vou pensar em um numero entre 1 e 5')
print('tente adivinhar')
import random
numero_secreto = random.randint(1, 5)
chute = int(input('qual numero eu pensei?'))
if chute == numero_secreto:
    print(f'Parabens voce acertou, eu pensei no numero:{numero_secreto}')
else:
    print(f'voce errou não é o numero:{chute} eu pensei no numero:{numero_secreto}')