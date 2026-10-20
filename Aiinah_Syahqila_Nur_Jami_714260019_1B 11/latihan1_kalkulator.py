#latihan 1 -  kalkulator sederhana
#pelatihan dasar pemrograman MORRIS IF 26
#==================
print("=================================")
print("   KALKULATOR KONSOL SEDERHANA   ")
print("=================================")
print("operasi tersedia: + - * / ")
print("---------------------------------")

# --- pembagian masukan pengguna -----
angka1 = float(input("masukkan angka pertama: "))
angka2 = float(input("masukkan angka kedua: "))
operator = input("masukkan operator (+, -, *, /): ")

print("---------------------------------")

#------- bagian proses -------
if operator == "+":
    hasil = angka1 + angka2
    print(f"Hasil: {angka1} + {angka2} = {hasil:.2f}")

elif operator == "-":
    hasil = angka1 - angka2
    print(f"Hasil: {angka1} - {angka2} = {hasil:.2f}")
elif operator == "*":
    hasil = angka1 * angka2
    print(f"Hasil: {angka1} * {angka2} = {hasil:.2f}")

elif operator == "/":
    if angka2 == 0:
        print("kesalahan: bilangan tidak dapat dibagi nol.")
    
    else:
        hasil = angka1 / angka2
        print(f"Hasil: {angka1} / {angka2} = {hasil:.2f}")

else:
    print(f"operator'{operator}' tidak dikenali.")
    print("gunakan salah satu dari: = - * / ")

print("================================================")
print("terimakasih telah menggunakan kalkulator ini.")