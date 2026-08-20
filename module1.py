#Load transactions.csv and customers.csv into Pandas. Display shape and first 5 rows.

import pandas as pd
df = pd.read_csv("customers.csv");
print(df.head(5))

df1 = pd.read_csv("transactions.csv")
print(df1.head(5))


#Identify missing values in transactions. Report columns and counts.

print(df1.isnull().sum())


print("successfully completed")









