print("=" * 50)
print("KONVERSI NILAI ANGKA KE HURUF MUTU".center(50))
print("=" * 50)


try:
    nilai = float(input("Masukkan nilai akhir (0-100): "))
except ValueError:
    print("-" * 50)
    print("Input tidak valid! Masukkan angka saja. contoh: 85")
    print("-" * 50)
    print("Terima kasih telah menggunakan program ini.")
    print("=" * 50)
    raise SystemExit

print("-" * 50)
    
if nilai < 0 or nilai > 100:
    print("Nilai ditolak! Nilai harus berada di rentang 0-100.")
else:
    if nilai >= 85:
        huruf = "A"
    elif nilai >= 70:
        huruf = "B"
    elif nilai >= 55:
        huruf = "C"
    elif nilai >= 40:
        huruf = "D"
    else:
        huruf = "E"

    if huruf in ("A", "B", "C"):
        keterangan = "LULUS"
    else:
        keterangan = "TIDAK LULUS"

    print(f"Nilai angka : {nilai}")
    print(f"Huruf mutu  : {huruf}")
    print(f"Keterangan  : {keterangan}")

print("-" * 50)
print("Terima kasih telah menggunakan program ini.")
print("=" * 50)




print("=" * 50)
print("Nama: Muhamad Ihsan Al Arabi")
print("NIM: 714260016")
print("Kelompok: DT09")
print("Kelas: D4 T1 1B")
print("=" * 50)

