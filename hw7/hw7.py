import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder

# Загрузка данных из CSV-файла
data = pd.read_csv("titanic.csv")

# Преобразование категориального столбца "PClass" в числовой формат
label_encoder = LabelEncoder()
data["PClass"] = label_encoder.fit_transform(data["PClass"])

# Выбор признаков
features = ["PClass", "Age", "SexCode"]

# Обработка отсутствующих значений с использованием SimpleImputer
imputer = SimpleImputer(strategy="mean")
data[features] = imputer.fit_transform(data[features])

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(data[features], data["Survived"], test_size=0.2, random_state=42)

# Создание и обучение модели Logistic Regression
model = LogisticRegression()
model.fit(X_train, y_train)

# Предсказание выживаемости на тестовой выборке
predictions = model.predict(X_test)

# Расчет и вывод точности модели
accuracy = model.score(X_test, y_test)
print("Точность модели:", accuracy, "\n")

# Вывод предсказаний для 10 случайных пассажиров
random_passengers = data.sample(10)
passenger_ids = random_passengers["PassengerID"].values
names = random_passengers["Name"].values
for i in range(10):
    print("Passenger ID:", passenger_ids[i])
    print("Name:", names[i])
    if predictions[i] == 1:
        print("Выжил")
    else:
        print("Не выжил")
    print("-------------------------------------")