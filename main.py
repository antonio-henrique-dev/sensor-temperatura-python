import random
import time

def gerar_temperatura():
    return random.randint(20, 40)

def verificar_temperatura(temp):
    if temp > 30:
        return f'Alerta, {temp} C° Temperatura Alta! '

    else:
        return f'{temp} C° Temperatura Normal!'

def salvar_log(mensagem):
    with open('log.txt', 'a') as f:
        f.write(mensagem + '\n')
contador_alerta = 0
while True:
    temperatura = gerar_temperatura()
    mensagem = verificar_temperatura(temperatura)
    if temperatura > 30:
        contador_alerta += 1
    print(f'{mensagem} | Total de Alerta: {contador_alerta} ' )
       
    salvar_log(mensagem)
    
    time.sleep(2)