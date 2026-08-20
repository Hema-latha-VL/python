#Load transactions.csv and customers.csv into Pandas. Display shape and first 5 rows.

import pandas as pd
df = pd.read_csv("customers.csv");
print(df.head(5))

df1 = pd.read_csv("transactions.csv")
print(df1.head(5))


#Identify missing values in transactions. Report columns and counts.

print(df1.isnull().sum())


# checking the value is valid or not
df1['amount_status'] = df1['amount'].apply(lambda x: 'Valid' if x > 0 else 'Flagged')

flagged_rows = df1[df1['amount'] <= 0]

if flagged_rows.empty:
    print("All transaction amounts are positive! No issues found.")
else:
    print(flagged_rows[['transaction_id', 'customer_id', 'amount']])


# Aggregate transactions by date (date, total_amount, transaction_count). Sort by date.
df1['date'] = pd.to_datetime(df1['date'])

summary = df1.groupby('date').agg(
    total_amount=('amount', 'sum'),
    transaction_count=('transaction_id', 'count')
).reset_index()

# Sorting the results 
summary = summary.sort_values(by='date')

print("--- Daily Transaction Summary ---")
print(summary)


print("the summary was successfully generated")

summary.to_csv("daily_sales_summary.csv", index=False)
print("developer 1 code ")

print("developer 2 change")








