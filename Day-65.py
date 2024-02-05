# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 08:35:57 2024

@author: Nishant
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import seaborn as sns
from sklearn.tree import DecisionTreeRegressor 
from sklearn.preprocessing import LabelEncoder
#C:/Decision Tree/credit.csv
data=pd.read_csv("C:/Decision Tree/credit.csv")
data.isnull().sum()
data.dropna()
data.info()
data=data.drop(['phone'],axis=1)

#Conconverting into Binary
lb=LabelEncoder()
data['checking_balance']=lb.fit_transform(data['checking_balance'])
data['credit_history']=lb.fit_transform(data['credit_history'])
data['purpose']=lb.fit_transform(data['purpose'])
data['other_credit']=lb.fit_transform(data['other_credit'])
data['housing']=lb.fit_transform(data['housing'])
data['savings_balance']=lb.fit_transform(data['savings_balance'])
data['employment_duration']=lb.fit_transform(data['employment_duration'])
data['job']=lb.fit_transform(data['job'])

#below 3 lines very imp used in every model
data['default'].unique()
data['default'].value_counts
colnames=list(data.columns)

predictors=colnames[:15]
target=colnames[15]

from sklearn.model_selection import train_test_split
#train the data
train,test= train_test_split(data,test_size=0.3)

from sklearn.tree import DecisionTreeClassifier as DT 

model=DT(criterion='entropy')
model.fit(train[predictors],train[target])
preds=model.predict(test[predictors])
preds

pd.crosstab(test[target],preds,rownames=['Actual'],colnames=['Predicted'])
np.mean(preds==test[target])

#########################################################################
#DT

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import seaborn as sns
from sklearn.tree import DecisionTreeRegressor 
from sklearn.preprocessing import LabelEncoder
#C:/Decision Tree/credit.csv
data=pd.read_csv("C:/Decision Tree/credit.csv")
data.isnull().sum()
data.dropna()
data.info()
data=data.drop(['phone'],axis=1)

#Conconverting into Binary
lb=LabelEncoder()
data['checking_balance']=lb.fit_transform(data['checking_balance'])
data['credit_history']=lb.fit_transform(data['credit_history'])
data['purpose']=lb.fit_transform(data['purpose'])
data['other_credit']=lb.fit_transform(data['other_credit'])
data['housing']=lb.fit_transform(data['housing'])
data['savings_balance']=lb.fit_transform(data['savings_balance'])
data['employment_duration']=lb.fit_transform(data['employment_duration'])
data['job']=lb.fit_transform(data['job'])

#below 3 lines very imp used in every model
data['default'].unique()
data['default'].value_counts
colnames=list(data.columns)

predictors=colnames[:15]
target=colnames[15]

from sklearn.model_selection import train_test_split
#train the data
train,test= train_test_split(data,test_size=0.3)

from sklearn.tree import DecisionTreeClassifier as DT 

model=DT(criterion='entropy')
model.fit(train[predictors],train[target])
preds_test=model.predict(test[predictors])
preds_test

pd.crosstab(test[target],preds_test,rownames=['Actual'],colnames=['Predicted'])
np.mean(preds_test==test[target])