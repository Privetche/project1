import quandl
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
quandl.ApiConfig.api_key = "9_ciVQbbNhsx4zfAmsmy"
btcprice = quandl.get("BCHAIN/MKPRU", start_date="2009-12-31", end_date="2018-11-04", returns="numpy")
btccap = quandl.get("BCHAIN/MKTCP", start_date="2009-12-31", end_date="2018-11-04", returns="numpy")
btcvolume = quandl.get("BCHAIN/ETRVU", start_date="2009-12-31", end_date="2018-11-04", returns="numpy")
df1=pd.DataFrame(btcvolume)
df1['price'] = pd.DataFrame(btcprice)['Value']
df1['cap'] = pd.DataFrame(btccap)['Value']
df1['NVT'] = df1['cap']/df1['Value']
df1['NVT_fast'] = df1['NVT'].ewm(span=5, adjust=False).mean()
df1['NVT_slow'] = df1['NVT'].ewm(span=15, adjust=False).mean()
print(df1.tail(10))
df1.plot(x='Date', y='NVT_fast', kind='line')
writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
df1.to_excel(writer, 'Sheet1')
writer.save()