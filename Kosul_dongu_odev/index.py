maas_Bilgisi = int(input("Lütfen maaş bilginizi giriniz: "))

if maas_Bilgisi <= 10000:
    oran = 5
elif maas_Bilgisi <= 25000:
    oran = 10
elif maas_Bilgisi <= 45000:
    oran = 25
else:
    oran = 30

vergi = maas_Bilgisi * oran / 100
yeni_maas = maas_Bilgisi - vergi

print("Uygulanan vergi oranı: %", oran)
print("Ödenecek vergi miktarı:", vergi)
print("Vergi sonrası maaşınız:", yeni_maas)


kullanıcı_adı = input("Lütfen kullanıcı adınızı giriniz: ")
sifre = int(input("Lütfen şifrenizi giriniz: "))

if len(sifre) == 6:
    print("Hesabınız oluşturuldu.")
elif len(sifre) < 6:
    print("Şifreniz çok kısa, lütfen en az 6 karakter giriniz.")
else:
    print("Şifreniz 6 karakterden uzun, yine de hesabınız oluşturuldu.")


kullanıcı_adı = input("Lütfen kullanıcı adınızı giriniz: ")

while True:

    sifre = input("Lütfen şifrenizi giriniz: ")

    if 5 <= len(sifre) <= 10:
        print("Hesabınız oluşturuldu.")
        break
    else:
        print("Lütfen girdiğiniz şifre 5 haneden az, 10 haneden fazla olmasın!")

kullanıcı_adı = input("Lütfen kullanıcı adınızı giriniz: ")
dogru_sifre ="123456"
hak =3

while hak > 0:
    sifre = input("Lütfen şifrenizi giriniz: ")
    if sifre == dogru_sifre:
        print("Hesabınıza giriş yaptınız.")
        break
    else:
        hak -= 1
        if hak > 0:
            print("Hatalı şifre girdiniz. Kalan hakkınız:", hak)
        else:
            print("3 kez hatalı şifre girdiniz.")
    