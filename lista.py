import re
import random
# Genera un numero random che verra' preso come parametro nella nostra funzione scorri e mostrera' la persona che deve fare la lista

lista = ["Anastasi", "Delio", "Sali", "Dashi", "Marco"]


def scorri(index):
    print("La lista verra' fatta da " + lista[index])


scorri(random.randint(0, 4))
