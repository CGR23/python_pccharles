# Exemple de data frame
import pandas as pd
data = {"state": ["Ohio", "Ohio", "Ohio",
"Nevada", "Nevada"],
"year": [2000, 2001, 2002, 2001, 2002],
"pop": [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = pd.DataFrame(data)
# ordre des colonnes
test = pd.DataFrame(data, columns=["year", "state", "pop"])
print ( test)
# index des lignes et valeurs manquantes (NaN)
frame2=pd.DataFrame(data, columns=["year", "state", "pop", "debt"],index=["one", "two", "three", "four", "five"])

print(frame2)
print(frame2.describe())
print(frame2.dtypes)
# liste des colonnes
frame.columns
# valeurs d’une colonnes
frame["state"]
frame.year
# "imputation"
frame2["debt"] = 16.5
frame2
# créer une variable
frame2["eastern"] = frame2.state == "Ohio"
frame2
# Trafic de données avec Python-pandas
# supprimer une variable
del frame2[u"eastern"]
frame2.columns

