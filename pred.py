import numpy as np

import pandas as pd

import matplotlib.pyplot as plt import seaborn as sns

data pd.read_csv('winequality-red.csv') =

data.head()

data.describe() extra = data[data.duplicated()]

extra.shape

y = data.quality

X = data.drop('quality', axis=1)

print(y.shape, x.shape)

colormap = plt.cm.viridis

plt.figure(figsize=(12,12))

plt.title('Correlation of Features', y=1.05, size=15) sns.heatmap(data.astype(float).corr(), linewidths-0.1,vmax-1.0, square=True,

linecolor='white', annot=True)

from sklearn.model_selection import train_test_split, cross_val_score from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score, log loss

from sklearn.metrics import confusion matrix

x_train, x_test, y_train, y_test train_test_split(x, y, test_size-0.2, random_state-seed) RF_clf RandomForestClassifier(random_state-seed) cv_scores cross_val_score(RF_clf,x_train, y_train, cv-10, scoring='accuracy') RF_clf.fit(x_train, y_train) pred RF RF_clf.predict(x_test) master- Tk()

Label (master, text="Fixed Acidity", anchor-"m", width-15).grid(row-e)

Label (master, text="Volatile Acidity", anchor="m", width-15).grid(row=1)

Label (master, text="Citric Acid", anchor="m", width-15).grid(row-2)

Label (master, text="Residual Sugar", anchor="m", width-15).grid(row=3)

Label (master, text="Chlorides", anchor="rw", width=15).grid(row=4)

Label (master, text-"Sulfur Dioxide", anchor="nw", width-15).grid(row-5)

Label (master, text="Total Sulfur Dioxide", anchor="nw", width=15).grid(row-6)

Label (master, text-"Density", anchor="m", width-15).grid(row=7)

Label (master, text-"pH", anchor="n", width-15).grid(row-8)

Label (master, text="Sulphates", anchor="r", width-15).grid(row-9)

Label (master, text="Alcohol", anchor-"m", width-15).grid(row=10)

Label (master, text "Quality" anchor-"m", width-15).grid(row-13)

el = Entry(master)

e2- Entry(master) e3 Entry(master)


e5= Entry(master)

el.grid(row, column=1)

e2.grid(row-1, column-1)

e3.grid(row-2, column-1)

e4.grid(row-3, column-1)

es.grid(rowd, column-1)

e6.grid(row-5, column-1)

e7.grid(row-6, column-1)

es.grid(row-7, column-1)

e9.grid(row-8, column-1)

e10.grid(row-9, column-1)

ell.grid(row-10, column-1)

quality.grid(row-13, column-1)

Button(master, text-'Quit', command-master.destroy,width-15).grid(row-11, column-0, sticky-w, pady-4) Button(master, text="Find Quality', command-showQuality,width-17).grid(row-11, column-1, sticky, pady) Button(master, text='Project By',width-15).grid(row-14, column-0, sticky-, pady-4) Button(master, text="Sakshi',width=17).grid(row-14, column-1, sticky, pady-4)

mainloop()
