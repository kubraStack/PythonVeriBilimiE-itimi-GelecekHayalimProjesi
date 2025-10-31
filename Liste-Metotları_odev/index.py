# Odev 1

# liste = ["Python",True,9,"3",8.4,"Hi-Kod","False",4.7]
# print(liste[3])  # 3. indexteki elemanı yazdırır
# print(liste[5]) # 5. indexteki elemanı yazdırır
# print(liste[-1]) # Listenin son elemanını yazdırır

# new_list = liste[2:6]
# print(new_list)  # 2. indexten başlayarak 6. indexe kadar olan elemanları yazdırır (6. index dahil değil)

# new_list2 = liste[4:]
# print(new_list2)  # 4. indexten başlayarak sondan 2. indexe kadar olan elemanları yazdırır (sondan 2. index dahil değil)

# Odev 2
# liste = ["Python",True,9,"3",8.4,"Hi-Kod","False",4.7]
# new_list = []
# for i in liste :
#     if type(i) == str :
#         new_list.append(i)
#         print(new_list)  # Sadece string elemanları içeren yeni listeyi yazdırır

# Odev 3
# for index in range(len(meyveler)):

#     print("{}. indexte bulunan meyve: {}".format(index,meyveler[index]))

# enumerate() Python’da çok kullanılan, özellikle döngülerde hem index (sıra numarası) hem de değer (eleman) almak istediğimizde işimizi kolaylaştıran bir yerleşik (built-in) fonksiyondur.
# meyveler = ["elma","armut","muz","çilek","karpuz"]
# for index, meyve in enumerate(meyveler):
#     print("{}. indexte bulunan meyve: {}".format(index,meyve))