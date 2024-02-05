# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:45:32 2024

@author: Nishant
"""


#Ensemble Techniques
#Random Forest
#confusion matrix when data is imbalace
import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()
dir(iris)

df=pd.DataFrame(iris.data,columns=iris.feature_names)
df.head()
df['target']=iris.target
df.head()
df['target']=iris.target

X=df.drop('target',axis=1)
y=df.target

from sklearn.model_selection import train_test_split
#tain the data
X_train,X_test,y_train,y_test = train_test_split(df.drop(['target'],axis=1),iris.target,test_size=0.2)

from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier()
#n_estimators is the no of trees in the random forest
model.fit(X_train,y_train)

model.score(X_train,y_train)
y_predicted=model.predict(X_test)
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_predicted)
cm
'''
array([[10,  0,  0],
       [ 0, 11,  0],
       [ 0,  2,  7]], dtype=int64)

'''
#Matplotlib Inline
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10,7))
sns.heatmap(cm,annot=True)
plt.xlabel("Predicted")
plt.ylabel("Actual")



