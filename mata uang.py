usd = 16000  # 1 USD = 16.000 IDR
jpy = 112    # 1 JPY = 112 IDR

rupiah = int(input("Masukkan jumlah Rupiah: "))


usd = rupiah / usd
jpy = rupiah / jpy

# output hasil
print("Hasil konversi:")
print("USD:", usd)
print("JPY:", jpy)