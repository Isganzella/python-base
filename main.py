#!/usr/bin/env python3
"""Menu Principal - Python Learning Scripts

Coleção de scripts Python para aprendizado.
"""

__version__ = "1.0.0"
__author__ = "Marlos Isganzella"

import subprocess
import sys

def run_script(script_name):
    """Execute um script Python"""
    try:
        subprocess.run([sys.executable, script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"\nErro ao executar {script_name}: {e}")
    except FileNotFoundError:
        print(f"\nScript {script_name} não encontrado!")

def main():
    while True:
        print("\n" + "="*50)
        print("MENU PRINCIPAL - Scripts Python")
        print("="*50)
        print("\n1. Hello World (Multi-idiomas)")
        print("2. Calculadora Infix")
        print("3. Tabuada (1 a 10)")
        print("4. Escola - Relatório de Atividades (ecola.py)")
        print("5. Escola - Exemplo Incompleto (escola.py)")
        print("0. Sair")
        print("\n" + "="*50)
        
        choice = input("\nEscolha uma opção: ").strip()
        
        if choice == "1":
            print("\n--- Executando Hello World ---")
            run_script("hello.py")
        elif choice == "2":
            print("\n--- Calculadora Infix ---")
            run_script("calc_infix.py")
        elif choice == "3":
            print("\n--- Tabuada ---")
            run_script("tabuada.py")
        elif choice == "4":
            print("\n--- Escola (ecola.py) ---")
            run_script("ecola.py")
        elif choice == "5":
            print("\n--- Escola (escola.py) - Incompleto ---")
            run_script("escola.py")
        elif choice == "0":
            print("\nSaindo... Até logo!")
            sys.exit(0)
        else:
            print("\nOpção inválida! Tente novamente.")
        
        input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPrograma interrompido. Até logo!")
        sys.exit(0)
