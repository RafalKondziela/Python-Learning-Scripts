import string
import sys

test = "alaMaKota"

test = test.capitalize()

print(test)


a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = a+b

print(a, " + ", b, " = ", c)

print("Liczba argumentów przekazana do systemu to: ", str(sys.argv))

print("Nazwa programu to: ", sys.argv[0])
#print("Wynik dodawania parametrów to: ", sys.arg[1] + sys.arg[2])



pLitera = str(input("Podaj pierwsza litere imienia: "))
nazwisko = str(input("Podaj nazwisko: "))
fullName = pLitera + (".") + nazwisko

print(fullName)


test = test.upper()
print(test)

first = str(input("Podaj dwie pierwsze cyfry aktualnego roku: "))
last = str(input("Podaj dwie koncowe cyfry aktualnego roku: "))
age = int(input("Podaj swoj wiek: "))
year = first+last
year = int(year)
yearOfBirth = year - age

print("Twój rok urodzenia to: ", yearOfBirth)
