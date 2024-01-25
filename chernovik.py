import numpy as np

data = np.random.randint(0,100,100)
srednee= np.mean(data)
print (srednee)

mediana = np.median(data)
print (mediana)

otkl = np.std(data)
print(otkl)