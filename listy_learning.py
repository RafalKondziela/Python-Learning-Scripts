lista ={input("Podaj imie: "), input("Podaj nazwisko: "), input("Podaj wiek : ")}

krotka = tuple(lista)

print(krotka)



slownik = {"1" : "Poniedziałek", "2" : "Wtorek", "3" : "Środa", "4" : "Czwartek", "5" : "Piątek", "6" : "Sobota", "7" : "Niedziela"}

ulubionyDzien = input("Podaj numer ulubionego dnia tygodnia : ")

print("Twój ulubiony dzień tygodnia to : " + slownik[ulubionyDzien])


