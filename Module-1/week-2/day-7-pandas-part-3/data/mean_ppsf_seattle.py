import pandas as pd
sales_df = pd.read_csv('EXTR_RPSale.csv')
bldg_df = pd.read_csv('EXTR_ResBldg.csv')
sales_df = sales_df[['Major', 'Minor', 'DocumentDate', 'SalePrice']]
bldg_df = bldg_df[['Major', 'Minor', 'SqFtTotLiving', 'ZipCode']]
sales_df['Major'] = pd.to_numeric(sales_df['Major'], errors='coerce')
sales_df['Minor'] = pd.to_numeric(sales_df['Minor'], errors='coerce')
sales_data = pd.merge(sales_df, bldg_df, on=['Major', 'Minor'])
sales_data = sales_data.loc[~sales_data['ZipCode'].isna(), :]
sales_data = sales_data.loc[sales_data['SalePrice'] > 0]
sales_data = sales_data.loc[sales_data['SqFtTotLiving'] > 50]
sales_data['ZipCode'] = sales_data.ZipCode.map(lambda x: str(x)[:5])
sales_data['ZipCode'] = pd.to_numeric(sales_data['ZipCode'], errors = 'coerce')
sales_data['PricePerSqFt'] = sales_data['SalePrice']/sales_data['SqFtTotLiving']
data2019 = sales_data.loc[sales_data.DocumentDate.str[-4:] == '2019']
data2019['ZipCode'] = pd.to_numeric(data2019['ZipCode'])
SeattleZipCodes = [8101, 98102, 98103, 98104, 98105, 98106, 98107, 98108, 98109, 98112, 98115, 98116, 98117, 98118, 98119, 98121, 98122, 98125, 98126, 98133, 98134, 98136, 98144, 98146, 98154, 98164, 98174, 98177, 98178, 98195, 98199]
seattle2019 = data2019.loc[data2019['ZipCode'].isin(SeattleZipCodes)]
print(seattle2019['PricePerSqFt'].mean())