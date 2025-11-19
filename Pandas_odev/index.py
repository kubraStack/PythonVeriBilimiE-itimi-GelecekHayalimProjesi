import pandas as pd

sozluk = {"Kategori": ["Giyim","Giyim", "Ayakkabı","Aksesuar","Ayakkabı","Giyim","Aksesuar","Aksesuar","Ayakkabı","Giyim"],
         "Ürün" : ["Kazak","T-shirt","Sandalet","Küpe","Spor Ayakkabı","Pantolon","Kolye","Yüzük","Çizme","Ceket"],
         "Fiyat" : [300,180,450,50,700,400,150,80,850,900]}

new_sozluk = pd.DataFrame(sozluk)
# print(new_sozluk)

# category_giyim = new_sozluk[new_sozluk["Kategori"]=="Giyim"]
# category_ayakkabi = new_sozluk[new_sozluk["Kategori"] =="Ayakkabı"]
# category_aksesuar = new_sozluk[new_sozluk["Kategori"] =="Aksesuar"]

##### 3 Aşağıdaki işlemleri dataframe üzerinde uygulayalım.
# - Giyim kategorisinde fiyatı 300'den fazla olan ürünleri gösterin
# - Ayakkabı kategorisinde fiyatı 600'den az olan ürünleri gösterin
# - Aksesuar kategorisinde fiyatı 100'den fazla olan aksesuarı gösterin
# giyim = new_sozluk[(new_sozluk["Kategori"] == "Giyim") & (new_sozluk["Fiyat"] > 300)]
# ayakkabi = new_sozluk[(new_sozluk["Kategori"] =="Ayakkabı") & (new_sozluk["Fiyat"] > 600)]
# aksesuar = new_sozluk[(new_sozluk["Kategori"]=="Aksesuar") & (new_sozluk["Fiyat"] > 100)]
# print(aksesuar)