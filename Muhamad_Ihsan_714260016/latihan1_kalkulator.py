print("==========================")
print("KALKULATOR KOSOL SEDERHANA")
print("==========================")
print("Operasi Tersedia: + - * /")
print("--------------------------")

angka1 = float(input("Masukkan Bilangan Pertama: "))
angka2 = float(input("Masukkan Bilangan Kedua  : "))
operator =input("Masukkan operator(+ - * /): ")

print("....................................")

if operator == "+":
    hasil = angka1 + angka2
    print(f"hasil:{angka1}+{angka2} = {hasil:.2f}")

elif operator == "-":
    hasil = angka1 - angka2
    print(f"hasil:{angka1}-{angka2} = {hasil:.2f}")

elif operator == "*":
    hasil = angka1 * angka2
    print(f"hasil:{angka1}x{angka2} = {hasil:.2f}")

elif operator == "/":
    if angka2 == 0:
        print("Kesalahan: bilangan tidak dapat dibagi dengan nol.")
    else:
        hasil = angka1 / angka2
        print(f"hasil:{angka1}:{angka2} = {hasil:.2f}")

else:
    print(f"operator '{operator}' tidak dikenali.")
    print("Gunakan salah satu dari: + - * /")

print("====================================")
print("Terimakasih telah menggunakan kalkulator ini.")

