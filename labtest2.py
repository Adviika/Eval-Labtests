#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC


# In[8]:


data = load_diabetes()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)


X.hist(bins=15, figsize=(15, 10), color='yellow')
plt.suptitle("histogram")
plt.show()


# In[31]:


plt.figure(figsize=(10, 8))
sns.heatmap(X.corr(), annot=True, cmap='GnBu')
plt.title("heatmap")
plt.show()


# In[ ]:





# In[32]:


splits = [0.7, 0.8, 0.9]
rf_acc = []
svm_acc = []

for split in splits:
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=split, random_state=42)   
    rf = RandomForestClassifier(random_state=42)
    rf.fit(x_train, y_train)
    rf_pred = rf.predict(x_test)
    rf_acc.append(accuracy_score(y_test, rf_pred))
    
    svm = SVC()
    svm.fit(x_train, y_train)
    svm_pred = svm.predict(x_test)
    svm_acc.append(accuracy_score(y_test,svm_pred))
    
    m1 = np.mean(rf_acc)
    m2 = np.mean(svm_acc)
    
print(f"mean1: {m1:.2f}")
print(f"mean2: {m2:.2f}")


# In[35]:


splits_labels = [f'{int(100*split)}% test' for split in splits]
plt.figure(figsize=(10, 5))
plt.plot(splits_labels, rf_acc, label="Random Forest", marker='o')
plt.plot(splits_labels, svm_acc, label="SVM", marker='o')
plt.title("accuracy")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()


# In[ ]:




