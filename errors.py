#!/usr/bin/env python3
"""Exemplo de tratamento de erros
"""
import os
import sys

# if os.path.exists("names.txt"):
#     input("...")
#     names = open("names.txt").readlines()
# else: 
#     print('[Error 2] File names.txt not found')
#     sys.exit(1)

try:
    names = open("names.txt").readlines()
except FileNotFoundError as e:
     print(f"{str(e)}")
     sys.exit(1)
    #TODO usar retry
else:
    print("Sucesso!")

finally:
    print("Execute isso sempre!")
try:
    print(names[2])
except IndexError as e:
    print(str(e).capitalize())
    sys.exit(2)