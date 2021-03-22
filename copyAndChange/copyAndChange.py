#import numpy as np
import pandas as pd
from sklearn import model_selection
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets.samples_generator import make_classification
from sklearn.model_selection import KFold

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from mpl_toolkits.mplot3d import Axes3D


def K_Flod_split(K,fold,data,label):
    split_list = []
    kf = KFold(n_splits=K,shuffle = False,random_state = None)
    for train, test in kf.split(data):
        split_list.append(train.tolist())
        split_list.append(test.tolist())
    train,test=split_list[2 * fold],split_list[2 * fold + 1]
    return  data[train], data[test], label[train], label[test]


fig = plt.figure()
img = fig.add_subplot(111, projection='3d')

x=pd.read_csv("./data/female0.csv")
y=x.pop("species")
#liuchufa
#x_train,x_test,y_train,y_test=model_selection.train_test_split(x.values,y.values,test_size=0.2)
# k folder
#kf = KFold(n_splits = 5,shuffle = False,random_state = None)
#x_train,x_test,y_train,y_test = K_Flod_split(5, 5, x.values, y.values)

for m in range(10):
    scoreTotal = 0
    for i in range(10):
        x_train, x_test, y_train, y_test = model_selection.train_test_split(x.values, y.values, test_size=0.2)
        knn = KNeighborsClassifier(m+1).fit(x_train, y_train)
        # for y_pred, y_true in zip(knn.predict(x_test), y_test):
        #    print(y_pred, y_true)
        #print(knn.score(x_test, y_test))
        scoreTotal = scoreTotal + knn.score(x_test, y_test)

    #print('-----ave-----')
    print(m+1)
    print(scoreTotal / 10)





cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

x_min, x_max = x_train[:, 0].min() - 1, x_train[:, 0].max() + 1
y_min, y_max = x_train[:, 1].min() - 1, x_train[:, 1].max() + 1
z_min, z_max = x_train[:, 2].min() - 1, x_train[:, 2].max() + 1
img.scatter(x_train[:,0], x_train[:,1], x_train[:,2], c=y_train, marker='o', cmap=cmap_bold)


img.set_xlabel('X-area(cm*cm)')
img.set_ylabel('Y-length(mm)')
img.set_zlabel('Z-roundness')
#img.set_zlabel('Z ratio')

plt.savefig('fig.png', dpi=300)
