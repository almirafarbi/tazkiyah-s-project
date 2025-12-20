data = [3, 7, 8, 15, 19, 23, 31, 42]
target = 31

left = 0
right = len(data) - 1
count = 0

while left <= right:
    count += 1
    mid = (left + right) // 2

    if data[mid] == target:
        print(f"Angka {target} ditemukan di indeks {mid}")
        break
    elif data[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

print(f"Jumlah pengecekan (Binary Search): {count}")