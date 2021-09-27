import random
def run():
    print('BIENVENIDO AL JUEGO ADIVINA EL NÚMERO')
    numero_aleatorio = random.randint(1, 100)
    numero_usuario = int(input('Ingresa un numero del 1-100: '))
    while True:
        if numero_usuario > numero_aleatorio:
            print('Ingresa un numero menor!')
        elif numero_usuario < numero_aleatorio:
            print('Ingresa un número mayor!')
        else:
            print('Ganaste')
            break
        numero_usuario = int(input('Busca otro número: '))


if __name__== '__main__':
    run()