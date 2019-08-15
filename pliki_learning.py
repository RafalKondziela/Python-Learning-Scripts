plik_parzyste = open("plik_parzyste.txt", "w+")
plik_nieparzyste = open("plik_nieparzyste.txt", "w+")


for i in range(6):
    x = int(input("Podaj liczbe: "))
    if (x%2 == 0):
       x = str(x)
       plik_parzyste.write(x + "\n")
       
    else:
        x = str(x)
        plik_nieparzyste.write(x + "\n")
    i +=1
    


plik_parzyste.close()
plik_nieparzyste.close()
