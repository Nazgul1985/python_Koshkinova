import numpy as np
def sum_rows(arr):
    rows_sum = np.sum(arr, axis=1)
    return rows_sum


arr1=np.random.randint(1,10, size=(3,3))
arr2=np.random.randint(1,10, size=(3,3))

result=np.multiply(arr1,arr2)
print (f"Array1: {arr1}")
print (f"Array2: {arr2}")

sum_rows1=sum_rows(arr1)
sum_rows2=sum_rows(arr2)
print (f"\n result {result}")
print (f"Summ1 {sum_rows1}")
print (f"Summ2 {sum_rows2}")