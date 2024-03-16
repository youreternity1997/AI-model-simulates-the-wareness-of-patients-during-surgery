import pandas as pd
import os

csv_path = os.path.join("C:\\Users\\carl\\Desktop\\20141218661003change.csv")
consciousness= pd.read_csv(csv_path)
print(consciousness)

print("============================================")

#consciousness.drop("Time", axis=1) 沒有功用
del consciousness ['Time']
del consciousness ['HR']
del consciousness ['SPO2']
del consciousness ['NBP_Dia']
del consciousness ['NBP_Sys']
del consciousness ['NBP_Mean']
del consciousness ['BIS']
#del consciousness ['EMG']
del consciousness ['Doctor']
del consciousness ['SQI']
print(consciousness)

print('---------------------1')

print('---------------------2')

print("---------------------3")

print('---------------------4')

consciousness = consciousness.set_index('Pulse')
print(consciousness)

print('---------------------5')
sample_incomplete_rows = consciousness[consciousness.isnull().any(axis=1)].head()
print(sample_incomplete_rows)


#consciousness_interp = consciousness.interpolate(method ='pad',limit = None,inplace = True)
print(consciousness_interp)











"""
#consciousness.drop("Time", axis=1) 沒有功用
del consciousness ['Time']
del consciousness ['HR']
del consciousness ['SPO2']
del consciousness ['NBP_Dia']
del consciousness ['NBP_Sys']
del consciousness ['NBP_Mean']
del consciousness ['BIS']
#del consciousness ['EMG']
del consciousness ['Doctor']
del consciousness ['SQI']
print(consciousness)

#print(consciousness.loc[:,'HR'][0:9])
#print(consciousness[consciousness.isnull().any(axis=1)].loc[:,'HR'])
#consciousness_HR0to9isnotNAN = consciousness.fillna(method='bfill', inplace=True)

print('---------------------1')

#print(consciousness[consciousness.loc[:,'HR'].isnull()])
#print(consciousness[consciousness.loc[:,'EMG'].isnull()])
#print(consciousness[consciousness.loc[:,'BIS'].isnull()].head(2120))

print('---------------------2')

conscious_average_HR0to9= consciousness.loc[10:20,'HR'].mean()
print("mean(HR[10:20])= ",conscious_average_HR0to9)
conscious_average_HR93to103 = consciousness.loc[93:103,'HR'].mean()
conscious_average_HR129to139 = consciousness.loc[129:139,'HR'].mean()
conscious_average_HR103to128 = (conscious_average_HR93to103 + conscious_average_HR129to139)/2
#print("mean((HR[93:103]+HR[129:139])/2)= ", conscious_average_HR103to128)

#conscious_average_EMG0to27= consciousness.loc[28:38,'EMG'].mean()
#print("mean(EMG[28:38])= ",conscious_average_EMG0to27)

print("---------------------3")
#consciousness_HR0to9isnotNAN = [consciousness.loc[0:9,'HR']].fillna(method='bfill', inplace=True)
#print(consciousness_HR0to9isnotNAN)

#writer = csv.writer(open("C:\\Users\\carl\\Desktop\\20141218661003change.csv", 'w'))
#writer.writerows(consciousness)

consciousness.loc[0:9,'HR']=conscious_average_HR0to9
consciousness.loc[103:128,'HR']=conscious_average_HR103to128
#print(consciousness[consciousness.loc[:,'HR'].isnull()])

#consciousness.loc[0:27,'EMG']=conscious_average_EMG0to27
#print(consciousness[consciousness.loc[:,'EMG'].isnull()])


print('---------------------4')

"""