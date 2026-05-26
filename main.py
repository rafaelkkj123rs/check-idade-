import time
import os
from tqdm import tqdm

os.system("cls")

def limpar():
    os.system("cls")

# CODIGO

for i in tqdm(range(100)):
    time.sleep(0.010)
limpar()

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade, idade minima é 18: "))

if idade >= 18:
    print("acesso liberado")
    time.sleep(1)
    limpar()
    print(f"seu nome é {nome}, e você tem {idade}")
else:
    print("acesso não liberado")


    # DESAFIO QUEM MANDOU CHAT GPT