data = [15, 8, 23, 42, 7, 31, 19, 3]
target = 31

count = 0
found = False

for i in range(len(data)):
    count += 1
    if data[i] == target:
        print(f"Angka {target} ditemukan di indeks {i}")
        break

print(f"Jumlah pengecekan (Linear Search): {count}")