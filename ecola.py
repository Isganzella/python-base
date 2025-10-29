#!/usr/bin/env python 3

"""Exibe relatorio de criancas por atividades

Imprimir a lista de criancas agrupadas por salas
que frequentam cada umas das atividades

"""

__version__ = '0.1.0'

#Dados

sala1 = ['Erik','Maia', 'Gustavo', 'Manuel', 'Sofia', 'Joana']
sala2 = ['Joao', 'Antonio', 'Carlos', 'Maria','Isolda']


aula_ingles = ["Erik",'Maia', 'Joana', 'Carlos', 'Antonio']
aula_musica = ['Erik', 'Sofia', 'Maria']
aula_danca = ['Gustavo', 'Sofia', 'Joana', 'Antonio']

atividades = [
            ("Ingles", aula_ingles), 
            ("Musica", aula_musica), 
            ("Danca", aula_danca)
]

for nome_atividade, atividade in atividades:

    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2) & set(atividade)

    """ for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)"""

    print(f'A {nome_atividade} sala 1:', atividade_sala1)
    print(f'A {nome_atividade} sala 2:', atividade_sala2)
    print('-' * 30)
