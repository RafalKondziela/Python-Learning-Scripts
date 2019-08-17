#Biblioteka MyCalculate - W założeniu ma być rozwijana o funkcje potrzebne na studiach do przedmiotów matematycznych.
#Tworzenie jej fnukcji ma pomóc w zrozumieniu zagadnień poszczególnych przedmiotów
#by: Siemowit


def dodaj(a,b):
    return a + b

def odejmij(a,b):
    return a - b

def pomnoz(a,b):
    return a * b

def podziel(a,b):
    if (b == 0):
        print("Nie dziel przez 0")

    else: return a / b

def pole_trojkata(a,h):
    return (0.5 * (a * h))


