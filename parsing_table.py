import pandas as pd

df = pd.read_excel('TABELA PREDITIVA-v3.xlsx', index_col='PRODUCTION')

print(df)
# usar df.loc['PROUÇÃO', 'SIMBOLO'] 
res = df.loc['PROC', 'int']
print(type(res))
# separa por espaço 
sep = res.split()
print(sep)
# remove os 2 primeiros elementos 
del(sep[0:2])
print(sep)
# inverte a lista
inverted = [el for el in reversed(sep)]
print(inverted)


