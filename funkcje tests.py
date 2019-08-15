import string



def imieINazwisko(imie,nazwisko):
    return (imie + " " + nazwisko)


imie = str(input("Podaj imie: "))
nazwisko = str(input("Podaj nazwisko: "))


print(imieINazwisko(imie,nazwisko))
