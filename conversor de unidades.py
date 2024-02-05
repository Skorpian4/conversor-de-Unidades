import os 
import time
y='s'

def menu():
    while y == 'n' or 'N':
        e = int(input('Deseja converter temperaturas ou distâncias: \n [1]- Temperaturas \n [2]- Distancias'))
        if e == 1: 
            temp()
            y = str(input('Deseja realizar mais algum calculo? '))
            if y != 'n' or 'N':
                print('Retornando ao inicio')               
        elif e == 2:
            distancia()
            y = str(input('Deseja realizar mais algum calculo? '))
            if y != 'n' or 'N':
                print('Retornando ao inicio')   
        else:
           os.system('cls')
           print('Opção inválida')
           time.sleep(2)
           os.system('cls') 

def temp():
    while True:
        os.system('cls')
        print('Indique uma das seguintes opções')
        esc = int(input('[1]- Graus Celsius para Fahrenheit \n [2]- Fahrenheit para Graus Celsius: (Escolha uma destas duas opções) '))
        if esc == 1:
            os.system('cls')
            t = float(input('Indique a temperatura que deseja converter em graus: '))
            f = (t * 1.8) + 32
            os.system('cls')
            print('A temperatura convertida em Fahrenheit é igual: ',f)
            time.sleep(2)
            os.system('cls')
            break
        elif esc == 2:
            os.system('cls')
            t = float(input('Indique a temperatura que deseja converter em Fahrenheit: '))
            f = (t -32) /1.8
            os.system('cls')
            print('A temperatura convertida em Graus é igual: ',f)
            time.sleep(2)
            os.system('cls')
            break
        else:
            os.system('cls')
            print('Opção inválida')
            time.sleep(2)
            os.system('cls')

def distancia():
    while True:
        os.system('cls')
        print('Indique uma das seguintes opções')
        esc = int(input('[1] - Quilometros (KM) para milhas \n [2] - Milhas para Quilometros (KM) '))  
        if esc == 1:
            os.system('cls')
            d = float(input('Indique a distancia em quilometros que deseja converter: '))
            time.sleep(1)
            m = d / 1.609
            os.system('cls')
            print('A distância convertida em milhas é igual: ',m)
            time.sleep(2)
            break

        if esc == 2:
            os.system('cls')
            d = float(input('Indique a distancia em milhas que deseja converter: '))
            time.sleep(1)
            m = d / 0.62137
            os.system('cls')
            print('A distância convertida em quilometros é igual: %2.2f',m)
            time.sleep(2)
            break
            
        else:
            os.system('cls')
            print('Opção inválida')
            time.sleep(2)  

#Inicio
print('Bem vindo ao conversor de Unidades')
time.sleep(1)
os.system('cls')
menu()
print('Desligando do programa \n adeus.')      