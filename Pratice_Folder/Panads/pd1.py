import pandas as pd
import numpy as np

# Create a sample DataFrame
df = pd.read_csv(r"C:\Users\Pramod\OneDrive\AI Python\Senapati Sir\Class Document\Pratice_Folder\Panads\CSV_DataSet.csv")
#print(df)

#check get the head values 
#print(df.head())


print("=====print the the column names=====")

print(df.columns)
print(len(df.columns))

print("=====print the the column names=====")
print(df['destination'])
print(df.head(1))

print("=====print 2 column names=====")

col2=df[['destination','temperature']]
print(col2)

print('====SELECT*FROM dataset_1 LIMIT 10====')
limit_10=df['destination'].head(10)
print(limit_10)
#print(df)

print('===select distinct destination from dataset_1====')
dist1=df['passanger'].unique()
print(dist1)

print("====== SELECT * FROM dataset_1 WHERE destination = 'Home'====")

where_home=df[df['destination']=="Home"]
print(where_home)

print("=====SELECT *FROM dataset_1 ORDER BY coupon==")
orderby_coupn=df.sort_values(by=['coupon', 'destination'],ascending=[True,False])
print(orderby_coupn)


print("========SELECT destination as Destination FROM dataset_1=======")

col_rename_alias=df.rename(columns={'destination':'Destination'},inplace=False)
print(col_rename_alias)
print('\n')
print("===========SELECT occupation FROM dataset_1 GROUP BY occupation====")

group_by=df.groupby('occupation').size().to_frame('Count').reset_index()
print(group_by)
print('\n')

print("==================SELECT weather ,AVG(temperature) as avg_temp FROM dataset_1 GROUP BY weather===")

group_by_avg=df.groupby('weather')['temperature'].mean().to_frame('avg_count').reset_index()
print(group_by_avg)
print('\n')

print("=========SELECT weather ,COUNT( temperature) AS count_temp FROM dataset_1 GROUP BY weather====")
group_Count_temp=df.groupby('weather')['temperature'].size().to_frame('Count_Temp').reset_index()
print(group_Count_temp)

print("======SELECT weather ,COUNT(DISTINCT temperature) AS count_distinct_temp FROM dataset_1 GROUP BY==")

print('\n')
group_count_distinct_temp=df.groupby('weather')['temperature'].nunique().to_frame('temp_dist').reset_index()
print(group_count_distinct_temp)
print('\n')

print("====SELECT weather ,SUM(temperature) AS sum_temp FROM dataset_1 GROUP BY weather===")

group_sum=df.groupby('weather')['temperature'].sum().to_frame('sum_temp').reset_index()
print(group_sum)
print('\n')

print("=====SELECT weather ,MIN(temperature) AS min_temp FROM dataset_1 GROUP BY weather===")
group_max=df.groupby('weather')['temperature'].max().to_frame('max_temp').reset_index()

group_min=df.groupby('weather')['temperature'].min().to_frame('min_temp').reset_index()
print(group_min)
print('\n')
print(group_max)
print('\n')

print("=====SELECT occupation FROM dataset_1 GROUP BY occupation HAVING occupation='Student===")

having_df=df.groupby('occupation').filter(lambda x:x['occupation'].iloc[0]=='Student').groupby('occupation').size()
print(having_df)
print('\n')

print("====SELECT DISTINCT destination FROM(SELECT * FROM dataset_1 UNION SELECT * FROM table_to_union)==")

dict_sub_qury=pd.concat([df,df1])['destination'].drop_duplicates()
print(dict_sub_qury)
print('\n')
