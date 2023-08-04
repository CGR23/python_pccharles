
import pandas as pd
# tables
df1 = pd.DataFrame({"key": ["b", "b", "a", "c","a","a", "b"],"data1": range(7)})
df2 = pd.DataFrame({"key": ["a", "b", "d"],"data2": range(3)})
print(df1)
print(df2)
print(pd.merge(df1,df2,on="key"))

# valeurs manquantes
print(pd.merge(df1,df2,on="key", how="outer"))

# tables
df1 = pd.DataFrame({"key": ["b", "b", "a", "c","a", "a", "b"],"var": range(7)})
df2 = pd.DataFrame({"key": ["a", "b", "d"],"var": range(3)})
# concaténation verticales
print(pd.concat([df1,df2],axis=0))
# concaténation horizontale
print(pd.concat([df1,df2],axis=1))