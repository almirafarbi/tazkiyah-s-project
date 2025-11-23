
angka = int(input("input angka: "))
prima = "prima"

if (angka == 1 or angka == 0):
    prima = "bukan prima"
for i in range(2,angka):
        if (angka  % i == 0):
         prima = "bukan prima"


print (prima)         
