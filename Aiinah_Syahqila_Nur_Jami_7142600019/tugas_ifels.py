#==========================================
# Nama : Aiinnah Syahqila Nur Jami
# NIM  : 7142600019
# kelas: 1B
#==========================================


print("=======================================")
print("   KONVERSI NILAI ANGKA KE HURUF MUTU  ")
print("=======================================")

nilai = float(input("Masukkan nilai akhir (0-100): "))

print("----------------------------------")
if nilai < 0:
    print("nilai tidak dapat angka minus")
elif nilai > 100:
    print("nilai tidak boleh lebih dari 100")
elif nilai >= 80:
    huruf = "A"
    print(f"Nilai {nilai} setara dengan huruf mutu {huruf}")
elif nilai >= 70:
    huruf = "B"
    print(f"Nilai {nilai} setara dengan huruf mutu {huruf}")
elif nilai >= 60:
    huruf = "C"
    print(f"Nilai {nilai} setara dengan huruf mutu {huruf}")
elif nilai >= 50:
    huruf = "D"
    print(f"Nilai {nilai} setara dengan huruf mutu {huruf}")
else:
    huruf = "E"
    print(f"Nilai {nilai} setara dengan huruf mutu {huruf}")
print("====================================")
print("TERIMAKASIH TELAH MENGGUNAKAN PROGRAM INI")
print("=======================================")