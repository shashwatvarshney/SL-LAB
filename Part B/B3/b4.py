import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
import seaborn as sns

titanic_df=pd.read_csv("train.csv")
print("data headers")
print(titanic_df.head(10))
print("data description")
titanic_df.info()
titanic_df.describe()
titanic_df.drop(['Parch','Cabin','Ticket'],axis=1,inplace=True)
print(titanic_df.head(10))
titanic_df["SibSp"]=titanic_df["SibSp"].fillna('C2')
print(titanic_df["SibSp"])
titanic_df["Survived"]=titanic_df["Survived"].map({
    0:'Died',
    1:'Survived'
})
print(titanic_df.head(5))
titanic_df["Embarked"]=titanic_df["Embarked"].fillna('S')
titanic_df["Embarked"]=titanic_df["Embarked"].map({
    'C':'Cherbourg',
    'Q':'Queenstown',
    'S':'Southampton'
})
print(titanic_df.head(5))
titanic_df["Pclass"]=titanic_df["Pclass"].map({
    1:'Luxury Class',
    2:'Economy Class',
    3:'Lower Class'
})
print(titanic_df.head(5))
print("Visulization based on passenger status")
ax=sns.countplot(x='Pclass',hue='Survived',palette='Set1',data=titanic_df)
ax.set(title='Passenger status against class',xlabel='Passenger Class',ylabel='Total')
plt.show()
print("Visualization based on sex against servival rate")
ax=sns.countplot(x='Sex',hue='Survived',palette='Set2',data=titanic_df)
ax.set(title='Survival rate against sex')
plt.show()
print("Visualization based on ages of peoples")
interval=(0,18,35,60,120)
categories=['Children','Teens','Adult','Old']
titanic_df["Age_cats"]=pd.cut(titanic_df.Age,interval,labels=categories)
ax=sns.countplot(x='Age_cats',hue='Survived',palette='Set3',data=titanic_df)
ax.set(title='Survival rate against age')
plt.show()
