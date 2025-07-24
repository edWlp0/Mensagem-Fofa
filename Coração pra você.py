# 💚 Mensagem pra uma pessoa que tá ficando especial 💚
# Feito com carinho por alguém que sorri só de pensar em você :)

import time
import os

# Limpa a tela (Windows ou Linux/Mac)
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Arte do coraçãozinho
coracao = """
       ******       ******
     **********   **********
   ************* *************
  *****************************
  *****************************
   ***************************
     ***********************
       *******************
         ***************
           ***********
             *******
               ***
                *
"""

# Mensagem estilo crush que vale ouro 💬
mensagem = [
    "Oi, você 🫣",
    "Talvez eu não diga muito, mas adoro conversar contigo 😄",
    "Você tem um jeitinho que é impossível não gostar 🫶",
    "Quando vejo sua mensagem, o dia fica melhor de verdade ☀",
    "Não sei se percebeu, mas... você anda ocupando uns pensamentos meus 🧠💭",
    "Enfim... só queria te deixar essa vibe boa mesmo 😅",
    "Tamo junto, de coração aberto 💚"
]

# Começo do programa
limpar_tela()
print(coracao)
time.sleep(2)

for frase in mensagem:
    print("💌", frase)
    time.sleep(2)

print("\n✨ Fim da mensagem. Mas quem sabe... seja só o começo :) ✨")
print("🚀 Feito com carinho por alguém que tá curtindo te conhecer 💚")
