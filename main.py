from datetime import datetime
import random
import time

zonas = ["Zona 1", "Zona 2", "Zona 3"]

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
contador_alertas = {"Zona 1":0,
                    "Zona 2":0,
                    "Zona 3":0
}
while True:
        
    agora = datetime.now()
    data_formatada = agora.strftime("%Y/%m/%d | %H:%M:%S")
    
    for zona in zonas:
        temp = gerar_temperatura()
        status = verificar_temperatura(temp)
        

        if temp > 30:
            contador_alertas[zona] += 1

        mensagem = f"{zona} | {status} | Alerta: {contador_alertas[zona]} | {data_formatada}"
        
        print(f'{mensagem}')
        salvar_log(mensagem)
        print("-"*65)
    
        time.sleep(2)