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













