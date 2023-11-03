from sklearn import dataset, svm
from sklearn.model_selection import train_test_split

digits = datasets.load_iris()
data = digits.data

#n_sample = len(digits.images)
#data = digits.images.reshape((n_sample, -1))

model = svm.SVC()
x_train, X_test, y_train, y_test = train_test_split(
    data, dgits.target, shuffle = False
)
model.fit(X_train, y_train)
predicted = model.predict([X_test[0:5]])

y_test = y_test[:5]
print("Предсказания Сети")
print(predicted)
print("\nПравильные ответы")
print(y_test)