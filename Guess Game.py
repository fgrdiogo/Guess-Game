import random 

x = random.randint(0, 5)
chances = 2

while (chances > 0):
    y = int(input("Digite um número: "))

    if y == x:
        print("Você ganhou!")
        break

    elif y > x: 
        print("Mais baixo!")
        chances = chances - 1

    elif y < x:
        print("Mais alto!")
        chances = chances - 1
    
if chances == 0:
    print("FIM DE JOGO! Você perdeu")

else:
    print("FIM DE JOGO")

