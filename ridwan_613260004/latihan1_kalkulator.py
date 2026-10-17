print("================================")
print("     KALKULATOR SEDERHANA       ")
print("================================")
print("operasi yang tersedia: +, -, *, /")

angka1 = float(input("masukan bilangan pertama: "))
angka2 = float(input("masukan bilangan kedua: "))
operator = input("masukan operasi:(+/-/*/) ")

print("================================")


if operator == "+":
    hasil = angka1 + angka2
    print(f"hasil dari {angka1} + {angka2} = {hasil}")

elif operator == "-":
    hasil = angka1 - angka2
    print(f"hasil dari {angka1} - {angka2} = {hasil}")  

elif operator == "*":
    hasil = angka1 * angka2
    print(f"hasil dari {angka1} * {angka2} = {hasil}")  

elif operator == "/":
    hasil = angka1 / angka2
    print(f"hasil dari {angka1} / {angka2} = {hasil}")

else:
    print(f"Operator {operator} tidak dikenali.")
    print("silahkan masukan operator yang tersedia: +, -, *, /")

print("================================")
print("terimakasih telah menggunakan kalkulator sederhana ini")