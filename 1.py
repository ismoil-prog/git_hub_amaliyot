""" “raqamlar” nomli tekst fayl ichiga 1 dan 10 gacha 
sonlarni kiritib, ularning yig'indisini ekranga 
chiqaruvchi dastur yarating."""
with open("raqamlar.txt", "w+") as f:
    sum = 0
    for x in range(1, 10 + 1):
        f.write(str(x) + ' ')
    print("Faylga 1-10 gacha bo'lgan sonlar yozildi")
    f.seek(0)
    res = f.read()
    numbers = res.split()
    for number in numbers:
        sum += int(number)
    print("Result =",sum)
