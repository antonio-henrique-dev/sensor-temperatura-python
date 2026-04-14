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
                    "Zona 3":0}

limites = {"Zona 1": 30,
           "Zona 2": 35,
           "Zona 3": 28}

while True:
        
    agora = datetime.now()
    data_formatada = agora.strftime("%Y/%m/%d | %H:%M:%S")

    for zona in zonas:
        temp = gerar_temperatura()
        limite = limites[zona]
    
        
        if temp > limite:
            contador_alertas[zona] += 1
            status = f'Alerta, {temp} C° (Limite {limite}° )'
        else:
            status = f'Normal, {temp} C° (Limite {limite}° )'
        
        mensagem = f"{zona} | {status} | Alerta: {contador_alertas[zona]} | {data_formatada}"
        print(f'{mensagem}')
        salvar_log(mensagem)
        print("-"*75)
        time.sleep(2)

    print("\n" + "="*30)
    print("=====RESUMO GERAL=====")
    print("="*30)
    for zona in zonas:
        print(f"{zona}: {contador_alertas [zona]} alertas")
    print("="*30 + "\n" )

        
    
        
    