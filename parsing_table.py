import pandas as pd

df = pd.read_excel('TABELA PREDITIVA-v3.xlsx', index_col='PRODUCTION')

print(df)

print(df.columns)

# usar df.loc['PROUÇÃO', 'SIMBOLO'] 
res = df.loc['ID_TYPE_ARITH', '0']
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


