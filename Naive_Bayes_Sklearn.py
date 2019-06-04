from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import numpy as np

X = np.array([[-1,-1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1,1,1,2,2,2])
clf = GaussianNB()
clf.fit(X,Y)
pred = clf.predict([[-0.8,-1]])
print(accuracy_score(pred,Y))

