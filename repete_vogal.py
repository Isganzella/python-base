"""
Faça um programa que pede ao usuário que digite uma ou mais palavras e 
imprime cada uma das palavras com as suas vogais duplicadas

ex:

python repete_vaogal.py
"Digite uma palavra (ou enter para sair): " Python
Pythoon

"""

vogais = ("a", "e", "i", "o", "u")

while True:
    word = input("Digite uma palavra (ou enter para sair): ").strip()
    if word == "":
        break
    new_word = []
    for letter in word.lower():
        if letter in vogais:
            new_word.append(letter * 2)
        else:
            new_word.append(letter)
    new_word = "".join(new_word)
    print(new_word)
            
