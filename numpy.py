# Numpy = Numerical Python
# Bilimsel hesaplamalar için kullanılır.

import numpy as np
list1 = [1, 2, 3]
list2 = [16, 25, 36]

arr1 = np.array(list1)
arr2 = np.array(list2)

np.array([1, 2, 3, 4, 5]) #Bir listeden array oluşturabiliriz.
type(arr1)

np.zeros(3, dtype=int) # Sıfırlardan oluşan bir array oluşturmak için kullanılır.
np.random.randint(0,99, size=5) # andom sayı seçmek için kullanılır.
np.random.normal(10, 1, 5) # ortalaması 10, standart sapması 1, 5 elemanlı bir array oluştur.

# Array özellikleri
# ndim: boyut sayısı
# shape: boyut bilgisi, biçim
# size: toplam eleman sayısı
# dtype: array veri tipini verir.

a = np.random.randint(55, size = 4)
a.ndim
a.shape
a.size
a.dtype

# Array reshaping
np.random.randint(1, 99, size = 9),
np.random.randint(1, 99, size = 9).reshape(3, 3)

# Index seçimi
array1 = np.random.randint(100, size = 7)
array1[0]
array1[0:5]

array2 = np.random.randint(100, size = (3, 5))
print(array2)
array2[2, 0]
array2[0, 2]
array2[1, 1] = 999

array2[0:2, 1:3]

# Fancy index
v = np.arange(0, 30, 3)
catch = [2, 4, 5]

v[catch]

# Numpy'da koşullu işlemler
v < 20 # array'deki elemanlar 20'den küçük mü sorgusunu yapar
v[v < 20]  # array'de 20'den küçük elemanları alır
v[v != 18] # array'de 18'e eşit olmayan elemanları alır.

# Matematiksel işlemler

v / 5
v ** 2
v - 1.2

np.subtract(v, 10)
np.add(v, 10)
np.mean(v)
np.sum(v)
np.min(v)
np.max(v)
np.var(v)

# np.linalg.solve(a, b) iki bilinmeyenli denklemleri çözmek için kullanılır.













