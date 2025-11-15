"""
Faça um programa que imprime os números pares de 1 a 200

ex:

python3 ex.py

2
4
6
8
"""

#for i in range(201):
    #if i % 2 == 0:
        #print(i)


"""
Alarme de temperatura

Faça um script que pergunta ao usuario qual a temperatura atual e o indice de umidade do ar 
sendo que caso será exibido uma mensagem de alerta dependendo das seguintes condições

tem maior que 45: ALERTA!!! Perigo calor extremo
temp vezes 3 for maior ou igual a umidade: ALERTA!!! Perido de calor umido
temp entre 10 e 30: Normal
temp entre 0 e 10: Frio
temp menor que 0 : frio extermo

"""

temp = int(input("informe a temperatua: "))
umi = int(input("informe a umidade: "))

if temp >= 45:
    print("ALERTA!!! Perigo calor extremo")
elif temp * 3 >= umi:
    print("ALERTA!!! Perido de calor umido")
elif temp >= 10 or temp <=30:
    print("Normal")
elif temp >=0 or temp <=10:
    print("Frio")
elif temp < 0:
    print("Frio Extermo")

