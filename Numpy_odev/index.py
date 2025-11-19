import numpy as np


# sayilar = np.array([3,8,9,24,75,34], dtype="int")

# ndim → dizinin kaç boyutlu olduğunu söyler.
# print(sayilar.ndim)
# size → toplam eleman sayısı. 
# print(sayilar.size)
# shape → dizinin şekli. 
# print(sayi.shape)

# arr1 = np.array([[1,2,6,7], [4,3,9,5]])
# arr2 = np.array([[[7,5,14], [21,8,11], [8,6,20], [14,3,9]]])

# boyut = arr1.ndim
# eleman = arr1.size
# satir1, sutun1 = arr1.shape
# print(f"Arr2 array'i {boyut} boyutlu ve  {eleman} elemanlıdır.{satir1} satırlı ve {sutun1} sütunludur.")

# boyut2 = arr2.ndim
# eleman2 = arr2.size
# derinlik, satir2, sutun2 = arr2.shape
# print(f"Arr3 array'i {boyut2} boyutlu ve  {eleman2} elemanlıdır.{derinlik} Derinliktedir ,{satir2} satırlıdır ve {sutun2} sütunludur.")

##### 3. İstenilen elamanlara ulaşmak için arrayler üzerinde indexleme işlemi yapalım
# eleman1 = arr1[0,1]
# print(eleman1)


# eleman2 = arr1[0,-1]
# print(eleman2)

# eleman3 = arr2[0,3,2]
# print(eleman3)

# eleman4 = arr2[0,0,1]
# print(eleman4)


# arr1 = np.array([[1,2,6,7], [4,3,9,5]])
# arr2 = np.array([[[7,5,14], [21,8,11], [8,6,20], [14,3,9]]])

# new_arr = arr1[0:1]
# new_arr2 = arr1[1:2]

# new_arr3 = arr2[0:1,1]
# new_arr4 = arr2[0:2,2]
# print(new_arr4)

##### 5. 5 satır 3 sütunluk sıfırlardan ve birlerden oluşan iki tane iki boyutlu array oluşturalım. Bu arrayleri satır ve sütun bazında birleştirelim.

arr_zero = np.zeros((5,3), dtype=int)
arr_one = np.ones((5,3),dtype=int)

print("Sıfırlar: ", arr_zero)
print("Birler: ", arr_one)

birlesik_satirlar = np.concatenate((arr_zero, arr_one), axis=0)
print("Satır bazında birleşim: ")
print(birlesik_satirlar)

birlesil_sütunlar = np.concatenate((arr_zero,arr_one), axis=1)
print("Sütun bazunda birleşim: ")
print(birlesil_sütunlar)