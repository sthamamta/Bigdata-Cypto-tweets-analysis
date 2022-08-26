
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import mean_squared_error
from sklearn.metrics import precision_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV

import pandas as pd
from sklearn.metrics import classification_report


from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB


import warnings
warnings.filterwarnings("ignore", category=FutureWarning)




#models
def logistic_regression(X_train,y_train):
    regression = LogisticRegression()
    grid = {'penalty': ['l2'], 'C': [0.01, 0.1, 1, 10],'max_iter':[300]}
    lr = GridSearchCV(regression, param_grid=grid, scoring='accuracy',cv=5)
    lr.fit(X_train, y_train)
    return lr.best_estimator_

def knearestneighbors(X_train,y_train):
    knn=KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    return knn


def decision_tree(X_train,y_train):
    param_grid = {'criterion':['gini','entropy'],'max_depth':[4,5,6,7,8,9,10,11,12,15,20,30,40,50,70,90,120,150]}
    # param_grid = [{'criterion': ['entropy', 'gini'], 'max_depth': max_depth_range},
    #             {'min_samples_leaf': min_samples_leaf_range}]
    tree = GridSearchCV(DecisionTreeClassifier(), param_grid, cv=5)
    tree.fit(X_train, y_train)
    return tree.best_estimator_


def svm(X_train,y_train):
    param_grid = {'C': [0.1, 1, 10, 100],
              'gamma': [1, 0.1, 0.01, 0.001],
              'kernel': ['rbf']}
    svm = GridSearchCV(SVC(), param_grid, refit = True, verbose = 3,cv=5)
    svm.fit(X_train, y_train)
    return svm.best_estimator_


def naive(X_train,y_train):
    gnb = GaussianNB()
    gnb.fit(X_train, y_train)
    return gnb




#utility function
def trainingResult(model,X_test,y_test):
    
    y_pred = model.predict(X_test)
    print('Misclassified samples: %d' % (y_test != y_pred).sum())
    print('Accuracy: %.2f' % accuracy_score(y_test, y_pred))


def evaluation(model,X_test,y_test):
    y_pred = model.predict(X_test)

    print(classification_report(y_test, y_pred,
                                target_names=['Under 50k', 'Over 50k']))
    print('Training Set Accuracy Score: {:.2f}'.format(
        model.score(X_train, y_train)))
    print('Testing Set Accuracy Score: {:.2f}'.format(
        model.score(X_test, y_test)))
#print a series of information about the model


def clasification_report_model(model,X_test,y_test):
    predictions = model.predict(X_test)
    print("Accuracy: " + str(accuracy_score(y_test, predictions)))
    print(classification_report(y_test, predictions))
