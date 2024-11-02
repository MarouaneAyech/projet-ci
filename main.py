# main.py
from cal import somme, soustraction, produit, division

def main():
    a = float(input("Entrez le premier nombre : "))
    b = float(input("Entrez le deuxième nombre : "))
    operateur = input("Entrez l'opérateur (+, -, *, /) : ")

    if operateur == '+':
        print("Résultat :", somme(a, b))
    elif operateur == '-':
        print("Résultat :", soustraction(a, b))
    elif operateur == '*':
        print("Résultat :", produit(a, b))
    elif operateur == '/':
        print("Résultat :", division(a, b))
    else:
        print("Opérateur non valide")

if __name__ == "__main__":
    main()
