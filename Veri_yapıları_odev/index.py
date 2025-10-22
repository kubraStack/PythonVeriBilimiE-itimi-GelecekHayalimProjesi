x = 3
x = float(x)
print(type(x))


y = 4.5
y = int(y)
print(type(y))

z = "8"
z = int(z)
print(type(z))

a = "12"
a = float(a)
print(type(a))

b = "46.8"
b = int(float(b))
print(type(b))

defne = 12
ali = 26
aleyna = 21

print(defne != ali)      # True
print(ali > aleyna)      # True
print(defne < aleyna)    # True
print(aleyna < ali)      # True
print(ali == defne)      # False

print(ali > 18 and aleyna < 25)          # True
print(defne < 18 or defne > 15)          # True
print(not(ali == defne and aleyna < defne))  # True

Kullanıcıdan iki değer al
sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))

toplam = sayi1 + sayi2
cikarma = sayi1 - sayi2
carpim = sayi1 * sayi2
bölme = sayi1 / sayi2

print("Toplam:", toplam)
print("Çıkarma:", cikarma)
print("Çarpım:", carpim)    
print("Bölme:", bölme)

Kullanıcıdan bilgilerini al
isim = str(input("İsminizi giriniz: "))
yas = int(input("Yaşınızı giriniz: "))
sehir = str(input("Şehrinizi giriniz: "))
meslek = str(input("Mesleğinizi giriniz: "))

print("İsim:", isim, ", Yaş:", yas, ", Şehir:", sehir, ", Meslek:", meslek)


kurs = "Hi-Kod Veri Bilimi Atölyesi"
print(kurs.split())    # Kelimelere ayırır
print(kurs.upper())      # Tüm harfleri küçük yapar
print(kurs.lower())      # Tüm harfleri büyük yapar

i ="0123456789"
print(i[0:10:2]) #başlangıç:bitiş:adım
print(i[1:10:2])
