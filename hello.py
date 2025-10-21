#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente
o programa exibe a mensagem correspondente.

Como usar:

Tenha a váriavel LANG devidademente configurada ex:

    export LANG=pt_BR

Execução:

    python3 heelo.py ou 
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Marlos Isganzella"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]
print(f"current_language: {current_language}")

msg = "Hello, World!"

if current_language == "pt_br":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"

print(msg)
