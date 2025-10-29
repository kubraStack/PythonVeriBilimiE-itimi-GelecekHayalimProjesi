#Odev1
#Kullanıcıdan pi değeri ve yarıçap bilgisi alıp dairenin alanı hesaplanır

# def alan_hesapla(pi, yaripcap):
#     alan = pi * (yaripcap ** 2)
#     print(f"Girilen pi değeri: {pi} ve girilen yarıçap değeri:{yaripcap} olan dairenin alanı: {alan} ")


# alan_hesapla(5.4, 7)


#Odev2
#Faktöriyel adında fonksiyon oluşurulup, döngü kullanılarak parametre olarak girilen sayının faktöriyeli hesaplanır.
#Format metodun kullanılarak ekrana yazdırılır.
# def faktöriyel(sayi):
#     sonuc = 1
#     for i in range(1, sayi +1):
#         sonuc *= i
#     print("Girilen sayının faktöriyeli: {}".format(sonuc))

# faktöriyel(5)


#Odev3
#Kişinin fonksiyona doğum yılını vererek kaç yaşında olduğunu hesaplayan bir fonksiyon oluştur.

def yas_hesapla(dogum_yili):
    import datetime  # datetime modülünü içe aktarır mevcut yıl bilgisini almak için
    simdiki_yil = datetime.datetime.now().year
    yas = simdiki_yil - dogum_yili
    # print(f"Doğum yılı {dogum_yili} olan kişinin yaşı: {yas}")
    return yas

# yas_hesapla(1997)

# Doğum yılı ve isim bilgisi verilen fonksiyon kişinin emekli olup olmadığını söylesin.
# (Kişi 65 yaşında ise emekli olur.) 
# Burada yaş hesabını yukarıdaki örnekteki fonksiyonu kullanarak yapsın.(Yani fonksiyon içinde fonksiyon kullanmanızı istiyorum :))
# Kişi 65 yaşında ya da daha fazlaysa "Emekli oldunuz" yanıtını, 65 yaşından küçükse emekliliğine kaç yıl kaldığını da hesaplayarak "(isim) emekliliğine (yıl) kaldı." yanıtını versin.


def emeklilik_hesapla(dogum_yili, isim):
   
    yas = yas_hesapla(dogum_yili)

    if yas >= 65:
        print("Emekli oldunuz")
    else:
        kalan_yil = 65 - yas
        print(f"{isim} emekliliğine {kalan_yil} yıl kaldı.")

emeklilik_hesapla(1960, "Ahmet")