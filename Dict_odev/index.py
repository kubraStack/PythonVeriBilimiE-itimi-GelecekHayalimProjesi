ogrenci_bilgileri = {
    "Ayşe Yılmaz": {
        "ders": {
            "matematik":"85",
            "fizik":"90",
            "kimya":"78",
            
        }
    },
    "Mehmet Demir": {
        "ders": {
            "matematik":"92",
            "fizik":"81",
            "kimya":"85",
           
        }
    },
    "Elif Kaya": {
        "ders": {
            "matematik":"75",
            "fizik":"89",
            "kimya":"92",
            
        }
    }
    
}

# isim =input("Öğrenci ismini giriniz: ")
# ders = input("Notunu öğrenmek istediğiniz dersi giriniz: ")

# print(f"{isim} adlı öğrencinin {ders} dersinden aldığı not: {ogrenci_bilgileri[isim]['ders'][ders]}")

def bilgileri_goster():
    #Tüm bilgileri getirir
    print("--- Tüm Öğrenci Bilgileri ---")
    for ogrenci, bilgiler in ogrenci_bilgileri.items(): 
        print(f"Öğrenci Adı: {ogrenci}")
        if 'ders' in bilgiler:
            for ders, notu in bilgiler['ders'].items():
                print(f"  {ders}: {notu}")
    print("-"*30)

def bilgileri_sorgula():
    #Kullanıcının girdiği öğrenci ve ders bilgilerini sorgular
    isim =input("Öğrenci ismini giriniz: ")

    if isim in ogrenci_bilgileri:
        ders = input("Notunu öğrenmek istediğiniz dersi giriniz: ")
        if ders in ogrenci_bilgileri[isim]['ders']:
            print(f"{isim} adlı öğrencinin {ders} dersinden aldığı not: {ogrenci_bilgileri[isim]['ders'][ders]}")
        else:
            print(f"{isim} adlı öğrenci için {ders} dersi bulunamadı.")

def not_guncelle():
    #Var olan öğrencinin ders notunu günceller
    isim = input("Notunu güncellemek istediğiniz öğrencinin ismini giriniz: ")
    if isim in ogrenci_bilgileri:
        ders = input("Notunu güncellemek istediğiniz dersi giriniz: ").lower()

        if ders in ogrenci_bilgileri[isim]['ders']:
            yeni_not = input(f"{ders} dersinin yeni notunu giriniz: ")
            ogrenci_bilgileri[isim]['ders'][ders] = yeni_not
            print(f"{isim} adlı öğrencinin {ders} dersinin notu güncellendi: {yeni_not}")
        else:
            print(f"{isim} adlı öğrenci için {ders} dersi bulunamadı.")
    else:
        print(f"{isim} adlı öğrenci bulunamadı.")       


def ogrenci_ekle():
    #Yeni öğrenci ekler
    yeni_isim=input("Eklemek istediğiniz öğrencinin ismini giriniz: ")
    if yeni_isim in ogrenci_bilgileri:
        print(f"{yeni_isim} adlı öğrenci zaten mevcut.")
        return
    else:
        #yeni öğrenci için boş bir ders sözlüğü oluşturur
        ogrenci_bilgileri[yeni_isim] = {"ders": {}}
        while True:
            ders_adi=input("Eklemek istediğiniz dersin adını giriniz (bitirmek için 'q' tuşuna basın): ")
            if ders_adi.lower() == 'q':
                break

            ders_notu=input(f"{ders_adi.capitalize()} dersinin notunu giriniz: ")

            #yeni değer ekleme
            ogrenci_bilgileri[yeni_isim]['ders'][ders_adi] = ders_notu
        print(f"{yeni_isim} adlı öğrenci başarıyla eklendi.")

ogrenci_ekle()
not_guncelle()
bilgileri_sorgula()
bilgileri_goster()

