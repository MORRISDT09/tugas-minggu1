# ==================================================
# Tugas Mandiri Modul 1 - Program Percabangan
# Nama : Jesar Dian Muhammad
# NIM : 714260023
# Kelas : 1B D4 TI
# ==================================================
print("=" * 50)
print("Program Penentuan Huruf Mutu")
print("=" * 50)  

try:
    nilai = float(input("Masukkan nilai akhir (0-100): "))
except ValueError:
    print("-" * 50)
    print("Input tidak valid. Harap masukkan angka.")
    print("-" * 50)
    print("Terima kasih telah menggunakan program ini.")
    print("=" * 50)
    raise SystemExit

print("-" * 50)

if nilai < 0 or nilai > 100:
    print("Nilai harus berada dalam rentang 0-100.")
else:
    if nilai >= 80:
        huruf = "A"
    elif nilai >= 70:
        huruf = "B"
    elif nilai >= 60:
        huruf = "C"
    elif nilai >= 50:
        huruf = "D"
    else:
        huruf = "E"

    if huruf in ("A", "B"):
        keterangan = "Lulus"
    else:
        keterangan = "Tidak lulus"

    print(f"Nilai angka : {nilai}")
    print(f"Nilai huruf : {huruf}")
    print(f"Keterangan : {keterangan}")

print("-" * 50)
print("Terima kasih telah menggunakan program ini.")    
print("=" * 50)  
print("=" * 50)
print("Nama : Jesar Dian Muhammad")
print("NIM : 714260023")
print("Kelas : 1B D4 Teknik Informatika")
print("=" * 50) 