import numpy as np
from random import randint


n, m = 4, 5
array = [[randint(1, 10) for j in range(m)] for i in range(n)]
print("Массив с рандомными значениями")
for i in array:
    print(i)
print()
a = np.amax(array)
print("Максимальное значение массива: ", a)

number = 0
for i in array:
    for j in i:
        if j == a:
            number+=1
print("Количество максимальных элементов в массиве: ", number)

print("Умножаем элементы массива на количество максимальных элементов: ")
for i in array:
    for j in i:
        print(j * number,',',end=' ')
    print()



