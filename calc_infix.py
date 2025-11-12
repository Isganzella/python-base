#!/usr/bin/env python3

"""Caclculadora Infix

Funcionamento:

[operacao] [n1] [n2]

Opercacoes possiveis:

sum -> +
sub -> -
mul -> *
div -> /

Uso:

$ calc_infix.py sum 5 2
7

$ calc_infix.py mul 10 5
50

"""

__version__ = "0.1.0"
__author__ = "Marlos Isganzella"


import os
import sys
from datetime import datetime
import logging
logging.basicConfig(
    filename="app.log",
    encoding="utf-8",
    filemode="a",
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)


arguments = sys.argv[1:]

if not arguments:
    operation = input("operacao: ")
    n1 = input("n1: ")
    n2 = input ("n2")
    arguments = [operation, n1, n2]
elif len(arguments) !=3:
    print("Numero de argumentos incorreto!")
    print("ex: sum 5 5")
    sys.exit(1)

operation, *nums = arguments

valid_operations = ("sum", "sub", "mul", "div")

if operation not in valid_operations:
    print("Operacao Invalida")
    logging.error("Operacao Invalida")
    print(valid_operations)
    sys.exit(1)

validated_nums = []
for num in nums:
    if not num.replace(".", "").isdigit():
        print(f"Numero invalido {num}")
        logging.error("Número inválido")
        sys.exit(2)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

n1, n2 = validated_nums

resultado = 0
if operation == "sum":
    resultado = n1 + n2
elif operation == "sub":
    resultado = n1 - n2
elif operation == 'mul':
    resultado = n1* n2
elif operation == 'div':
    resultado  = n1 / n2





# path = os.curdir
# filepath = os.path.join(path, "infix.txt")
# timestamp = datetime.now().isoformat()

# with open(filepath, 'a') as file_:
#     file_.write(f"date={timestamp} - {operation} {n1} {n2} = {resultado}\n")

print(resultado)
