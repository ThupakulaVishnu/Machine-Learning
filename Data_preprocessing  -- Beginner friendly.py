#---------------------------------------->Data preprocessing<-------------------------------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data=pd.read_csv(r"F:\ML\6_Udemy\Data Preprocessing\Data.csv")


qualitative=[i for i in data.describe()]
# print(qualitative)
from  sklearn.impute import SimpleImputer
asd=SimpleImputer(missing_values=np.NaN,strategy='mean')

# data["Age"]=asd.fit_transform(data[["Age"]])
# print(data.isna().sum())

# #Filling numetrical data by using mean
from  sklearn.impute import SimpleImputer
for i in qualitative:
    data[i]=asd.fit_transform(data[[i]])

#Filling the categorical data

aq=SimpleImputer(missing_values=np.nan,strategy="most_frequent")
data['Country']=aq.fit_transform(data[["Country"]]).ravel()#----------->
# print(data.isna().sum())
# print(data)

X=data.iloc[:,:-1].values
Y=data.iloc[:,-1].values


# from sklearn.compose import ColumnTransformer
# from sklearn.preprocessing import OneHotEncoder
# n=ColumnTransformer(transformers=[('encode',OneHotEncoder(),[0])],remainder='passthrough')

from sklearn.preprocessing import LabelEncoder
n=LabelEncoder()
X[:,0]=n.fit_transform(X[:,0])
Y=n.fit_transform(Y)
# print(Y)
# print(X)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=0)

# print(x_train)
# print("------------------------------------------")
# print(x_test)
# print("------------------------------------------")
# print(y_train)
# print("------------------------------------------")
# print(y_test)

from sklearn.preprocessing import StandardScaler,normalize
# x_train[:,1:]=normalize(x_train[:,1:])
# x_test[:,1:]=normalize(x_test[:,1:])

n=StandardScaler()
x_train[:,1:]=n.fit_transform(x_train[:,1:])
x_test[:,1:]=n.fit_transform(x_test[:,1:])

print(x_train)
print("------------------------------")
print(x_test)