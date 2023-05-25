import numpy as np
import pandas as pd
from scipy import stats
from sklearn.preprocessing import LabelEncoder

data=pd.read_csv('citydata1.csv')
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.ensemble import RandomForestRegressor

# Create a Random Forest regressor instance
rf = RandomForestRegressor(n_estimators=100, random_state=42)

# Create an iterative imputer instance with the Random Forest regressor
imputer = IterativeImputer(random_state=42, estimator=rf)
data['PM2.5'] = imputer.fit_transform(data[['PM2.5']])
data['PM10'] = imputer.fit_transform(data[['PM10']])
data['NO'] = imputer.fit_transform(data[['NO']])
data['NO2'] = imputer.fit_transform(data[['NO2']])
data['NOx'] = imputer.fit_transform(data[['NOx']])
data['NH3'] = imputer.fit_transform(data[['NH3']])
data['CO'] = imputer.fit_transform(data[['CO']])
data['SO2'] = imputer.fit_transform(data[['SO2']])
data['O3'] = imputer.fit_transform(data[['O3']])
data['Benzene'] = imputer.fit_transform(data[['Benzene']])
data['Toluene'] = imputer.fit_transform(data[['Toluene']])
data['Xylene'] = imputer.fit_transform(data[['Xylene']])

le=LabelEncoder()

data['City']=le.fit_transform(data['City'])
idx=~data['AQI_Bucket'].isna()
data.loc[idx,'AQI_Bucket']=le.fit_transform(data.loc[idx,'AQI_Bucket'])
#data['AQI_Bucket']=le.fit_transform(data~data['AQI_Bucket'].isnull())
data['State']=le.fit_transform(data['State'])
data['Zone']=le.fit_transform(data['Zone'])

data1= data.drop('Xylene',axis=1)

from sklearn.preprocessing import MinMaxScaler
data2=data1.filter(['PM2.5','PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3','Benzene','Toluene','AQI'])
#scale features
scaler = MinMaxScaler()
model=scaler.fit(data2[['PM2.5','PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3','Benzene','Toluene']])
normalized_data=model.transform(data2[['PM2.5','PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3','Benzene','Toluene']])

from sklearn.model_selection import train_test_split

# Separate rows with null target values into a separate dataframe
validation_data = data2[data2['AQI'].isnull()]
x_val = validation_data.drop(['AQI'],axis=1)

# Separate rows with non-null target values into a training/testing dataframe
train_test_data = data2[~data2['AQI'].isnull()]

#Independent and dependent variables
x = train_test_data.drop(['AQI'], axis=1)
y = train_test_data['AQI']

#Train Test data
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=.25,random_state=42)

from sklearn.ensemble import RandomForestRegressor
rf_rgr=RandomForestRegressor(n_estimators=100,random_state=42)
rf_rgr.fit(x_train,y_train)
y_pred_rf=rf_rgr.predict(x_test)

#Validation Set:
from sklearn.ensemble import RandomForestRegressor
rf_rgr=RandomForestRegressor(n_estimators=100,random_state=42)
rf_rgr.fit(x_train,y_train)


y_val_pred_rf=rf_rgr.predict(x_val)
data1.loc[data1['AQI'].isna(),'AQI']=y_val_pred_rf


import pickle
pickle.dump(rf_rgr,open('model.pkl','wb'))

