##Dice simulator: Write a program that simulates the roll of two dice and calculates the sum of
##the values obtained.

import random

def roll_two_dice():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    return die1,die2

def main():
 
    die1, die2 = roll_two_dice()
    print(f"Resultado del dado 1: {die1}")
    print(f"Resultado del dado 2: {die2}")
    print(f"Sum total: ",die1+die2)
    
def main():
    results = [] # Lista para almacenar los resultafos de los datos

    for i in range(1,1001): # repetir 1000 veces
        die1, die2 = roll_two_dice()
        total = die1 +die2
        results.append((i, die1, die2, total)) # Añadir el número de tirada 
        
if __name__ == "__main__":
    main()